from flask import Flask, render_template, request, redirect, url_for, flash
import re

from forms import PemesananForm, TiketForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nadaraya-fest-demo-secret-key"

# Data contoh festival dan tiket (bukan transaksi/pembayaran sungguhan)
TIKET = [
    {"id": 1, "nama": "Early Bird", "kategori": "Festival Pass", "harga": 175000, "kuota": 500,
     "deskripsi": "Akses festival satu hari dengan harga presale."},
    {"id": 2, "nama": "Regular Pass", "kategori": "Festival Pass", "harga": 250000, "kuota": 1200,
     "deskripsi": "Akses festival satu hari untuk menikmati seluruh panggung."},
    {"id": 3, "nama": "Weekend Pass", "kategori": "2-Day Pass", "harga": 425000, "kuota": 600,
     "deskripsi": "Akses dua hari festival dengan satu tiket."},
    {"id": 4, "nama": "VIP Experience", "kategori": "VIP", "harga": 650000, "kuota": 150,
     "deskripsi": "Area menonton khusus dan jalur masuk prioritas."}
]

USERNAME_TERDAFTAR = ["farid", "andhika", "kholil"]
PEMESANAN_TERAKHIR = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html")


@app.route("/tiket")
def tiket():
    return render_template("tiket.html", tiket=TIKET)


@app.route("/tiket/<int:id>")
def detail_tiket(id):
    item = next((t for t in TIKET if t["id"] == id), None)
    if item is None:
        return render_template("404.html"), 404
    return render_template("detail_tiket.html", item=item)


@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


@app.route("/cek", methods=["GET", "POST"])
def cek_username():
    username = ""
    hasil = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if not re.fullmatch(r"[A-Za-z0-9_]{4,20}", username):
            hasil = "tidak_valid"
        elif username.lower() in USERNAME_TERDAFTAR:
            hasil = "dipakai"
        else:
            hasil = "tersedia"
    return render_template("cek.html", username=username, hasil=hasil)


@app.route("/pesan", methods=["GET", "POST"])
def pesan():
    global PEMESANAN_TERAKHIR

    form = PemesananForm()
    form.jenis_tiket.choices = [
        (t["id"], f'{t["nama"]} — Rp{t["harga"]:,}'.replace(",", "."))
        for t in TIKET
        if t["kuota"] > 0
    ]
    if form.validate_on_submit():
        item = next(t for t in TIKET if t["id"] == form.jenis_tiket.data)

        if form.jumlah.data > item["kuota"]:
            form.jumlah.errors.append(
                f"Kuota {item['nama']} tersisa {item['kuota']} tiket."
            )
        else:
            PEMESANAN_TERAKHIR = {
                "nama": form.nama.data.strip(),
                "email": form.email.data.strip(),
                "jenis_tiket": item["nama"],
                "jumlah": form.jumlah.data,
                "catatan": (form.catatan.data or "").strip(),
            }
            flash(
                "Pemesanan berhasil dikirim. Ini hanya simulasi pembelajaran, "
                "tidak ada pembayaran sungguhan.",
                "success",
            )
            return redirect(url_for("konfirmasi"))

    return render_template("pesan.html", form=form)


@app.route("/konfirmasi")
def konfirmasi():
    return render_template(
        "konfirmasi.html",
        data=PEMESANAN_TERAKHIR,
    )


@app.route("/admin/tiket", methods=["GET", "POST"])
def admin_tiket():
    form = TiketForm()

    if form.validate_on_submit():
        tiket_baru = {
            "id": max((t["id"] for t in TIKET), default=0) + 1,
            "nama": form.nama.data.strip(),
            "kategori": form.kategori.data,
            "harga": form.harga.data,
            "kuota": form.kuota.data,
            "deskripsi": form.deskripsi.data.strip(),
        }
        TIKET.append(tiket_baru)
        flash(
            f'Tiket "{tiket_baru["nama"]}" berhasil ditambahkan ke katalog.',
            "success",
        )
        return redirect(url_for("admin_tiket"))

    return render_template("admin_tiket.html", form=form, tiket=TIKET)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
