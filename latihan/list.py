datas = []
while True:
    print("\nMasukkan data buku ")
    judul = input("judul buku\t : ")
    penulis = input("penulis\t :")

    data_baru = [judul, penulis]
    datas.append(data_baru)

    print('='*30)
    for index, data in enumerate(datas):
        print(f"{index+1} | {data[0]} | {data[1]}")

    print('='*30)
    isLanjut = input("apakah ingin lanjut ? (y,n)")

    if isLanjut == 'n':
      break
print("PROGRAM SELESAI")