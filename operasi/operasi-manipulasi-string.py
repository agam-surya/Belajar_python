nama = "agam surya armanda"

status = len(nama)
print('panjang = ',status)

a = ('a')
status = a in nama
print(status) #true

a = ('A')
status = a in nama
print(status) #false

a = ('A').lower()
status = a in nama
print(status) #true

# mengulang string
print('wk'*10)

# indexing
print(nama[0])
print(nama[-2])
print(nama[0:4]) # index 0 - 3
print(nama[0:8:2]) # index 0 - 8, diloncat 2 , (0,2,4,6)

# item terkecil
print(min(nama)) # spasi
# item terbesar
print(max(nama)) # spasi

# ascii code
ascii_code = ord('a')
print(ascii_code)

data = 117

print('data = ', chr(data))

x = 10
for x in range(120):
  print(chr(x), end=' ,')


# OPERATOR DALAM BENTUK METHOD

# count
jumlah = nama.count('a')
print('\n', jumlah)

