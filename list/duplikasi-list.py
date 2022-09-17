## menduplikat list

# cara ini akan memiliki address/memory yang sama => salah

# a = [1,3,5,7,9]
# b = a
# print('address a =',hex(id(a)))
# print('address b =',hex(id(b)))

# memakai copy() => benar, karena akan membuat list baru pada memory yang baru

a = [1,3,5,7,9]
b = a.copy()
print('address a =',hex(id(a)))
print('address b =',hex(id(b)))
