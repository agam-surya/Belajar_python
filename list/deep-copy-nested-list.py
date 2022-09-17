from copy import deepcopy


list1 = [1,2]
list2 = [3,4]

list = [list1,list2,5,6]

## nested list tidak tercopy
list_copy = list.copy()

# alamatnya sama, padahal sudah dicopy. ini adalah kesalahan, maka kita butuh deepcopy
list_copy[0][0] = 3

print(f'id (asli) dari {list1} =',hex(id(list1)))
print(f'id (nested) dari {list[0]} =',hex(id(list[0])))
print(f'id (copy) dari {list_copy[0]} =',hex(id(list_copy[0])))

print('='*40)

# deep copy = mengkopy sampai ke nested list
list_deep_copy= deepcopy(list)

print(f'id (asli) dari {list1} =',hex(id(list1)))
print(f'id (nested) dari {list[0]} =',hex(id(list[0])))
print(f'id (copy) dari {list_copy[0]} =',hex(id(list_copy[0])))
print(f'id (deepcopy) dari {list_deep_copy[0]} =',hex(id(list_deep_copy[0])))
