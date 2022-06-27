from random import randrange

"""
  Write non-UI functions below
"""


######################################
#       Setters & Getters            #
######################################
def get_utility_amount(apartments, apartment, utility_type):
    return apartments[apartment][utility_type]


def test_get_utility_amount():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    assert get_utility_amount(apartments, 1, 'water') == 32
    assert get_utility_amount(apartments, 2, 'other') == 540
    assert get_utility_amount(apartments, 1, 'gas') == 0


test_get_utility_amount()


def set_utility_amount(apartments, apartment_id, utility_type, amount):
    apartments[apartment_id][utility_type] = amount


def test_set_utility_amount():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    set_utility_amount(apartments, 1, 'water', 100)
    assert get_utility_amount(apartments, 1, 'water') == 100

    set_utility_amount(apartments, 2, 'gas', 50)
    assert get_utility_amount(apartments, 2, 'gas') == 50


test_set_utility_amount()


######################################
#    Format input for A command      #
######################################
def get_a_params(number_of_apartments, cmd_params):
    """
    Check the parameters of a type A command
    :param number_of_apartments: The number of apartments in the building
    :param cmd_params: Command parameters input by the user
    :return: A tuple of (<apartment>, <type>, <amount>)
    """

    if cmd_params is None:
        raise ValueError('Invalid command!')

    tokens = cmd_params.split()
    for i in range(0, len(tokens)):
        tokens[i].strip()

    if len(tokens) != 3:
        raise ValueError('Invalid command!')

    # Check the number of the apartment
    try:
        apartment = int(tokens[0])
        if apartment <= 0:
            raise IndexError('Invalid apartment number!')
        elif apartment > number_of_apartments:
            raise IndexError('Invalid apartment number!')
    except ValueError:
        raise ValueError('Invalid apartment number!')

    # Check the type
    if tokens[1] not in ['water', 'heating', 'electricity', 'gas', 'other']:
        raise ValueError('Invalid utility type!')
    else:
        utility_type = tokens[1]

    # Check the amount:
    try:
        amount = int(tokens[2])
        if amount <= 0:
            raise IndexError('Invalid amount value!')
    except ValueError:
        raise ValueError('Invalid amount value!')

    return apartment, utility_type, amount


def test_get_a_params():
    assert get_a_params(25, '5 gas 100') == (5, 'gas', 100)
    assert get_a_params(25, '6 water 120') == (6, 'water', 120)
    assert get_a_params(25, '10 electricity 232') == (10, 'electricity', 232)
    assert get_a_params(25, '9 other 30') == (9, 'other', 30)
    assert get_a_params(25, '14 heating 200') == (14, 'heating', 200)


test_get_a_params()


######################################
#       Operation A (adding)         #
######################################
def add_apartment(apartments, a_params):
    """
    Add new transaction to an apartment
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param a_params: A tuple of (<apartment>, <utility_type>, <amount>)
    :return: The updated dictionary
    """
    apartment = a_params[0]
    utility_type = a_params[1]
    amount = a_params[2]

    # Get the current amount of "utility_type" from the apartment "apartment"
    current_amount = get_utility_amount(apartments, apartment, utility_type)

    # Update the new amount
    new_amount = current_amount + amount
    set_utility_amount(apartments, apartment, utility_type, new_amount)

    return apartments


def test_add_apartment():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    assert add_apartment(apartments, get_a_params(2, '1 gas 25')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 25, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    assert add_apartment(apartments, get_a_params(2, '2 other 100')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 25, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 640},
    }


test_add_apartment()


