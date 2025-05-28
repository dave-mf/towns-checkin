import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, JobQueue
import datetime
import json

# Konfigurasi
BOT_TOKEN = "7886016775:AAEksvf5b7x16Xj1S5UM-gFBDJCW2xJlhWM"
USER_ID = 842061413
DATA_FILE = "streak_data.json"
REMINDER_INTERVAL = 1  # Jam interval reminder (jika belum verify)

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Fungsi untuk load & save data streak

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"last_checkin": None, "streak": 0}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def is_verified_today():
    data = load_data()
    last_checkin = data["last_checkin"]
    if last_checkin:
        last_time = datetime.datetime.fromisoformat(last_checkin)
        now = datetime.datetime.now()
        return last_time.date() == now.date()
    return False

# Fungsi reminder tiap 2 jam
async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    print("Fungsi send_reminder dipanggil")
    if is_verified_today():
        print("Sudah verify hari ini, tidak kirim reminder")
        return
    keyboard = [[InlineKeyboardButton("✅ Verify", callback_data="verify")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=USER_ID,
        text="⏰ Jangan lupa check-in Towns hari ini!",
        reply_markup=reply_markup
    )
    print("Reminder dikirim ke Telegram")

# Handler untuk /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != USER_ID:
        await update.message.reply_text("Bot ini hanya untuk pemiliknya.")
        return
    
    # Kirim pesan verify saat pertama kali start
    keyboard = [[InlineKeyboardButton("✅ Verify", callback_data="verify")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Bot reminder check-in Towns aktif!\nJangan lupa verify check-in hari ini!",
        reply_markup=reply_markup
    )

# Handler untuk tombol Verify
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.from_user.id != USER_ID:
        await query.edit_message_text("Bot ini hanya untuk pemiliknya.")
        return
    
    data = load_data()
    now = datetime.datetime.now()
    last_checkin = data["last_checkin"]
    streak = data["streak"]
    
    if last_checkin:
        last_time = datetime.datetime.fromisoformat(last_checkin)
        delta = now - last_time
        if delta.total_seconds() <= 24*60*60 and last_time.date() == (now - datetime.timedelta(days=1)).date():
            streak += 1
        elif last_time.date() == now.date():
            # Sudah verify hari ini, streak tidak berubah
            pass
        else:
            streak = 1
    else:
        streak = 1
    
    data["last_checkin"] = now.isoformat()
    data["streak"] = streak
    save_data(data)
    
    msg = f"Streak kamu sekarang: {streak} hari berturut-turut!\nLangsung check-in di sini: https://app.towns.com"
    await query.edit_message_text(msg)

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    # Inisialisasi job_queue
    job_queue = app.job_queue
    
    # Jika belum pernah verify, kirim reminder setiap 2 jam
    if not is_verified_today():
        job_queue.run_repeating(send_reminder, interval=REMINDER_INTERVAL*60*60, first=5)
    else:
        # Jika sudah verify, kirim reminder pada jam yang sama dengan verify terakhir
        data = load_data()
        last_time = datetime.datetime.fromisoformat(data["last_checkin"])
        next_time = datetime.datetime.now().replace(hour=last_time.hour, minute=0, second=0, microsecond=0)
        if datetime.datetime.now() > next_time:
            next_time += datetime.timedelta(days=1)
        job_queue.run_daily(send_reminder, time=next_time.time(), days=(0,1,2,3,4,5,6))

    app.run_polling() 