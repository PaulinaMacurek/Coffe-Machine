import sys

class CoffeeMachine:

    machine_supply = {'water': 400, 'milk': 540, 'coffee beans': 120, 'money': 550, 'disposable cups': 9}
    stn_coffe = {'espresso': {'water': 250, 'milk': 0, 'coffee beans': 16, 'money': 4},
                 'latte': {'water': 350, 'milk': 75, 'coffee beans': 20, 'money': 7},
                 'cappuccino': {'water': 200, 'milk': 100, 'coffee beans': 12, 'money': 6}}

    @classmethod
    def remaining(cls):
        print('\nThe coffee machine has:')
        print(cls.machine_supply['water'], 'ml of water')
        print(cls.machine_supply['milk'], 'ml of milk')
        print(cls.machine_supply['coffee beans'], 'g of coffee beans')
        print(cls.machine_supply['disposable cups'], 'disposable cups')
        print('$' + str(cls.machine_supply['money'])+' of money')

    @classmethod
    def fill_action(cls):
        print('Write how many ml of water you want to add:')
        cls.machine_supply['water'] += int(input())
        print('Write how many ml of milk you want to add:')
        cls.machine_supply['milk'] += int(input())
        print('Write how many grams of coffee beans you want to add:')
        cls.machine_supply['coffee beans'] += int(input())
        print('Write how many disposable cups you want to add:')
        cls.machine_supply['disposable cups'] += int(input())
        return cls.machine_supply

    @classmethod
    def take_action(cls):
        print('I gave you $' + str(cls.machine_supply['money']))
        cls.machine_supply['money'] = 0

    @staticmethod
    def user_input():
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        user_decision = input()
        if user_decision == 'back':
            return 4
        else:
            return int(user_decision)

    @classmethod
    def check_is_enough_supply(cls, coffee_name):
        if cls.machine_supply['disposable cups'] == 0:
            print('Sorry, not enough disposable cups!')
            return False
        elif cls.stn_coffe[coffee_name]['water'] > cls.machine_supply['water']:
            print('Sorry, not enough water!')
            return False
        elif cls.stn_coffe[coffee_name]['milk'] > cls.machine_supply['milk']:
            print('Sorry, not enough milk!')
            return False
        elif cls.stn_coffe[coffee_name]['coffee beans'] > cls.machine_supply['coffee beans']:
            print('Sorry, not enough coffee beans!')
            return False
        else:
            return True

    @classmethod
    def make_coffee(cls, coffee_type):
        if coffee_type == 1:
            if not cls.check_is_enough_supply('espresso'):
                return False
            else:
                print('I have enough resources, making you a coffee!')
                cls.machine_supply['water'] -= 250
                cls.machine_supply['coffee beans'] -= 16
                cls.machine_supply['money'] += 4
        elif coffee_type == 2:
            if not cls.check_is_enough_supply('latte'):
                return False
            else:
                print('I have enough resources, making you a coffee!')
                cls.machine_supply['water'] -= 350
                cls.machine_supply['milk'] -= 75
                cls.machine_supply['coffee beans'] -= 20
                cls.machine_supply['money'] += 7
        elif coffee_type == 3:
            if not cls.check_is_enough_supply('cappuccino'):
                return False
            else:
                print('I have enough resources, making you a coffee!')
                cls.machine_supply['water'] -= 200
                cls.machine_supply['milk'] -= 100
                cls.machine_supply['coffee beans'] -= 12
                cls.machine_supply['money'] += 6
        elif coffee_type == 4:
            return False
        cls.machine_supply['disposable cups'] -= 1
        return True

    @classmethod
    def run(cls):
        while True:
            print('\nWrite action (buy, fill, take, remaining, exit): ')
            action = input()
            if action == 'buy':
                cls.make_coffee(cls.user_input())
            elif action == 'fill':
                cls.fill_action()
            elif action == 'take':
                cls.take_action()
            elif action == 'remaining':
                cls.remaining()
            elif action == 'exit':
                sys.exit()



CoffeeMachine.run()