# INT

data = 0

datafloat = float(data)
print("data = ", datafloat, ', type = ', type(datafloat))
dataStr = str(data)
print("data = ", dataStr, ', type = ', type(dataStr))
dataBool = bool(data)
print("data = ", dataBool, ', type = ', type(dataBool))

# FLOAT

data = 0.0

dataInt = int(data)  # akan dibulatkan ke bawah
print("data = ", dataInt, ', type = ', type(dataInt))
dataStr = str(data)
print("data = ", dataStr, ', type = ', type(dataStr))
dataBool = bool(data)  # akan false jika nilai float 0.0
print("data = ", dataBool, ', type = ', type(dataBool))

# BOOLEAN

data = True

dataInt = int(data)  # true = 1, false = 0
print("data = ", dataInt, ', type = ', type(dataInt))
datafloat = float(data)  # true = 1.0, false = 0.0
print("data = ", datafloat, ', type = ', type(datafloat))
dataStr = str(data)  # akan jadi String
print("data = ", dataStr, ', type = ', type(dataStr))

# STRING

data = '1'

dataInt = int(data)  # String harus angka
print("data = ", dataInt, ', type = ', type(dataInt))
datafloat = float(data)  # String harus angka
print("data = ", datafloat, ', type = ', type(datafloat))
dataBool = bool(data)  # jika String kosong nilai akan false
print("data = ", dataBool, ', type = ', type(dataBool))
