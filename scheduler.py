# scheduler.py

from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import TOKEN, CHANNEL_ID, ARCHIVE_INTERVAL
from sources import SOURCES
from utils.labels import generate_labels
import asyncio

bot = Bot(token=TOKEN)

async def archive_from_source(source):
    """
    مرور پست‌های جدید از یک کانال یا گروه
    توجه: با Bot API رسمی نمی‌توان پست‌های تاریخچه کانال را بدون افزودن ربات خواند.
    این تابع جایگاه برای گسترش است.
    """
    # TODO: توسعه برای خواندن پست‌های منابع با روش‌های جایگزین
    pass

async def scheduled_archive():
    for source in SOURCES:
        await archive_from_source(source)

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(lambda: asyncio.create_task(scheduled_archive()), 'interval', seconds=ARCHIVE_INTERVAL)
    scheduler.start()
