# GUPLANATION #
GUPLANATION (Gui Based Plant Recommendation System) adalah sistem berbentuk aplikasi GUI (Graphic User Interface) yang berguna untuk penentuan jenis komoditas berdasarkan karakteristik lahan. Guplation sendiri dirancang dengan bahasa pemrograman python. Dalam pengembangannya cara kerjanya, Guplation menggunakan bagian teknologi machine learning yaitu clustering (klaster). Klaster digunakan untuk membantu mempelajari serangkaian data record sebelumnya dan mengelompokkan suatu label/output tertentu berdasarkan parameter yang ia miliki. Dalam hal ini proses clustering dibantu dengan algoritma DecisionTreeClassifier yang bersumber dari library python yaitu scikit-learn.

# MEKANISME KERJA #
Algoritma DecisionTreeClassifier mengolah serangkaian data (data sheet) yang digunakan sebagai testing program atau uji serta sebagai sumber pembelajaran algoritma sehingga dapat membantu memberikan rekomendasi/keputusan. Data yang digunakan berukuran 2200 x 8 (2200 baris dan 8 kolom) yang memuat nama tanaman pada kolom terakhir serta karakteristik lahan/tanahnya pada 7 kolom lainnya yaitu kadar nitrogen (%), kadar fosfor (%), kadar kalium (%), temperatur, kelembaban relatif, pH tanah, serta curah hujan. Selain itu, dibutuhkan library numpy serta pandas dalam python untuk bagian proses serta manipulasi data. 

# TAMPILAN GUPLANATION #
![Halaman Login](https://github.com/paresqmd/GUPLANATION-/assets/143917694/e6f57942-bdac-4050-88db-6c0cc72328d7)

![Halaman katalog](https://github.com/paresqmd/GUPLANATION-/assets/143917694/7610f4c0-fb54-4dbb-84f4-0b7ebfde2443)

![Halaman katalog](https://github.com/paresqmd/GUPLANATION-/assets/143917694/2121f4e6-79b3-4165-8b52-93419581402e)


# TOOLS YANG DIGUNAKAN #
1. Visual Studio Code
2. Qt Designer
3. Adobe Ilustrator
4. Microsoft Office Excel

# Technology #
1. Python
2. tkinter
3. Scikit-Learn
4. Pandas, Numpy
