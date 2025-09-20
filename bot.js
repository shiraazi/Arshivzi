// bot.js
// ربات آرشیوگر تلگرام به زبان جاوااسکریپت برای استفاده در Cloudflare Workers
// این فایل باید از Worker فراخوانی بشه

export async function handleRequest(update, env) {
  const TELEGRAM_TOKEN = env.TELEGRAM_BOT_TOKEN;
  const ARCHIVE_CHANNEL_ID = env.ARCHIVE_CHANNEL_ID;
  const API_URL = `https://api.telegram.org/bot${TELEGRAM_TOKEN}`;

  const msg = update.message;
  if (!msg) return { ok: true };

  // ساخت لیبل‌ها
  let labels = `👤 فرستنده: ${msg.from?.first_name || ""} ${msg.from?.last_name || ""}\n`;
  labels += `🆔 ID: ${msg.from?.id}\n`;
  labels += `⏰ تاریخ: ${new Date(msg.date * 1000).toLocaleString("fa-IR")}\n`;

  if (msg.forward_from_chat) {
    labels += `📢 منبع: ${msg.forward_from_chat.title}\n`;
  }

  // ارسال به کانال آرشیو
  if (msg.text) {
    await fetch(`${API_URL}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: ARCHIVE_CHANNEL_ID,
        text: `${msg.text}\n\n${labels}`
      })
    });
  } else if (msg.photo) {
    const photo = msg.photo[msg.photo.length - 1];
    await fetch(`${API_URL}/sendPhoto`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: ARCHIVE_CHANNEL_ID,
        photo: photo.file_id,
        caption: labels
      })
    });
  } else if (msg.document) {
    await fetch(`${API_URL}/sendDocument`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: ARCHIVE_CHANNEL_ID,
        document: msg.document.file_id,
        caption: labels
      })
    });
  } else if (msg.video) {
    await fetch(`${API_URL}/sendVideo`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: ARCHIVE_CHANNEL_ID,
        video: msg.video.file_id,
        caption: labels
      })
    });
  }

  return { ok: true };
}
