data = ['agam','surya','armanda']

# data pertama
print(f"data ke 1 = {data[0]}")
# data terakhir
print(f"data terakhir = {data[-1]}")
# mengabil panjang data
print(f"panjang data = {len(data)}")

# ubah data index
data[1]='suriya'

# append = menambah di akhir
data.append('append')
print(data)

# insert = menambah data
data.insert(1,'insert')
print(data)

# # clear = menghapus semua data
# data.clear()
# print(data)

# remove = menghapus data ..
data.remove('insert') # case sensitive
print(data)

# menghapus data terakhir
data.pop()
print(data)

# extend = menambah di akhir
data_baru = ['data','baru','nih']
data.extend(data_baru)
print(data)