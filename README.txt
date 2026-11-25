NADARAYA FEST - TUGAS INDIVIDU 7

Project ini merupakan kelanjutan dari project NadaRaya Fest sebelumnya.
Perubahan utama:
- Form pemesanan tiket pengunjung menggunakan Flask-WTF.
- Form tambah tiket admin menggunakan Flask-WTF.
- CSRF Token melalui form.hidden_tag().
- Validasi server-side dengan DataRequired, Length, Email, dan NumberRange.
- Pesan error ditampilkan di bawah field yang bermasalah.
- Nilai input otomatis dipertahankan ketika validasi gagal.
- Flash message setelah proses berhasil.
- Pola Post/Redirect/Get (PRG) pada pemesanan dan tambah tiket.
- Desain dan struktur utama project lama dipertahankan.

CARA MENJALANKAN

1. Buat virtual environment:
   python -m venv venv

2. Aktifkan:
   Windows:
   venv\Scripts\activate
   macOS/Linux:
   source venv/bin/activate

3. Install dependency:
   pip install -r requirements.txt

4. Jalankan:
   python app.py

5. Buka:
   http://127.0.0.1:5000/

HALAMAN FITUR

/pesan       = Form pemesanan tiket pengunjung
/admin/tiket = Form tambah tiket admin
/tiket       = Katalog tiket
/konfirmasi   = Hasil redirect setelah pemesanan berhasil
