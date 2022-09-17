from operator import contains


data = [2,2,1,4,3,4,5,8,6]
print(data)

# count = menghitung banyak data tertentu
print(data.count(4))

# ambil posisi data
print(data.index(4))

# mengurutkan data
data.sort(reverse=True)
print(data)
