#program konversi waktu ke detik

#deklarasi
class Waktu:
    jj = 0
    mm = 0
    dd = 0

jam = Waktu()
TotalDetik = 0

#algoritma input waktu berangkat konversi ke detik
j = input("masukan jam :")
m = input("masukan menit :")
d = input("masukan detik :")

jam.jj = int(j)
jam.mm = int(m)
jam.dd = int(d)
print("jam:",jam.jj,":",jam.mm,":",jam.dd)

TotalDetik = jam.dd
TotalDetik = TotalDetik + (jam.mm * 60)
TotalDetik = TotalDetik + (jam.jj * 3600)

print("Total Detik Hasil konversi:", TotalDetik)

#algoritma memasukan waktu tambahan
n = int(input('Masukan Detik Perjalan tambahan: '))

TotalDetikAkhir = TotalDetik + n

print("Total Detik Hasil Detik:", TotalDetikAkhir)

#algoritma konversi dari detik akhir ke jam,menit,detik
x = int(input('Masukan Jumlah Detik tadi lalu di konversikan ke waktu: '))

jam = x // 3600
sisa = x % 3600
menit = sisa // 60
detik = sisa % 60
print("Jadi Seseorang sampai pada pukul:")
print ('jam     : ', jam)
print ('menit   : ', menit)
print ('detik   : ', detik)
