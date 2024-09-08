my_dict={'Ирина': 1985, "Света": 1998}
print(my_dict)
print(my_dict['Ирина'])
my_dict['Евгений']=2000
print(my_dict)
my_dict.update({'Юра':1982, 'Лида': 2005})
print(my_dict)
a=my_dict.pop('Света')
print(my_dict)
print(a)


my_set={2, 5, False, False, 6.9, 6.9, 2, 5}
print(my_set)
print(my_set.add(4))
print(my_set.add(7))
print(my_set.discard(6.9))
print(my_set)