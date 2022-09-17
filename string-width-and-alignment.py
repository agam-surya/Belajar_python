nama = "agam"
umur = 12
tinggi = 165
kelas = '3E'

data = f"""
nama = {nama}
umur = {umur}
tinggi = {tinggi}
kelas = {kelas}
"""
print(data)

# mengatur lebar biar rapi

data = f"""
nama   = {nama:>10}
umur   = {umur:>10}
tinggi = {tinggi:>10}
kelas  = {kelas:>10}
"""
print(data)
