from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class PemesananForm(FlaskForm):
    nama = StringField(
        "Nama pemesan",
        validators=[
            DataRequired(message="Nama wajib diisi."),
            Length(min=3, max=50, message="Nama harus 3–50 karakter.")
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email wajib diisi."),
            Email(message="Masukkan alamat email yang valid."),
        ],
    )
    jenis_tiket = SelectField(
        "Jenis tiket",
        coerce=int,
        validators=[DataRequired(message="Silakan pilih jenis tiket.")],
    )
    jumlah = IntegerField(
        "Jumlah tiket",
        validators=[
            DataRequired(message="Jumlah tiket wajib diisi."),
            NumberRange(min=1, max=10, message="Jumlah tiket harus 1–10."),
        ],
    )
    catatan = TextAreaField(
        "Catatan (opsional)",
        validators=[Length(max=200, message="Catatan maksimal 200 karakter.")],
    )
    submit = SubmitField("Kirim pemesanan")


class TiketForm(FlaskForm):
    nama = StringField(
        "Nama tiket",
        validators=[
            DataRequired(message="Nama tiket wajib diisi."),
            Length(min=3, max=50, message="Nama tiket harus 3–50 karakter."),
        ],
    )
    kategori = SelectField(
        "Kategori",
        choices=[
            ("Festival Pass", "Festival Pass"),
            ("2-Day Pass", "2-Day Pass"),
            ("VIP", "VIP"),
        ],
        validators=[DataRequired(message="Kategori wajib dipilih.")],
    )
    harga = IntegerField(
        "Harga (Rupiah)",
        validators=[
            DataRequired(message="Harga wajib diisi."),
            NumberRange(min=1, message="Harga harus lebih dari Rp0."),
        ],
    )
    kuota = IntegerField(
        "Kuota tiket",
        validators=[
            DataRequired(message="Kuota wajib diisi."),
            NumberRange(min=0, message="Kuota tidak boleh negatif."),
        ],
    )
    deskripsi = TextAreaField(
        "Deskripsi",
        validators=[
            DataRequired(message="Deskripsi wajib diisi."),
            Length(min=10, max=200, message="Deskripsi harus 10–200 karakter."),
        ],
    )
    submit = SubmitField("Tambah tiket")
