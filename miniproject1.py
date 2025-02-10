import random

while True:
    choice = input('roll the dice(y/n):').lower()
    if choice == 'y':
        diel1 = random.randint(1,6)
        diel2 = random.randint(1,6)
        print(f'({diel1}, {diel2})')
    elif choice == 'n':
        print('Thankyou for playing!')
        break
    else:
        print('Invalid choice!')