######################################
#    Format input for B command      #
######################################
def get_b_params(number_of_apartments, cmd_params):
    """
    Check the parameters of a type B command
    :param number_of_apartments: The number of apartments in the building
    :param cmd_params: Command parameters input by the user
    :return: A tuple of (1, <apartment>, None, None) - if the command is "remove <apartment>"
             A tuple of (2, <apartment1>, <apartment2>, None) - command "remove <start apartment> to <end apartment>"
             A tuple of (3, <utility_type>, None, None) - if the command is "remove <type>"
             A tuple of (4, <apartment>, <utility_type>, <amount>) - command "replace <apartment> <type> with <amount>"
    """
    if cmd_params is None:
        raise ValueError('Invalid command!')
    else:
        tokens = cmd_params.split()
        for i in range(0, len(tokens)):
            tokens[i].strip()

        if len(tokens) == 1:
            if tokens[0] in ['water', 'heating', 'electricity', 'gas', 'other']:
                return 3, tokens[0], None, None
            else:
                try:
                    apartment = int(tokens[0])
                    if apartment <= 0:
                        raise IndexError('Invalid apartment number!')
                    elif apartment > number_of_apartments:
                        raise IndexError('Invalid apartment number!')
                    return 1, apartment, None, None
                except ValueError:
                    raise ValueError('Invalid input!')

        elif len(tokens) == 3:
            if tokens[1] != 'to':
                raise ValueError('Invalid command!')

            try:
                start_apartment = int(tokens[0])
                if start_apartment <= 0:
                    raise IndexError('Invalid apartment number!')
                elif start_apartment > number_of_apartments:
                    raise IndexError('Invalid apartment number!')
            except ValueError:
                raise ValueError('Invalid apartment number!')

            try:
                end_apartment = int(tokens[2])
                if end_apartment <= 0:
                    raise IndexError('Invalid apartment number!')
                elif end_apartment > number_of_apartments:
                    raise IndexError('Invalid apartment number!')
            except ValueError:
                raise ValueError('Invalid apartment number!')

            return 2, start_apartment, end_apartment, None

        elif len(tokens) == 4:
            if tokens[1] not in ['water', 'heating', 'electricity', 'gas', 'other']:
                raise ValueError('Invalid command!')
            if tokens[2] != 'with':
                raise ValueError('Invalid command!')

            try:
                apartment = int(tokens[0])
                if apartment <= 0:
                    raise IndexError('Invalid apartment number!')
                elif apartment > number_of_apartments:
                    raise IndexError('Invalid apartment number!')
            except ValueError:
                raise ValueError('Invalid apartment number!')

            try:
                amount = int(tokens[3])
                if amount <= 0:
                    raise IndexError('Invalid amount value!')
            except ValueError:
                raise IndexError('Invalid amount value!')

            return 4, apartment, tokens[1], amount

        else:
            raise ValueError('Invalid command!')


def test_get_b_params():
    assert get_b_params(25, '15') == (1, 15, None, None)
    assert get_b_params(25, '5 to 10') == (2, 5, 10, None)
    assert get_b_params(25, 'gas') == (3, 'gas', None, None)
    assert get_b_params(25, '12 gas with 200') == (4, 12, 'gas', 200)


test_get_b_params()


######################################
#      Operation B (modifying)       #
######################################
def modify_apartments(apartments, b_params):
    """
    Modify the apartments based on the type of the command and its parameters
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param b_params: A tuple of (<type_of_command>, <parameter>, <parameter>, <parameter>)
                     The parameters depend on the type of command
    :return: The updated dictionary
    """
    type_of_command = b_params[0]

    if type_of_command == 1:
        apartment = b_params[1]
        for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
            set_utility_amount(apartments, apartment, utility_type, 0)
    elif type_of_command == 2:
        for apartment in range(b_params[1], b_params[2]+1):
            for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
                set_utility_amount(apartments, apartment, utility_type, 0)
    elif type_of_command == 3:
        utility_type = b_params[1]
        for apartment in apartments:
            set_utility_amount(apartments, apartment, utility_type, 0)
    elif type_of_command == 4:
        apartment = b_params[1]
        utility_type = b_params[2]
        new_amount = b_params[3]
        set_utility_amount(apartments, apartment, utility_type, new_amount)

    return apartments


def test_modify_apartments():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    assert modify_apartments(apartments, get_b_params(3, '1 other with 100')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 100},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    assert modify_apartments(apartments, get_b_params(3, 'other')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 0},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 0},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 0},
    }

    assert modify_apartments(apartments, get_b_params(3, '2')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 0},
        2: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 0},
    }

    assert modify_apartments(apartments, get_b_params(3, '2 to 3')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 0},
        2: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0},
        3: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0},
    }


test_modify_apartments()


