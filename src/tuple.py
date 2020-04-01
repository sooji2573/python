
my_tuple = ()

print(type(my_tuple))

my_tuple = 1, 2, 3 # packing

num1, num2, num3 = my_tuple # unpacking

print(num1)
print(num2)
print(num3)

# num2 = 1, num1 = 2 로 하고 싶으면
num1, num2 = num2, num1

print(num1)
print(num2)
print(num3)
