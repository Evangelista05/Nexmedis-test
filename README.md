# BACKEND Sederhana dengan FastAPI 

Repositori ini dibuat sebagai bagian dari tes teknis untuk posisi Research & Development di **Nexmedis**. Proyek ini menampilkan backend sederhana dengan **FastAPI** untuk menerima dan mengirim data JSON, menyimpan data secara lokal, serta menampilkan antarmuka web untuk memperbarui informasi pengguna.

##  Deskripsi Proyek

Aplikasi ini memungkinkan:

- Pengiriman dan penerimaan data dalam format JSON.
- Penyimpanan data ke file lokal (`received_data.json`).
- Menampilkan halaman web untuk melihat dan mengubah data pengguna melalui form HTML.
- Template berbasis **Jinja2**.

---

##  Teknologi yang Digunakan

- **Python 3.9+**
- **FastAPI**
- **Pydantic**
- **Jinja2 Templates**
- **HTML5**

---

##  Struktur Proyek

Nexmedis-test/
├── main.py # Backend utama menggunakan FastAPI
├── models.py # Pydantic model (User)
├── received_data.json # File data yang diterima dan disimpan
├── templates/
│ └── index.html # Template HTML frontend
└── index.html # Antarmuka pengguna

---

##  Cara Menjalankan

### 1. Clone repositori

```bash
git clone https://github.com/Evangelista05/Nexmedis-test.git
cd Nexmedis-test

2. Install dependensi
bash
Salin
Edit
pip install fastapi uvicorn jinja2

3. Jalankan server FastAPI
bash
Salin
Edit
uvicorn main:app --reload

4. Akses aplikasi
API: http://127.0.0.1:8000/
Web Form: http://127.0.0.1:8000/page

API Docs (Swagger): http://127.0.0.1:8000/docs

 Daftar Endpoint
Method	URL	Deskripsi
GET	/	Menampilkan sapaan sederhana
GET	/send-data	Mengirim data JSON default
POST	/receive-data	Menerima JSON dari user dan menyimpannya
GET	/page	Menampilkan halaman HTML dengan form
POST	/submit-form	Menerima data dari form HTML dan simpan ke file

 Contoh Data (received_data.json)
json
Salin
Edit
{
  "name": "Evangelista",
  "age": 24
}

Tampilan Halaman /page
Menampilkan data JSON saat ini.
Form HTML untuk mengubah data.
Data akan langsung disimpan ke received_data.json.

----

 Catatan
File received_data.json otomatis dibuat saat data dikirim melalui form atau endpoint.

Template disimpan di folder templates/ sesuai kebutuhan FastAPI + Jinja2.
