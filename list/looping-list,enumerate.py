angkas = [7,3,9,4,8,0,2,6,9]

# # for loop
# for angka in angkas:
#   print(angka)


# mengambil indexnya

# # for loop dan range

# for angka in range(len(angkas)):
#   print(angkas[angka])

# # while loop

# i =0
# while i <len(angkas):
#   print(angkas[i])
#   i+=1


# # list comperhension
# [print(i) for i in angkas]

# # enumerate = mengambil index dan datanya

# for index, data in enumerate(angkas):
#   print(f'index = {index}, data = {data}')


# penggabungan dengan comperhension

# # dengan enumerate
# [print(f'index = {index}, data = {data}') for index,data in enumerate(angkas)]

# membuat list baru dengan manipulasi dari list diatas

baru = [i**2 for i in angkas]
print(baru)