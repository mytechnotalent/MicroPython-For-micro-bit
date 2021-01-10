CHOCOLATE_CHOICES = {
    'dark': {
        'ingredients': {
            'sugar': 1,
            'butter': 1,
            'dark chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 2.75,
    },
    'mint': {
        'ingredients': {
            'sugar': 1,
            'butter': 1,
            'mint chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 2.50,
    },
    'caramel': {
        'ingredients': {
            'sugar': 1,
            'caramel': 3,
            'butter': 1,
            'milk chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 3.25,
    },
    'surprise': {
        'ingredients': {
            'sugar': 1,
            'Reese\'s Pieces': 3,
            'butter': 1,
            'milk chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 3.25,
    },
}

raw_materials = {
    'sugar': 5,
    'butter': 5,
    'caramel': 15,
    'dark chocolate': 30,
    'mint chocolate': 30,
    'milk chocolate': 30,
    'light corn syrup': 5,
    'sweetened condensed milk': 5,
    'vanilla extract': 5,
    'Reese\'s Pieces': 15,
}

total_money_collected = 0
SHUTDOWN_PASSWORD = '8675309'


def has_raw_materials(f_raw_materials):
    """Check if there are enough raw materials in the machine

    Args:
        f_raw_materials: dict

    Returns:
        True or False
    """
    need_raw_materials = False
    for f_raw_material in f_raw_materials:
        if f_raw_materials[f_raw_material] > raw_materials[f_raw_material]:
            need_raw_materials = True
            print('Machine Needs Additional: {0}'.format(f_raw_material))
    if need_raw_materials:
        print()
        return False
    else:
        return True


def collect_money(f_max_value):
    """Collect money into the machine

    Args:
        f_max_value: float

    Returns:
        float or False
    """
    try:
        money_collected = int(input('Quarters: ')) * 0.25
        money_collected += int(input('Dimes: ')) * 0.10
        money_collected += int(input('Nickels: ')) * 0.05
        if money_collected <= 0.00:
            print('Insufficient funds...  Dispensing coins inserted.')
        elif money_collected >= f_max_value:
            print('Machine can\'t hold more than ${0:.2f}...  Dispensing coins inserted.'.format(f_max_value))
        else:
            return money_collected
    except ValueError:
        print('Please enter valid currency.')
        return False


def has_enough_money(f_money_collected, f_chocolate_price):
    """Check to see if customer put in enough money into the machine

    Args:
        f_money_collected: float
        f_chocolate_price: float

    Return:
        True or False
    """
    if f_money_collected >= f_chocolate_price:
        excess_money_collected = round(f_money_collected - f_chocolate_price, 2)
        print('Change: ${0:.2f}'.format(excess_money_collected))
        global total_money_collected
        total_money_collected += f_chocolate_price
        return True
    else:
        print('Insufficient funds...  Dispensing coins inserted.')
        return False


def bake_chocolate_bar(f_chocolate_choice, f_raw_materials):
    """Bake chocolate bar from raw materials

    Args:
        f_chocolate_choice: dict
        f_raw_materials: dict
    """
    for f_raw_material in f_raw_materials:
        raw_materials[f_raw_material] -= f_raw_materials[f_raw_material]
    print('A {0} chocolate bar dispensed!\n'.format(f_chocolate_choice))


def stats():
    """Show machine statistics"""
    print('sugar {0} tablespoons remaining'.format(raw_materials['sugar']))
    print('butter {0} teaspoons remaining'.format(raw_materials['butter']))
    print('dark chocolate {0} tablespoons remaining'.format(raw_materials['dark chocolate']))
    print('mint chocolate {0} tablespoons remaining'.format(raw_materials['mint chocolate']))
    print('milk chocolate {0} tablespoons remaining'.format(raw_materials['milk chocolate']))
    print('light corn syrup {0} teaspoons remaining'.format(raw_materials['light corn syrup']))
    print('sweetened condensed milk {0} teaspoons remaining'.format(raw_materials['sweetened condensed milk']))
    print('vanilla extract {0} teaspoons remaining'.format(raw_materials['vanilla extract']))
    print('Reese\'s Pieces {0} tablespoons remaining'.format(raw_materials['Reese\'s Pieces']))
    print('Total Money Collected: ${0:.2f}\n'.format(total_money_collected))


machine_active = True
choices = ['dark', 'caramel', 'mint', 'surprise', 'stats', 'shutdown']

while machine_active:
    valid_choice = False
    choice = input('ORDER [dark - caramel - mint - surprise]: ')
    if choice in choices:
        valid_choice = True
    else:
        print('That is not a valid selection...\n')
    if choice == 'shutdown':
        entered_password = input('ENTER SHUTDOWN PASSWORD: ')
        if entered_password == SHUTDOWN_PASSWORD:
            machine_active = False
        else:
            print('YOU ARE NOT AUTHORIZED TO DISABLE THIS MACHINE!\n')
    elif choice == 'stats':
        stats()
    elif valid_choice:
        selection = CHOCOLATE_CHOICES[choice]
        if has_raw_materials(selection['ingredients']):
            customer_money_collected = collect_money(100.00)
            if customer_money_collected:
                if has_enough_money(customer_money_collected, selection['price']):
                    bake_chocolate_bar(choice, selection['ingredients'])
        else:
            machine_active = False

print('We are going down for maintenance...')