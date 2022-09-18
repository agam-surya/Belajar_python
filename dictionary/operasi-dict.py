## operasi dictionary

data = {
  'a':'agam',
  'b':2,
  'c':['agam','agam2'],
  'd':'agam4',
}

# # panjang dict
# panjang = len(data)
# print(panjang)

# # cek key ada ngga
# key = 'b'
# cek = key in data
# print(cek)

# # mengakses value dengan get

# print(data.get('b'))
# print(data.get('z')) # none
# print(data.get('z','tidak ditemukan')) # tidak ditemukan

# # mengupdate data

# data['a'] = "ubah"
# print(data)

# data.update({'b':'update'}) #kalo data ada akan update
# print(data)
# data.update({'g':'baru'}) #kalo data gak ada akan menambah data baru
# print(data)

# delete data dict
del data['a']
print(data)