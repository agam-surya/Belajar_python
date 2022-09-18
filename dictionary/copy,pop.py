datas = {
  '1':'data1',
  '2':'data2',
  '3':'data3',
  '4':'data4',
  '5':'data5',
}

## mempunyai address yang sama, ( = masih data yang sama)

# dataCopy = datas

# dataCopy = datas.copy() # ini yang benar

# # pop dict

# # menghapus data, lalu mereturn data tersebut
# data1 = datas.pop('1')

# print(datas)
# print(data1)

# # popitem dict

# menghapus data terakhir, lalu mereturn data tersebut
data1 = datas.popitem()

print(datas)
print(data1)