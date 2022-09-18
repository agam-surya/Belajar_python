import datetime
import os
import random
import string

datamhs = {}

os.system('cls')

while True:
  
  print(f"\n{'PROGRAM INPUT DATA':^70}\n")
  print('='*70,'\n')
  mahasiswa= {
    'nama':input('Nama : '),
    'nim': input('NIM : '),
    'ipk':float(input('IPK : ')),
    'tgllahir': datetime.date(int(input("tahun lahir (yyyy) : ")),int(input("bulan lahir (1-12) : ")),int(input("tanggal lahir (1-31) : ")))
  }

  KEY = ''.join((random.choice(string.ascii_uppercase)) for i in range(4))
  datamhs.update({KEY:mahasiswa})

  print(f"\n{'KEY':<10} {'NAMA':<30} {'NIM':<14} {'LAHIR':<10}\n")

  print('='*70)

  for mhs in datamhs:
    KEY = mhs

    NAMA = datamhs[KEY]['nama']
    NIM = datamhs[KEY]['nim']
    IPK = datamhs[KEY]['ipk']
    TGL = str(datamhs[KEY]['tgllahir'])

    print(f"{KEY:<10} {NAMA:<30} {NIM:<14} {TGL:<10}")

  islanjut = input('mau lanjut ? (y/n)')

  if islanjut == 'n':
    break

print("SELESAI")
