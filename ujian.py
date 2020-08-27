#Soal 1 - Konversi Waktu (30 Poin)
def timeConverter(detik):
    try:
        detik=int(input("Masukkan detik "))#mengecek inputan
        detik = detik % (24 * 3600) #untuk menghitung jika sudah lebih dari 24 jam
        jam = detik / 3600#menghitung jumlah jam nya, /3600 per hari karena 3600 detik
        detik %= 3600#untuk menghitung jumlah detiknya
        menit = detik / 60#menghitung menit dalam setiap jam nya
        detik %= 60#menghitung detik yang tersisa jika sudah lewat dari 60 detik
        print ("%02d:%02d:%02d" % (jam, menit, detik))#ini output agar dua desimal
    except:#kalo salah masuknya kesini
        print("Invalid Input!")
timeConverter(n)