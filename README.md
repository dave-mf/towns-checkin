# Towns Daily Check-in Telegram Reminder Bot

Bot ini akan mengirimkan notifikasi reminder ke Telegram Anda setiap 2 jam jika Anda belum melakukan check-in harian di aplikasi Towns. Setelah Anda klik tombol **Verify** di Telegram, reminder akan berhenti untuk hari itu dan streak Anda akan diupdate.

## Fitur
- Reminder otomatis setiap 2 jam jika belum check-in.
- Tombol **Verify** untuk konfirmasi check-in harian.
- Sistem streak harian (beruntun) yang tercatat otomatis.
- Link langsung ke [app.towns.com](https://app.towns.com) setelah verifikasi.
- Hanya merespon ke user ID tertentu (aman untuk penggunaan pribadi).

## Cara Install & Setup

### 1. Clone Repo & Masuk Folder
```bash
cd ~/projects/airdrop/towns
```

### 2. Install Python & Dependensi
Pastikan Python 3.8+ sudah terinstall.

Install library yang dibutuhkan:
```bash
pip install python-telegram-bot[job-queue]
```

### 3. Konfigurasi Token & User ID
Edit file `towns_reminder_bot.py` dan ganti:
- `BOT_TOKEN` dengan token bot Telegram Anda
- `USER_ID` dengan user id Telegram Anda

### 4. Jalankan Bot
```bash
python3 towns_reminder_bot.py
```

### 5. Mulai Chat dengan Bot
Cari bot Anda di Telegram, klik **Start** atau kirim `/start`.

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