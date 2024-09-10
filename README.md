# 1. 
a. Membuat sebuah proyek Django baru
- Membuat folder di lokal (Laptop sendiri)
- Membuka folder itu pada powershell, membuat virtual environment python, lalu meng-install depedencies yg dibutuhkan
- jalankan "django-admin startproject nama_proyek ." pada terminal
- Membuat repo di github
- inisiasi repo (pastikan ada .gitignore yang diperlukan)

b. Membuat aplikasi dengan nama main pada proyek tersebut.
- Jalankan "python manage.py startapp main" untuk membuat aplikasi bernama main

c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- masukkan string 'main' ke dalam settings.py yang ada di folder proyek di bagian INSTALLED_APPS
- Memasukkan "localhost" dan "127.0.0.1" ke settings.py di tempat yang sama di bagian ALLOWED_HOSTS
- membuat folder baru bernama templates di dalam folder main, lalu membuat file bernama main.html yang akan menampilkan website yang diinginkan, main.html diisi oleh atribut yang akan dibuat seperti {{ nama_atribut }}

d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. (name,price,description)
- Edit models.py pada direktori main, lalu import models dari Django
- membuat class dengan parameter models.Model lalu buat atribut yang diinginkan pada class itu,
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
dan atribut lain yang kiranya dibutuhkan
- membuat method yang akan digunakan pada unit test untuk mengecek kebenaran kode
- melakukan migration setelah meng-edit models.py, "python manage.py makemigrations" lalu "python manage.py makemigrations"

e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Edit views.py pada direktori main dengan mengimport render dari Django dan menambahkan method show_main dengan paramater request
- Membuat dictionary yang berisi semua atribut yang dibuah pada models sebagai key dan value tiap atribut sebagai valuenya
- lalu return method render dengan parameter request, main.html, dan nama variabel dictionary

f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Edit urls.py di folder main dengan

from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

- Edit juga urls.py di folder proyek dengan mengimport include dan menambahkan 
path('', include('main.urls')),
pada urlpatterns

g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Create new project pada website PWS
- masukkan url PWS pada ALLOWED_HOSTS di folder main settings.py
- ikuti perintah pada web PWS

h. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

https://ragnall-muhammad-gopedia.pbp.cs.ui.ac.id/

http://ragnall-muhammad-gopedia.pbp.cs.ui.ac.id/

# 2.

![Bagan No 2](./main/static/images/Bagan%20README%20no%202.jpeg)

# 3. 
Dengan git, orang - orang bisa mengerjakan proyek bersama - sama dalam waktu yang sama. Hal ini dapat dilakukan dengan branching dalam git, suatu developer bisa mengerjakan fitur A dan developer lain bisa mengerjakan fitur lainnya. git juga bisa dijadikan backup, karena dengan git sebuah proyek disimpan di "dua" tempat, lokal developer masing - masing dan juga disimpan di github.

# 4. 
Karena Django menggunakan MVT yang friendly untuk pemula yang mengajarkan dasar - dasar. MVT memudahkan kode untuk dikelola, kode juga dapat digunakan kembali dalam berbagai bagian aplikasi yang berbeda, dan juga memisahkan tugas antara logika aplikasi, tampilan, dan data. Django juga menggunakan Python yang juga merupakan bahasa pemrograman untuk pemula.

# 5. 
Model pada Django disebut ORM karena Django menggunakan sistem Object Relational Mapping. Object Relational Mapping adalah teknik memanipulasi data dari database menggunakan paradigma object-oriented.
