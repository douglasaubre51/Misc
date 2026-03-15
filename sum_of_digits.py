num = int(input('enter a num: '))

temp = 0

while num != 0:
    temp += num % 10
    num = int(num / 10)

print(f'sum of digits: {temp}')
