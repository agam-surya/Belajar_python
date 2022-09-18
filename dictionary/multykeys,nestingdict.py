import datetime
import os


mahasiswa = {
    'nama': 'agam surya',
    'nim': '362055401123',
    'ipk': 3.8,
    'beasiswa': True,
    'tgllahir': datetime.date(2001, 9, 25)
}
mahasiswa2 = {
    'nama': 'agam surya2',
    'nim': '362055401124',
    'ipk': 3.9,
    'beasiswa': False,
    'tgllahir': datetime.date(2002, 5, 15)
}
mahasiswa3 = {
    'nama': 'agam surya3',
    'nim': '362055401125',
    'ipk': 3.5,
    'beasiswa': True,
    'tgllahir': datetime.date(2002, 2, 23)
}

datamhs = {
    'key1': mahasiswa,
    'key2': mahasiswa2,
    'key3': mahasiswa3
}

os.system("cls")

print(f"{'KEY':<10} {'NAMA':<17} {'NIM':<14} {'BEASISWA':<10} {'LAHIR':<10}")
print('='*70)

for mhs in datamhs:
    KEY = mhs

    NAMA = datamhs[KEY]['nama']
    NIM = datamhs[KEY]['nim']
    IPK = datamhs[KEY]['ipk']
    BEASISWA = datamhs[KEY]['beasiswa']
    TGL = str(datamhs[KEY]['tgllahir'])

    print(f"{KEY:<10} {NAMA:<17} {NIM:<14} {BEASISWA:>10} {TGL:<10}")
