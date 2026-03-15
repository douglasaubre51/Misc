num = int(input('enter a num: '))

hold = num
temp = 0
reverse = 0

while num != 0:
    temp = num % 10
    reverse = (reverse * 10) + temp
    num = int(num / 10)

    print(f'temp: {temp}')
    print(f'reverse: {reverse}')

if reverse == hold:
    print(f'{reverse} is a Pallindrome of {hold}')
else:
    print(f'{reverse} is not a Pallindrome of {hold}')

