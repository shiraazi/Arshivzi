# bot.py

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import config
from utils.labels import generate_labels
from scheduler import start_scheduler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات آرشیوگر فعال شد!")

async def archive_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    labels = generate_labels(msg)

    if msg.photo:
        await context.bot.send_photo(
            chat_id=config.CHANNEL_ID,
            photo=msg.photo[-1].file_id,
            caption=labels
        )
    elif msg.video:
        await context.bot.send_video(
            chat_id=config.CHANNEL_ID,
            video=msg.video.file_id,
            caption=labels
        )
    elif msg.document:
        await context.bot.send_document(
            chat_id=config.CHANNEL_ID,
            document=msg.document.file_id,
            caption=labels
        )
    else:
        await context.bot.send_message(
            chat_id=config.CHANNEL_ID,
            text=(msg.text or '') + "\n\n" + labels
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(config.TOKEN).build()

    # هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, archive_post))

    # شروع Scheduler
    start_scheduler()

    # اجرای وب‌هوک
    WEBHOOK_URL = os.environ.get("WEBHOOK_URL") or f"https://your-render-service.com/{config.TOKEN}"
    PORT = int(os.environ.get("PORT", 8443))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL
    )
