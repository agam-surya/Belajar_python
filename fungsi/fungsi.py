# # argumen / parameter
# def tambah(a,b):
#   print(f"{a}+{b} = {a+b}")
# tambah(4,5)


# # default argumen
# def nama(a='agam'):
#   print(a)
# nama('surya')


# # return
# def kuadrat(a):
#   kuadrat = a*a
#   return kuadrat

# print(kuadrat(7))


# # Type Hints
# def kuadrat(a:float):
#   kuadrat = a*a
#   return kuadrat

# print(kuadrat(4))


# # *args => bisa memasukkan banyak argumen, *args tuples
# def fungsi(*args):
#   print(len(args))
#   for i in range(len(args)):
#    print(args[i])
#   print('='*20)

# fungsi(2,3,4)

# # bisa juga gini
# def fungsi(*data):
#   print(len(data))
#   for i in range(len(data)):
#     print(data[i])

# fungsi(7,3,4,0,'agam')


# **kwargs jadi dictionary

def fungsi(**kwargs):
  print(len(kwargs))
  print(kwargs['nama'])

fungsi(nama='agam2',tinggi=165,berat=55)


def math(*args,**kwargs):
  output = 0
  if kwargs["option"] == 'tambah':
    print('operasi penjumlahan')
    for a in args:
      output += a
  elif kwargs["option"] == 'kali':
    print('operasi perkalian')
    output = 1
    for a in args:
      output *= a
  else:
    print("tidak ada operasi")
  
  print(output)

math(1,2,3,4,5,option='tambah')
math(1,2,3,4,5,option='kali')