# utils/labels.py

def generate_labels(message):
    """
    تولید متن لیبل برای هر پیام
    """
    labels = f"فرستنده: {message.from_user.full_name}\n"
    labels += f"شناسه فرستنده: {message.from_user.id}\n"
    labels += f"زمان ارسال: {message.date}\n"

    if message.forward_from_chat:
        labels += f"فرستاده شده از کانال: {message.forward_from_chat.title}\n"
    if message.forward_from_message_id:
        labels += f"لینک پست: https://t.me/{message.forward_from_chat.username}/{message.forward_from_message_id}\n"

    views = getattr(message, "views", "نامشخص")
    labels += f"تعداد بازدید: {views}\n"

    if message.entities:
        entities = [e.type for e in message.entities]
        labels += f"موجودیت‌ها: {', '.join(entities)}\n"

    return labels
