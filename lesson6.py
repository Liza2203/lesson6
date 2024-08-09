my_dict={'Liza':2007, "Olya":2005}
print(my_dict)
print(my_dict['Liza'])
print(my_dict.get('Nastya'))
my_dict.update({'Masha':2008, 'Kostya':2000})
print(my_dict["Olya"])
my_dict.pop('Olya')
print(my_dict)


set_my={2,True,True,'lol'}
print(set_my)
set_my.add(5)
set_my.add('no')
set_my.discard(True)
print(set_my)