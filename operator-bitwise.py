a=3
b=2

# bitwise or
print('=======OR=======')
c = a | b
print('nilai a :',a,'biner : ',format(a,'08b'))
print('nilai b :',b,'biner : ',format(b,'08b'))
print('------------------------')
print('nilai a | b :',c,'biner : ',format(c,'08b'))

# bitwise and
print('=======AND=======')
c = a & b
print('nilai a :',a,'biner : ',format(a,'08b'))
print('nilai b :',b,'biner : ',format(b,'08b'))
print('------------------------')
print('nilai a & b :',c,'biner : ',format(c,'08b'))

# bitwise XOR (^)
print('=======XOR=======')
c = a ^ b
print('nilai a :',a,'biner : ',format(a,'08b'))
print('nilai b :',b,'biner : ',format(b,'08b'))
print('------------------------')
print('nilai a ^ b :',c,'biner : ',format(c,'08b'))

# bitwise NOT (~)
print('=======NOT=======')
c = ~b
print('nilai a :',a,'biner : ',format(a,'08b'))
print('nilai b :',b,'biner : ',format(b,'08b'))
print('------------------------')
print('nilai a ^ b :',c,'biner : ',format(c,'08b'))

# shifting

# shift right (>>)
print('=======NOT=======')
c = a >> b # a bergeser ke kanan sebanyak b kali
print('nilai a :',a,'biner : ',format(a,'08b'))
print('nilai b :',b,'biner : ',format(b,'08b'))
print('------------------------')
print('nilai a >> b :',c,'biner : ',format(c,'08b'))

# shift left (<<)
print('=======NOT=======')
c = a << b # a bergeser ke kiri sebanyak b kali
print('nilai a :',a,'biner : ',format(a,'08b'))
print('nilai b :',b,'biner : ',format(b,'08b'))
print('------------------------')
print('nilai a << b :',c,'biner : ',format(c,'08b'))
