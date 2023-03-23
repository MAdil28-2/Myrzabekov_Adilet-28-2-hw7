import random
from decouple import config
def casino():
    money = config('MY_MONEY', cast=int)
    balance = money
    while True:
        slot_won = random.randint(1, 31)
        numb = int(input("введите номер"))
        if numb not in range(1,31):
            print('Такой слот не возможен')
        bet = int(input('Сделайте ставку: '))
        if bet > balance:
            print(f'У вас не так много денег Ваш баланс {balance}')

        if slot_won == numb:
            balance += bet * 2
        else:
            balance -= bet

        continue_or_no = input('Хотите продолжить ? y/n')
        if continue_or_no == 'y':
            print(f'выиграшный слот {slot_won}')
            continue
        elif continue_or_no == 'n':
            print(f'выиграшный слот {slot_won}')
            print(f'Ваш баланс {balance}')
            break


if __name__ == '__main__':
    casino()
