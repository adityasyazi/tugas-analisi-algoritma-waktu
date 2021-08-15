# Seseorang berangkat pukul  08 : 52 : 45
# ( pukul 08 lewat 52 menit 45 detik ) ,
# dan tiba ditujuan pukul : 12 : 15 : 10.
# Susun program untuk menghitung dan mencetak berapa jam, berapa menit dan berapa detik
# waktu yang dia habiskan dalam perjalanan.

print(">>>>>>>>>>>>>>>>>>SOAL 1 | PROGRAM DURASI WAKTU<<<<<<<<<<<<<<<<<<<<")
print("masukan dalam format 24jam")
jamawaljam = int(input("masukan jam awal: "))
jamawalmenit = int(input("masukan menit awal: "))
jamawaldetik = int(input("masukan detik awal: "))
print("\t\t\t\t\t ")
jamakhirjam = int(input("masukan jam akhir: "))
jamakhirmenit = int(input("masukan menit akhir: "))
jamakhirdetik = int(input("masukan menit akhir: "))
detikawal = jamawaljam * 3600 + jamawalmenit * 60 + jamawaldetik
detikakhir = jamakhirjam * 3600 +jamakhirmenit * 60 + jamakhirdetik

if(detikawal < detikakhir):
    durasi = detikakhir - detikawal
else:
    durasi = (detikakhir+24*3600)-detikawal

#konversi
jamdurasijam = durasi/3600
jamdurasimenit = (durasi%3600)/60
jamdurasidetik = durasi%60

#konversi (am 00.00-11.59 pm 12.00-23.59)

print("Lama Perjalanan Aadalah %d jam %d menit %d detik" % (jamdurasijam, jamdurasimenit, jamdurasidetik))