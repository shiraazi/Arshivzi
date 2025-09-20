# config.py
# =======================
# خواندن تنظیمات از GitHub Secrets یا متغیر محیطی
# =======================

import os

# توکن ربات
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# کانال مقصد آرشیو
CHANNEL_ID = os.environ.get("ARCHIVE_CHANNEL_ID")

# بازه زمانی مرور منابع (ثانیه)
ARCHIVE_INTERVAL = int(os.environ.get("ARCHIVE_INTERVAL", 60))
