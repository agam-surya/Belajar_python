# data = input("masukkan data: ") # data input pasti jadi string
# print("data = ", data,", type = ",type(data))

# # INT

# data2 = int(input("masukkan data: ")) # data input dicasting jadi int
# print("data = ", data2,", type = ",type(data2))

# # FLOAT

# data2 = float(input("masukkan data: ")) # data input dicasting jadi float
# print("data = ", data2,", type = ",type(data2))

# BOOLEAN

data1 = bool(input("masukkan data: ")) # input akan selalu bernilai true kecuali dikosongi

print("data = ", data1,", type = ",type(data1))

data2 = bool(int(input("masukkan data: "))) # input akan bernilai false jika 0, dan true jika 1, karena string dicasting jadi integer

print("data = ", data2,", type = ",type(data2))