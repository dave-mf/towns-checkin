# Towns Check-in Reminder Bot

Bot Telegram untuk mengingatkan check-in harian di aplikasi Towns. Bot ini akan membantu Anda mempertahankan streak check-in dengan mengirimkan pengingat secara otomatis.

## Fitur

- ✅ Pengingat otomatis untuk check-in harian
- 🔄 Sistem streak untuk melacak check-in berturut-turut
- ⏰ Pengingat setiap 1 jam jika belum melakukan check-in
- 🎯 Pengingat pada jam yang sama dengan check-in terakhir setelah verify
- 🔒 Keamanan dengan verifikasi user ID
- 💾 Penyimpanan data streak secara lokal

## Cara Penggunaan

1. Jalankan bot dengan perintah:
   ```bash
   python towns_reminder_bot.py
   ```

2. Bot akan langsung mengirimkan pesan verify saat pertama kali dijalankan

3. Klik tombol "✅ Verify" setiap kali Anda melakukan check-in di Towns

4. Bot akan mengirimkan pengingat:
   - Setiap 1 jam jika belum melakukan check-in hari ini
   - Pada jam yang sama dengan check-in terakhir setelah verify

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

## Instalasi

1. Clone repository ini
2. Install dependencies:
   ```bash
   pip install python-telegram-bot
   ```
3. Update `BOT_TOKEN` dan `USER_ID` di `towns_reminder_bot.py`
4. Jalankan bot

## Catatan

- Bot akan menyimpan data streak di file `streak_data.json`
- Pastikan bot memiliki akses untuk mengirim pesan ke chat Anda
- Streak akan direset jika melewatkan check-in selama 24 jam

## Troubleshooting
- **PermissionError saat klik Verify:**
  - Pastikan user yang menjalankan script punya izin menulis file di folder tersebut.
  - Jika perlu, jalankan:
    ```bash
    touch streak_data.json
    chmod 666 streak_data.json
    ```
- **Tidak ada notifikasi:**
  - Pastikan sudah menjalankan `/start` di Telegram.
  - Pastikan token dan user id sudah benar.
  - Cek log terminal untuk error.

## Customisasi
- Ubah interval reminder dengan mengedit variabel `REMINDER_INTERVAL` di script (dalam jam).
- Untuk multi-user, perlu modifikasi script agar menyimpan data per user.

## Lisensi
Bebas digunakan dan dimodifikasi untuk keperluan pribadi.

---

**Dibuat oleh: [DaveMF & Cursor 😂]** 