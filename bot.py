import os
import tempfile
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from PyPDF2 import PdfReader
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

# ================= CONFIGURATION =================
TOKEN = ""  # Your Telegram bot token
MODEL_NAME = "philschmid/bart-large-cnn-samsum"           # Specialized summarization model


# Initialize AI pipeline
summarizer = pipeline(
    "summarization",
    model=MODEL_NAME,
    device=-1,  # -1 for CPU, 0 for GPU
    framework="pt",
    truncation=True,
    model_kwargs={
        
        "repetition_penalty": 2.0,
        "no_repeat_ngram_size": 3
    }
)

# ================= CORE FUNCTIONALITY =================
async def summarize_content(text: str) -> str:
    """Generate structured summary with key insights"""
    try:
        # Clean and prepare text
        clean_text = " ".join(text.replace("\n", ". ").split()[:3000])
        
        # Generate AI summary
        result = summarizer(
            clean_text,
            max_length=1000,
            min_length=700,
            do_sample=True,
            early_stopping=True
        )
        
        # Format professional summary
        summary = result[0]['summary_text']
        key_points = [f"• {point.strip()}" for point in summary.split(". ") if point]
        
        return (
            "📌 **Key Insights**\n\n" +
            "\n".join(key_points[:5]) + "\n\n" +
            "🔍 **Executive Summary**\n" +
            f"{summary.split('.')[0]}"
        )
        
    except Exception as e:
        return f"⚠️ Summarization Error: {str(e)}"

# ================= PDF PROCESSING =================
def extract_pdf_text(file_path: str) -> str:
    """Extract text from PDF with layout preservation"""
    try:
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            return " ".join([
                page.extract_text() 
                for page in reader.pages 
                if page.extract_text()
            ])
    except Exception as e:
        raise RuntimeError(f"PDF Read Error: {str(e)}")

async def handle_pdf(update: Update, context: CallbackContext):
    """Process PDF files end-to-end"""
    temp_path = None
    try:
        # Download PDF
        file = await context.bot.get_file(update.message.document.file_id)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_path = temp_file.name
        await file.download_to_drive(temp_path)
        
        # Process and summarize
        text = extract_pdf_text(temp_path)
        summary = await summarize_content(text)
        await update.message.reply_text(summary, parse_mode="Markdown")
        
    except Exception as e:
        await update.message.reply_text(f"❌ PDF Error: {str(e)}")
        
    finally:
        if temp_path and os.path.exists(temp_path):
            try: os.remove(temp_path)
            except: pass

# ================= YOUTUBE PROCESSING =================
def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from various URL formats"""
    if "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    raise ValueError("Invalid YouTube URL")

async def handle_youtube(update: Update, context: CallbackContext):
    """Process YouTube videos end-to-end"""
    try:
        # Get transcript
        video_id = extract_video_id(update.message.text)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry["text"] for entry in transcript])
        
        # Generate summary
        summary = await summarize_content(text)
        await update.message.reply_text(summary, parse_mode="Markdown")
        
    except Exception as e:
        await update.message.reply_text(f"❌ YouTube Error: {str(e)}")

# ================= TELEGRAM SETUP =================
async def start(update: Update, context: CallbackContext):
    """Welcome message with instructions"""
    welcome_msg = """🎓 **Smart Content Summarizer** 🎓

Send me:
- 📄 PDF files for document summaries
- ▶️ YouTube links for video summaries

I'll provide:
✅ Key insights
✅ Executive summary
✅ Important highlights"""
    await update.message.reply_text(welcome_msg, parse_mode="Markdown")

# Initialize bot
application = Application.builder().token(TOKEN).build()

# Register handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
application.add_handler(MessageHandler(
    filters.TEXT & ~filters.COMMAND & (
        filters.Entity("url") | 
        filters.Entity("TEXT_LINK")
    ), 
    handle_youtube
))

# ================= MAIN EXECUTION =================
if __name__ == "__main__":
    print("🤖 AI Summarizer Bot Activated")
    application.run_polling()
