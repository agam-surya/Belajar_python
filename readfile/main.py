import io
from operator import mod

# file = open("readfile/file_text.txt", mode="r")

# print(f"status read : {file.readable()}")

# print(file.read()) # baca semua baris
# print(file.readline()) # baca perbaris
# print(file.readlines()) # baca semua lalu jadi list

# print(f"apakah file sudah diclosed ? : {file.closed}")
# file.close()
# print(f"apakah file sudah diclosed ? : {file.closed}")



# TEKNIK MEMBUKA FILE PYTHON, (with)

# with open("readfile/file_text.txt",mode="r",encoding="utf-8") as file:
#   content = file.readline()
#   print(content,end="")
  
#   file.write("AGAMSSSS")
#   print(content,end="")

# print(f"apakah file sudah diclosed ? : {file.closed}")


# TEKNIK MENGWRITE FILE PYTHON

# mode w, => menimpa, membuat file baru

with open("readfile/file_text.txt",mode="w",encoding="utf-8") as file: 
  file.write("AGAMSSSS")

print(f"apakah file sudah diclosed ? : {file.closed}")



# mode append /a, => tidak menimpa

with open("readfile/file_text.txt",mode="w",encoding="utf-8") as file: 
  file.write("AGAMSSSS\n")
  file.write("AGAMSSSS\n")

print(f"apakah file sudah diclosed ? : {file.closed}")