from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data default awal (bisa diganti-ganti lewat web nanti)
data_undangan = {
    "pria": "Romeo",
    "wanita": "Juliet",
    "tanggal": "12 Desember 2026",
    "link_foto": "https://unsplash.com",
    "link_bg": "https://unsplash.com" # Background mewah emas/lampu
}

@app.route('/')
def home():
    return render_template('index.html', info=data_undangan)

# Fungsi untuk memproses perubahan saat tombol "Simpan" diklik
@app.route('/update', methods=['POST'])
def update():
    data_undangan['pria'] = request.form['pria']
    data_undangan['wanita'] = request.form['wanita']
    data_undangan['tanggal'] = request.form['tanggal']
    data_undangan['link_foto'] = request.form['link_foto']
    data_undangan['link_bg'] = request.form['link_bg']
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