######################################
#    Format input for C command      #
######################################
def get_c_params(number_of_apartments, cmd_params):
    """
    Check the parameters of a type C command
    :param number_of_apartments: The number of apartments in the building
    :param cmd_params: Command parameters input by the user
    :return: A tuple of (1, None, None) - if the command is only "list" - case in which cmd_params is None
             A tuple of (2, <apartment>, None) - if the command is "list <apartment>"
             A tuple of (3, <operator>, <amount>) - if the command is "list [ < | = | > ] <amount>"
    """
    if cmd_params is None:
        return 1, None, None
    else:
        tokens = cmd_params.split()
        for i in range(0, len(tokens)):
            tokens[i].strip()

        if len(tokens) == 1:
            try:
                apartment = int(tokens[0])
                if apartment <= 0:
                    raise IndexError('Invalid apartment number!')
                elif apartment > number_of_apartments:
                    raise IndexError('Invalid apartment number!')
                return 2, apartment, None
            except ValueError:
                raise ValueError('Invalid input!')

        elif len(tokens) == 2:
            if tokens[0] in ['<', '=', '>']:
                try:
                    amount = int(tokens[1])
                    if amount <= 0:
                        raise IndexError('Invalid amount value!')

                    for sign in ['<', '=', '>']:
                        if tokens[0] == sign:
                            return 3, sign, amount
                except ValueError:
                    raise ValueError('Invalid amount value!')
            else:
                raise ValueError('Invalid sign operator!')
        else:
            raise ValueError('Invalid command!')


def test_get_c_params():
    assert get_c_params(25, None) == (1, None, None)
    assert get_c_params(25, '15') == (2, 15, None)
    assert get_c_params(25, '> 100') == (3, '>', 100)
    assert get_c_params(25, '= 17') == (3, '=', 17)


test_get_c_params()


######################################
#       Operation C (listing)        #
######################################
def get_total_expenses(apartments, apartment):
    """
    Get the total of expenses for a certain apartment
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param apartment: The number of the apartments
    :return: The sum of total expenses
    """
    s = 0
    for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
        s += get_utility_amount(apartments, apartment, utility_type)
    return s


def test_get_total_expenses():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    assert get_total_expenses(apartments, 1) == 92
    assert get_total_expenses(apartments, 2) == 1192


test_get_total_expenses()


def list_apartments(apartments, c_params):
    """
    List the apartments according to the input
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param c_params: A tuple of (<type_of_command>, <apartment> / <sign>, <amount>)
    :return: A formatted answer regarding the command
    """
    type_of_command = c_params[0]
    answer = ''
    number_of_apartments = len(apartments)

    if type_of_command == 1:
        answer += 'The expenses are as follows:\n'

        for i in range(0, number_of_apartments):
            answer += 'For the apartment number ' + str(i+1) + ':\n'
            for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
                answer += utility_type + ':' + str(get_utility_amount(apartments, i+1, utility_type)) + '\n'
            answer += '---------------------------------------\n'

        return answer

    elif type_of_command == 2:
        apartment = c_params[1]
        answer += 'The expenses for apartment ' + str(apartment) + ' are:\n'
        for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
            answer += utility_type + ':' + str(get_utility_amount(apartments, apartment, utility_type)) + '\n'
        answer += '---------------------------------------\n'

    else:
        sign = c_params[1]
        amount = c_params[2]
        answer += 'The apartments that check this condition are:'
        for i in range(0, number_of_apartments):
            s = get_total_expenses(apartments, i+1)

            if sign == '<' and s < amount:
                answer += ' ' + str(i+1)
            elif sign == '=' and s == amount:
                answer += ' ' + str(i + 1)
            elif sign == '>' and s > amount:
                answer += ' ' + str(i + 1)

    return answer


def test_list_apartments():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540},
    }

    result1 = 'The expenses are as follows:\n' \
              'For the apartment number 1:\nwater:32\nheating:10\nelectricity:0\ngas:0\nother:50\n' \
              '---------------------------------------\n' \
              'For the apartment number 2:\nwater:312\nheating:120\nelectricity:220\ngas:0\nother:540\n' \
              '---------------------------------------\n'

    result2 = 'The expenses for apartment 1 are:\n' \
              'water:32\nheating:10\nelectricity:0\ngas:0\nother:50\n' \
              '---------------------------------------\n' \

    result3 = 'The apartments that check this condition are: 1'
    result4 = 'The apartments that check this condition are: 1 2'
    result5 = 'The apartments that check this condition are: 1'

    assert list_apartments(apartments, get_c_params(2, None)) == result1
    assert list_apartments(apartments, get_c_params(2, '1')) == result2
    assert list_apartments(apartments, get_c_params(2, '= 92')) == result3
    assert list_apartments(apartments, get_c_params(2, '> 10')) == result4
    assert list_apartments(apartments, get_c_params(2, '< 100')) == result5


