data0 = ['agam', 2]
data1 = ['surya', 4]

datas = [data0, data1,1,2]
print(datas)

# memanggil list 2d

# print(datas[0][0])


# for data in datas:
#   if isinstance(data,list):
#     for i in data:
#       print(i)
#   else:
#     print(data)


# PERMASALAHAN dengan copy(), kita hanya akan mengcopy luarnya saja, sedangkan alamat data didalam listnya tetap sama, sehingga ketika merubah datanya akan tetap mempengaruhi semua list

print(hex(id(data0[0])))

for data in datas:
  if isinstance(data,list):
    for i in data:
      print(f'alamat {i} = ',hex(id(i)))
  else:
    print(f'alamat {data} = ',hex(id(data)))

datas[0][0] = "ubah"

# kedua list ikut berubah
print(data0)
print(datas)

# cara mengatasinya ada di deep copy-nested-list.py
