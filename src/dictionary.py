

my_dict = {'a': '학생1', 'b': '학생2', 'c': '학생3', 'd': '학생4'}

print(my_dict['a'])
print(my_dict)

del my_dict['b']
print(my_dict)

for std in my_dict.values():
    print(std)

for key in my_dict.keys():
    print(key)

for key, val in my_dict.items():
    print(key, val)