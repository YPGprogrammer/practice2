numb = int(input('Введите количество цифр: '))
numbers = []
counter = 1
while len(numbers) < numb:
    print('Введите', counter, 'элемент:')
    numbers.append(int(input()))
    counter += 1
numbers.sort()
print(numbers)