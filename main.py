from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Biodata Diri</p><p>Nama : Naily Iqomatar Rosyidah </p><p>NIM : 22083000033</p><p>Prodi : Sistem Informasi</p><p>Tempat,tanggal lahir : Malang, 23 November 2003</p><p> Alamat : Dusun Ketapang, Kepanjen, Malang</p><p>Jenis Kelamin : Perempuan</p><p> kewarganegaraan : Indonesia</p><p>Agama : Islam</p><p>Instansi : Universitas Merdeka Malang</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
