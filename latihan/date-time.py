import datetime as dt

# ini tidak sempurna

hariini = dt.date.today()
print(hariini)

tanggal = int(input("masukkan tanggal lahir : "))
bulan = int(input("masukkan bulan lahir : "))
tahun = int(input("masukkan tahun lahir : "))

tanggalku = dt.date(tahun,bulan,tanggal)
umurku = hariini-tanggalku
umurku //= 365
print("umurku adalah = ", umurku.days," tahun")