# Table of Contents
[Tugas 2](#Tugas-2) <br>
[Tugas 3](#Tugas-3)

## Tugas 2
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan No 2](./main/static/images/Bagan%20README%20no%202.jpeg)

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Dengan git, orang - orang bisa mengerjakan proyek bersama - sama dalam waktu yang sama. Hal ini dapat dilakukan dengan branching dalam git, suatu developer bisa mengerjakan fitur A dan developer lain bisa mengerjakan fitur lainnya. git juga bisa dijadikan backup, karena dengan git sebuah proyek disimpan di "dua" tempat, lokal developer masing - masing dan juga disimpan di github.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django menggunakan MVT yang friendly untuk pemula yang mengajarkan dasar - dasar. MVT memudahkan kode untuk dikelola, kode juga dapat digunakan kembali dalam berbagai bagian aplikasi yang berbeda, dan juga memisahkan tugas antara logika aplikasi, tampilan, dan data. Django juga menggunakan Python yang juga merupakan bahasa pemrograman untuk pemula.

### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM karena Django menggunakan sistem Object Relational Mapping. Object Relational Mapping adalah teknik memanipulasi data dari database menggunakan paradigma object-oriented.

---

## Tugas 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita perlu data delivery dalam pengimplementasian sebuah platform karena data delivery yang efisien memastikan website/app berjalan dengan lancar, sehingga memberikan user experience baik.
### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, tidak bisa dikatakan secara objektif yang lebih baik antara XML dan JSON, mereka memiliki kelebihan dan kekurangan masing - msaing. Alasan JSON lebih populer dibandingkan XML adalah karena beberapa hal:
<br>1. JSON lebih mudah untuk dibaca/ditulis dibandingkan XML
<br>2. Sebagian besar language dan framework modern memiliki built-in support untuk JSON
<br>3. Banyak web API yang lebih memilih JSON karena lebih mudah diintegrasikan dengan aplikasi berbasis JavaScript
### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() adalah method yang memeriksa apakah data di form yang dikirimkan oleh user valid sesuai validasi yang ditentukan. Method ini penting karena kita dapat memastikan kebenaran data dan menjaga dari input berbahaya.
### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita menggunakan csrf_token untuk memastikan request asli dan berasal dari orang yang diinginkan. <br>
Tanpa csrf_token, seseorang bisa mendapatkan akses ke aplikasi yang tidak sah<br>
Penyerang membuat request yang mengatasnamakan user, tanpa csrf_token, request asli dan request berbahaya tidak dapat bisa dibedakan

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
