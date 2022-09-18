# looping dan mengambil data dengan method keys(), values(), items()

datas = {
  '1':'data1',
  '2':'data2',
  '3':'data3',
  '4':'data4',
  '5':'data5',
}

# ini hanya akan mengambil key nya
for data in datas:
  print(data)

print('=='*20)


# # mengambil valuenya

# dengan get(key)
for data in datas.keys():
  print(datas.get(data))

print('=='*20)

# dengan values()
for data in datas.values():
  print(data)

print('=='*20)


# dengan items() => akan mengambil key dan values sekaligus
for data in datas.items():
  print(data)

# bisa juga begini
for key,values in datas.items():
  print(f"key = {key}, value = {values}")
