a = 3 > 2 #true
a = 3 < 2 #false
a = 3 >= 2 #true
a = 3 <= 2 #false
a = 3 == 2 #false
a = 3 != 2 #true

# IS dan IS NOT

x = 5
y = 5

# 2 VARIABEL YANG BERNILAI SAMA AKAN DIMASUKKAN KE MEMORI YANG SAMA (CONST)
print("nilai x =",x,'id = ',hex(id(x)))
print("nilai y =",y,'id = ',hex(id(y)))

hasil = x is y
hasil = x is 5 # lebih baik pake == daripada is

print(hasil) # hasil akan true karena memori sama
