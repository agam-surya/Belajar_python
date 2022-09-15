# membuat gabungan area rentang dari angka


# ++++3----10++++

inputan = float(
    input(" masukkan angka yang bernilai kurangdari 3 atau  lebih dari 10 : "))

isKurangDari = (inputan < 3)
isLebihDari = (inputan > 10)
isBenar = isKurangDari or isLebihDari

print("kurang dari 3 ? ", isKurangDari)
print("lebih dari 10 ? ", isLebihDari)
print("angka yang anda masukkan = ", isBenar)

# ----3++++10----

print('\n', 15*'=', '\n')

inputan = float(input(" masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))

isKurangDari = (inputan < 10)
isLebihDari = (inputan > 3)
isBenar = isKurangDari and isLebihDari

print("lebih dari 3 ? ", isKurangDari)
print("kurang dari 10 ? ", isLebihDari)
print("angka yang anda masukkan = ", isBenar)
