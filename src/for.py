for n in range(5):
    print(n)


# 구구단
for j in range(2, 10):
    for i in range(1, 10):
        print('{}X{}={}'.format(j, i, j*i))

# comprehension, 간결하게 만드는 방법
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

print(odd_numbers)
odd_numbers = [number for number in numbers if number % 2 == 1]