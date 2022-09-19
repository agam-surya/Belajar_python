# def kuadrat(a):
#     a *= a
#     print(a)


# kuadrat(2)


# # lambda

# def kuadrat(angka): return angka**2


# print(kuadrat(3))

# # 2 parameter


# def tambah(angka1, angka2): return angka1+angka2


# print(tambah(3, 4))


# # sorting list

# # biasanya begini bro

# datalist = ['otong', 'ucup', 'dudung']

# datalist.sort()
# print(f"sorted list = {datalist}")

# datalist.sort(key=len)
# print(f"sorted list by len = {datalist}")


# def panjang(a):
#     return len(a)

# datalist.sort(key=panjang)
# print(f"sorted list by panjang fungsi = {datalist}")

# datalist.sort(key= lambda a:len(a))
# print(f"sorted list by panjang lambda = {datalist}")


# # filter

# datas= [1,2,3,4,5,6,7,8,9]

# datagenap = list(filter(lambda a:(a%2==0),datas))
# dataganjil = list(filter(lambda a:a%2,datas))

# print(datagenap)
# print(dataganjil)


# # ANONYMOUS
# currying => haskell curry

def pangkat(angka,n):
  return angka**n

hasil = pangkat(2,3)
print(f"fungsi biasa = {hasil}")

# dengan currying
def pangkat2(angka):
  return lambda n:angka**n


print(f"fungsi currying = {pangkat2(2)(3)}")

hasil2 = pangkat2(2)
print(f"fungsi currying = {hasil2(3)}")