# Towns Check-in Reminder Bot

Bot Telegram untuk mengingatkan check-in harian di aplikasi Towns. Bot ini akan membantu Anda mempertahankan streak check-in dengan mengirimkan pengingat secara otomatis.

## Fitur

- ✅ Pengingat otomatis untuk check-in harian
- 🔄 Sistem streak untuk melacak check-in berturut-turut
- ⏰ Pengingat setiap 1 jam jika belum melakukan check-in
- 🎯 Pengingat pada jam yang sama dengan check-in terakhir setelah verify
- 🔒 Keamanan dengan verifikasi user ID
- 💾 Penyimpanan data streak secara lokal
- 🌐 Tombol langsung ke website Towns

## Cara Penggunaan

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/towns-reminder-bot.git
   cd towns-reminder-bot
   ```

2. Install dependencies:
   ```bash
   pip install python-telegram-bot
   ```

3. Konfigurasi bot:
   - Buka `towns_reminder_bot.py`
   - Update `BOT_TOKEN` dengan token bot Telegram Anda
   - Update `USER_ID` dengan ID Telegram Anda

4. Jalankan bot:
   ```bash
   python towns_reminder_bot.py
   ```

5. Di Telegram:
   - Mulai chat dengan bot Anda
   - Kirim perintah `/start`
   - Klik tombol "✅ Verify" setiap kali Anda melakukan check-in
   - Klik tombol "🌐 Buka Towns" untuk langsung ke website

## Konfigurasi

Bot dapat dikonfigurasi dengan mengubah variabel berikut di `towns_reminder_bot.py`:

- `BOT_TOKEN`: Token bot Telegram Anda
- `USER_ID`: ID Telegram pengguna yang diizinkan menggunakan bot
- `REMINDER_INTERVAL`: Interval pengingat dalam jam (default: 1 jam)

## Persyaratan

- Python 3.7+
- python-telegram-bot library
- Koneksi internet aktif
- Token bot Telegram yang valid

## Catatan

- Bot akan menyimpan data streak di file `streak_data.json`
- Pastikan bot memiliki akses untuk mengirim pesan ke chat Anda
- Streak akan direset jika melewatkan check-in selama 24 jam

## Kontribusi

Silakan buat pull request untuk kontribusi. Untuk perubahan besar, harap buka issue terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

## Lisensi

[MIT](https://choosealicense.com/licenses/mit/)

---

**Dibuat oleh: [DaveMF & Cursor 😂]** 