test_list_apartments()


######################################
#    Format the user's input         #
######################################
def split_command_params(user_cmd):
    """
    Split the user's command into the command word and a string of parameters
    :param user_cmd: Command input by the user
    :return: A tuple of (<command word>, <command params>) in lowercase
    """
    user_cmd = user_cmd.strip()
    tokens = user_cmd.split(' ', maxsplit=1)

    cmd_word = tokens[0].lower().strip() if len(tokens) > 0 else None
    cmd_param = tokens[1].lower().strip() if len(tokens) == 2 else None

    return cmd_word, cmd_param


def test_split_command_params():
    assert split_command_params('add 25 gas 100') == ('add', '25 gas 100')
    assert split_command_params('remove 15') == ('remove', '15')
    assert split_command_params('remove 5 to 10') == ('remove', '5 to 10')
    assert split_command_params('remove gas') == ('remove', 'gas')
    assert split_command_params('replace 12 gas with 200') == ('replace', '12 gas with 200')
    assert split_command_params('list') == ('list', None)
    assert split_command_params('list 15') == ('list', '15')
    assert split_command_params('list > 100') == ('list', '> 100')
    assert split_command_params('list = 17') == ('list', '= 17')
    assert split_command_params('exit') == ('exit', None)


test_split_command_params()


######################################
#      General Non-UI command        #
######################################
def init_apartments(apartments, number_of_apartments):
    """
    Initialize the apartments
    :param apartments: The dictionary of apartments
    :param number_of_apartments: The number of apartment
    """
    for i in range(0, number_of_apartments):
        apartments[i+1] = {}
        set_utility_amount(apartments, i+1, 'water', randrange(500))
        set_utility_amount(apartments, i+1, 'heating', randrange(500))
        set_utility_amount(apartments, i+1, 'electricity', randrange(500))
        set_utility_amount(apartments, i+1, 'gas', randrange(500))
        set_utility_amount(apartments, i+1, 'other', randrange(500))


def test_init_apartments():
    apartments = {}
    init_apartments(apartments, 2)

    assert len(apartments) == 2
    assert 3 not in apartments
    assert 2 in apartments
    assert 'water' in apartments[1]
    assert 'other' in apartments[2]
    assert 'something' not in apartments[1]


test_init_apartments()


"""
  Write the command-driven UI below
"""


######################################
#       General UI commands          #
######################################
def print_menu():
    print('\t (A) Add new transaction:')
    print('\t\t add <apartment> <type> <amount>')

    print('\t (B) Modify expenses:')
    print('\t\t remove <apartment>')
    print('\t\t remove <start apartment> to <end apartment>')
    print('\t\t remove <type>')
    print('\t\t replace <apartment> <type> with <amount>')

    print('\t (C) Display expenses having different properties:')
    print('\t\t list')
    print('\t\t list <apartment>')
    print('\t\t list [ < | = | > ] <amount>')

    print('\t (D) Exit the menu:')
    print('\t\t exit')


def start_command_ui():

    apartments = {}
    init_apartments(apartments, 10)

    while True:
        print_menu()
        user_cmd = input("Write a command: ")
        try:
            cmd_word, cmd_params = split_command_params(user_cmd)

            if cmd_word == 'exit':
                return
            elif cmd_word == 'add':
                apartments = add_apartment(apartments, get_a_params(len(apartments), cmd_params))
            elif cmd_word == 'remove' or cmd_word == 'replace':
                apartments = modify_apartments(apartments, get_b_params(len(apartments), cmd_params))
            elif cmd_word == 'list':
                print(list_apartments(apartments, get_c_params(len(apartments), cmd_params)))
            else:
                print('Invalid command!')
        except ValueError as ve:
            print(ve)
        except IndexError as ve:
            print(ve)


start_command_ui()
