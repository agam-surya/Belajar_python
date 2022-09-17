nama = "agam surya armanda"

# status = len(nama)
# print('panjang = ',status)

# a = ('a')
# status = a in nama
# print(status) #true

# a = ('A')
# status = a in nama
# print(status) #false

# a = ('A').lower()
# status = a in nama
# print(status) #true

# # mengulang string
# print('wk'*10)

# # indexing
# print(nama[0])
# print(nama[-2])
# print(nama[0:4]) # index 0 - 3
# print(nama[0:8:2]) # index 0 - 8, diloncat 2 , (0,2,4,6)

# # item terkecil
# print(min(nama)) # spasi
# # item terbesar
# print(max(nama)) # spasi

# # ascii code
# ascii_code = ord('a')
# print(ascii_code)

# data = 117

# print('data = ', chr(data))

# x = 10
# for x in range(120):
#   print(chr(x), end=' ,')


# OPERATOR DALAM BENTUK METHOD

# count
jumlah = nama.count('a')
print('\n', jumlah)

# uppercase & lowercase

upper = nama.upper()
print(upper)
lower = nama.lower()
print(lower)

# pengecekan dengan isX method

# isalpha() = mengecek apakah semuanya huruf
# isalnum() = mengecek apakah semuanya huruf dan angka
# isdecimal() = mengecek apakah semuanya angka
# isspace() = mengecek apakah semuanya spasi, tab, newline
# istitle() = mengecek apakah semua kata dimulai dengan huruf besar

cek = nama.islower()
print(cek)
cek = nama.isupper()
print(cek)

# mengecek komponen startswith() endswith()

cek_start = nama.startswith('Agam')  # case sensitive
cek_end = nama.upper().endswith('ARMANDA')  # case sensitive
print(cek_start)
print(cek_end)

# penggabungan komponen join() split()
pisah = ['agam', 'surya', 'armanda']
gabung = ','.join(pisah)
print(gabung)

pisah_lagi = gabung.split(',') # jadi list
print(pisah_lagi)

# menambahkan karakter rjust() ljust() center()

kanan = "kanan".rjust(10,'-')
print("'",kanan,"'")
kiri = "kiri".ljust(10,'-')
print("'",kiri,"'")
center = "center".center(10,'-')
print("'",center,"'")

# menghapus karakter strip()

print(kanan.strip('-'))