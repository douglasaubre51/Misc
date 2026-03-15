num = int(input('enter a num: '))

if num < 2:
    print(f'{num} is not a prime!')
    exit()

for i in range(2, num - 1):
    if num % i == 0:
        print(f'{num} is not a prime!')
        exit()

print(f'{num} is a PRIME!')
