"""
  Program functionalities module
"""
from random import randrange


######################################
#       Setters & Getters            #
######################################
def get_utility_amount(apartments, apartment_id, utility_type):
    """
    Get the expense of the utility = utility_type from the apartment with the id of apartment_id
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param apartment_id: The id of the apartment
    :param utility_type: The type of the utility we are interested in
    :return: The value of the expense
    """
    return apartments[apartment_id][utility_type]


def test_get_utility_amount():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert get_utility_amount(apartments, 1, 'water') == 32
    assert get_utility_amount(apartments, 2, 'other') == 540
    assert get_utility_amount(apartments, 1, 'gas') == 0


test_get_utility_amount()


def set_utility_amount(apartments, apartment_id, utility_type, amount):
    """
    Set the expense of the utility = utility_type from the apartment with the id of apartment_id
    with a new value = amount
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param apartment_id: The id of the apartment
    :param utility_type: The type of the utility we are interested in
    :param amount: The new value for the expense
    """
    apartments[apartment_id][utility_type] = amount


def test_set_utility_amount():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    set_utility_amount(apartments, 1, 'water', 100)
    assert get_utility_amount(apartments, 1, 'water') == 100

    set_utility_amount(apartments, 2, 'gas', 50)
    assert get_utility_amount(apartments, 2, 'gas') == 50


test_set_utility_amount()


def get_number_of_apartment(apartments, apartment_id):
    """
    Get the actual number of the apartment with the id of apartment_id
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param apartment_id: The id of the apartment
    :return: The actual number of the apartment with the id of apartment_id
    """
    return apartments[apartment_id]['number']


def test_get_number_of_apartment():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }
    assert get_number_of_apartment(apartments, 1) == 1
    assert get_number_of_apartment(apartments, 2) == 2

    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 2},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 1},
    }
    assert get_number_of_apartment(apartments, 1) == 2


test_get_number_of_apartment()


def set_number_of_apartment(apartments, apartment_id, apartment_number):
    """
    Set the actual number of the apartment with the id of apartment_id to apartment_number
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param apartment_id: The id of the apartment
    :param apartment_number: The actual number of the apartment with the id of apartment_id
    """
    apartments[apartment_id]['number'] = apartment_number


def test_set_number_of_apartment():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    set_number_of_apartment(apartments, 1, 2)
    set_number_of_apartment(apartments, 2, 1)
    assert get_number_of_apartment(apartments, 1) == 2
    assert get_number_of_apartment(apartments, 2) == 1

    set_number_of_apartment(apartments, 1, 3)
    assert get_number_of_apartment(apartments, 1) == 3


test_set_number_of_apartment()


def copy_dict(apartments):
    """
    Assign to a new dictionary the same values as for the dictionary apartments,
    without keeping the same reference
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :return: The new dictionary of dictionaries containing all the information of the apartments
    """
    new_apartments = {}
    for apartment_id in apartments:

        new_apartments[apartment_id] = {}

        for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
            amount = get_utility_amount(apartments, apartment_id, utility_type)
            set_utility_amount(new_apartments, apartment_id, utility_type, amount)

        apartment_number = get_number_of_apartment(apartments, apartment_id)
        set_number_of_apartment(new_apartments, apartment_id, apartment_number)

    return new_apartments


def test_copy_dict():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 300, 'number': 3},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert copy_dict(apartments) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 300, 'number': 3},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }


test_copy_dict()


######################################
#      General Non-UI command        #
######################################
def init_apartments(apartments, number_of_apartments):
    """
    Initialize the apartments
    :param apartments: The dictionary of apartments
    :param number_of_apartments: The number of apartments
    """
    for i in range(1, number_of_apartments + 1):
        apartments[i] = {}

        # Set the utilities
        set_utility_amount(apartments, i, 'water', randrange(500))
        set_utility_amount(apartments, i, 'heating', randrange(500))
        set_utility_amount(apartments, i, 'electricity', randrange(500))
        set_utility_amount(apartments, i, 'gas', randrange(500))
        set_utility_amount(apartments, i, 'other', randrange(500))

        # Set the number of the apartment
        set_number_of_apartment(apartments, i, i)


def test_init_apartments():
    apartments = {}
    init_apartments(apartments, 2)

    assert len(apartments) == 2
    assert 3 not in apartments
    assert 2 in apartments
    assert 'water' in apartments[1]
    assert 'other' in apartments[2]
    assert 'something' not in apartments[1]
    assert apartments[1]['number'] == 1
    assert apartments[2]['number'] == 2


test_init_apartments()


def format_display_apartments(answer_apartments):
    """
    Create a formatted answer based on the dictionary given
    :param answer_apartments: The dictionary of dictionaries containing all the information of the apartments
    :return: The formatted answer based on the dictionary given
    """
    answer = "The apartments and their expanses with the property entered are:\n"

    for apartment_id in answer_apartments:
        answer += "Apartment number " + str(get_number_of_apartment(answer_apartments, apartment_id)) + ':\n'
        answer += "------------------------------\n"
        for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
            answer += utility_type + ':' + str(get_utility_amount(answer_apartments, apartment_id, utility_type)) + '\n'
        answer += "------------------------------\n\n"

    return answer


def test_format_display_apartments():
    apartments = {
        1: {'water': 32, 'heating': 1000, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 2},
        2: {'water': 0, 'heating': 120, 'electricity': 0, 'gas': 0, 'other': 540, 'number': 1},
    }
    assert format_display_apartments(apartments) == \
           'The apartments and their expanses with the property entered are:\n' \
           'Apartment number 2:\n------------------------------\n' \
           'water:32\nheating:1000\nelectricity:0\ngas:0\nother:50\n' \
           '------------------------------\n\n' \
           'Apartment number 1:\n------------------------------\n' \
           'water:0\nheating:120\nelectricity:0\ngas:0\nother:540\n' \
           '------------------------------\n\n'


test_format_display_apartments()


######################################
#        Operation F (undo)          #
######################################
def add_undo(apartments, undo_apartments):
    """
    Add the current dictionary state to the list containing all the main dictionary's states after each operation
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param undo_apartments: A list containing all the main dictionary's states after each operation
    """
    new_undo_apartment = copy_dict(apartments)
    undo_apartments.append(new_undo_apartment)


def test_add_undo():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 300, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    undo_apartments = [
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        },
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 100, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        }
    ]

    add_undo(apartments, undo_apartments)

    assert undo_apartments == [
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        },
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 100, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        },
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 300, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        }
    ]


test_add_undo()


def undo(apartments, undo_apartments):
    """
    Undo the last performed operation that changed the current dictionary
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param undo_apartments: A list containing all the main dictionary's states after each operation
    :return: The 'new' undid dictionary
    """
    if len(undo_apartments) == 0:
        return apartments
    else:
        apartments = copy_dict(undo_apartments[-1])
        undo_apartments.pop()
        return apartments


def test_undo():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 300, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    undo_apartments = [
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        },
        {
            1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 100, 'number': 1},
            2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        }
    ]

    apartments = undo(apartments, undo_apartments)
    assert apartments == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 100, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    apartments = undo(apartments, undo_apartments)
    assert apartments == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    apartments = undo(apartments, undo_apartments)
    assert apartments == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }


test_undo()


######################################
#    Format input for A command      #
######################################
def get_a_params(number_of_apartments, cmd_params):
    """
    Get the parameters of a type A command
    :param number_of_apartments: The number of apartments in the building
    :param cmd_params: Command parameters input by the user
    :return: A tuple of (<apartment_id>, <utility_type>, <amount>)
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
        apartment_id = int(tokens[0])
        if apartment_id <= 0:
            raise ValueError('Invalid apartment number!')
        elif apartment_id > number_of_apartments:
            raise ValueError('Invalid apartment number!')
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
            raise ValueError('Invalid amount value!')
    except ValueError:
        raise ValueError('Invalid amount value!')

    return apartment_id, utility_type, amount


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
    Add new transaction to an apartment based on the command input by the user
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param a_params: A tuple of (<apartment_id>, <utility_type>, <amount>)
    :return: The updated dictionary
    """
    apartment_id = a_params[0]
    utility_type = a_params[1]
    amount = a_params[2]

    # Get the current amount of "utility_type" from the apartment with the id of apartment_id
    current_amount = get_utility_amount(apartments, apartment_id, utility_type)

    # Update the new amount
    new_amount = current_amount + amount
    set_utility_amount(apartments, apartment_id, utility_type, new_amount)

    return apartments


def test_add_apartment():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert add_apartment(apartments, get_a_params(2, '1 gas 25')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 25, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert add_apartment(apartments, get_a_params(2, '2 other 100')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 25, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 640, 'number': 2},
    }


test_add_apartment()


######################################
#    Format input for B command      #
######################################
def get_b_params(number_of_apartments, cmd_params):
    """
    Get the parameters of a type B command
    :param number_of_apartments: The number of apartments in the building
    :param cmd_params: Command parameters input by the user
    :return: A tuple of (1, <apartment_id>, None, None) - for command "remove <apartment>"
             A tuple of (2, <apartment1_id>, <apartment2_id>, None) - for "remove <start apartment> to <end apartment>"
             A tuple of (3, <utility_type>, None, None) - for "remove <type>"
             A tuple of (4, <apartment_id>, <utility_type>, <amount>) - for "replace <apartment> <type> with <amount>"
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
                    apartment_id = int(tokens[0])
                    if apartment_id <= 0:
                        raise ValueError('Invalid apartment number!')
                    elif apartment_id > number_of_apartments:
                        raise ValueError('Invalid apartment number!')
                    return 1, apartment_id, None, None
                except ValueError:
                    raise ValueError('Invalid apartment number!')

        elif len(tokens) == 3:
            if tokens[1] != 'to':
                raise ValueError('Invalid command!')

            try:
                start_apartment_id = int(tokens[0])
                if start_apartment_id <= 0:
                    raise ValueError('Invalid apartment number!')
                elif start_apartment_id > number_of_apartments:
                    raise ValueError('Invalid apartment number!')
            except ValueError:
                raise ValueError('Invalid apartment number!')

            try:
                end_apartment_id = int(tokens[2])
                if end_apartment_id <= 0:
                    raise ValueError('Invalid apartment number!')
                elif end_apartment_id > number_of_apartments:
                    raise ValueError('Invalid apartment number!')
            except ValueError:
                raise ValueError('Invalid apartment number!')

            return 2, start_apartment_id, end_apartment_id, None

        elif len(tokens) == 4:
            if tokens[1] not in ['water', 'heating', 'electricity', 'gas', 'other']:
                raise ValueError('Invalid command!')
            if tokens[2] != 'with':
                raise ValueError('Invalid command!')

            try:
                apartment_id = int(tokens[0])
                if apartment_id <= 0:
                    raise ValueError('Invalid apartment number!')
                elif apartment_id > number_of_apartments:
                    raise ValueError('Invalid apartment number!')
            except ValueError:
                raise ValueError('Invalid apartment number!')

            try:
                amount = int(tokens[3])
                if amount <= 0:
                    raise ValueError('Invalid amount value!')
            except ValueError:
                raise ValueError('Invalid amount value!')

            return 4, apartment_id, tokens[1], amount

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
                     The parameters depend on the type of the command explained in the function get_b_params()
    :return: The updated dictionary
    """
    type_of_command = b_params[0]

    if type_of_command == 1:
        apartment_id = b_params[1]
        for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
            set_utility_amount(apartments, apartment_id, utility_type, 0)
    elif type_of_command == 2:
        start_apartment_id = b_params[1]
        end_apartment_id = b_params[2]
        for apartment_id in range(start_apartment_id, end_apartment_id + 1):
            for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
                set_utility_amount(apartments, apartment_id, utility_type, 0)
    elif type_of_command == 3:
        utility_type = b_params[1]
        for apartment_id in apartments:
            set_utility_amount(apartments, apartment_id, utility_type, 0)
    elif type_of_command == 4:
        apartment_id = b_params[1]
        utility_type = b_params[2]
        new_amount = b_params[3]
        set_utility_amount(apartments, apartment_id, utility_type, new_amount)

    return apartments


def test_modify_apartments():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 3},
    }

    assert modify_apartments(apartments, get_b_params(3, '1 other with 100')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 100, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 3},
    }

    assert modify_apartments(apartments, get_b_params(3, 'other')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 0, 'number': 2},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 0, 'number': 3},
    }

    assert modify_apartments(apartments, get_b_params(3, '2')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 1},
        2: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 2},
        3: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 0, 'number': 3},
    }

    assert modify_apartments(apartments, get_b_params(3, '2 to 3')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 1},
        2: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 2},
        3: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 3},
    }


test_modify_apartments()


######################################
#    Format input for C command      #
######################################
def get_c_params(number_of_apartments, cmd_params):
    """
    Get the parameters of a type C command
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
                apartment_id = int(tokens[0])
                if apartment_id <= 0:
                    raise ValueError('Invalid apartment number!')
                elif apartment_id > number_of_apartments:
                    raise ValueError('Invalid apartment number!')
                return 2, apartment_id, None
            except ValueError:
                raise ValueError('Invalid apartment number!')

        elif len(tokens) == 2:
            if tokens[0] in ['<', '=', '>']:
                try:
                    amount = int(tokens[1])
                    if amount <= 0:
                        raise ValueError('Invalid amount value!')

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
def get_total_expenses(apartments, apartment_id):
    """
    Get the total of expenses for the apartment with the id of apartment_id
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param apartment_id: The id of the apartment
    :return: The sum of total expenses for the apartment with the id of apartment_id
    """
    s = 0
    for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
        s += get_utility_amount(apartments, apartment_id, utility_type)
    return s


def test_get_total_expenses():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert get_total_expenses(apartments, 1) == 92
    assert get_total_expenses(apartments, 2) == 1192


test_get_total_expenses()


def list_apartments(apartments, c_params):
    """
    Return the apartments according to the command input by the user
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param c_params: A tuple of (<type_of_command>, <apartment_id> / <sign>, <amount>)
    :return: A dictionary of dictionaries containing only the apartments with the given property
    """
    type_of_command = c_params[0]
    answer_apartments = copy_dict(apartments)
    number_of_apartments = len(apartments)

    if type_of_command == 1:
        return answer_apartments

    elif type_of_command == 2:
        apartment_id = c_params[1]
        for i in range(1, number_of_apartments + 1):
            if i != apartment_id:
                answer_apartments.pop(i)

    else:
        sign = c_params[1]
        amount = c_params[2]
        for i in range(1, number_of_apartments + 1):
            s = get_total_expenses(apartments, i)

            if sign == '<' and s >= amount:
                answer_apartments.pop(i)
            elif sign == '=' and s != amount:
                answer_apartments.pop(i)
            elif sign == '>' and s <= amount:
                answer_apartments.pop(i)

    return answer_apartments


def test_list_apartments():
    apartments = {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert list_apartments(apartments, get_c_params(2, None)) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }
    assert list_apartments(apartments, get_c_params(2, '1')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
    }
    assert list_apartments(apartments, get_c_params(2, '= 92')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
    }
    assert list_apartments(apartments, get_c_params(2, '> 10')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }
    assert list_apartments(apartments, get_c_params(2, '< 100')) == {
        1: {'water': 32, 'heating': 10, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
    }
    assert list_apartments(apartments, get_c_params(2, '> 100')) == {
        2: {'water': 312, 'heating': 120, 'electricity': 220, 'gas': 0, 'other': 540, 'number': 2},
    }


test_list_apartments()


######################################
#    Format input for D command      #
######################################
def get_d_params_sum(cmd_params):
    """
    Get the parameters of the type D command "sum <type>"
    :param cmd_params: Command parameters input by the user
    :return: The utility_type
    """
    if cmd_params is None:
        raise ValueError('Invalid command!')

    tokens = cmd_params.split()
    for i in range(0, len(tokens)):
        tokens[i].strip()

    if len(tokens) != 1:
        raise ValueError('Invalid command!')

    if tokens[0] in ['water', 'heating', 'electricity', 'gas', 'other']:
        return tokens[0]
    else:
        raise ValueError('Invalid command!')


def test_get_d_params_sum():
    assert get_d_params_sum('gas') == 'gas'
    assert get_d_params_sum('water') == 'water'
    assert get_d_params_sum('electricity') == 'electricity'


test_get_d_params_sum()


def get_d_params_max(number_of_apartments, cmd_params):
    """
    Get the parameters of the type D command "max <apartment>"
    :param number_of_apartments: The number of apartments in the building
    :param cmd_params: Command parameters input by the user
    :return: The apartment_id
    """
    if cmd_params is None:
        raise ValueError('Invalid command!')

    tokens = cmd_params.split()
    for i in range(0, len(tokens)):
        tokens[i].strip()

    if len(tokens) != 1:
        raise ValueError('Invalid command!')

    try:
        apartment_id = int(tokens[0])
        if apartment_id <= 0 or apartment_id > number_of_apartments:
            raise ValueError('Invalid apartment number!')
        else:
            return apartment_id
    except ValueError:
        raise ValueError('Invalid apartment number!')


def test_get_d_params_max():
    assert get_d_params_max(25, '25') == 25
    assert get_d_params_max(10, '5') == 5


test_get_d_params_max()


def get_d_params_sort(cmd_params):
    """
    Get the parameters of the type D command "sort apartment" or "sort type"
    :param cmd_params: Command parameters input by the user
    :return: 1 if the command is "sort apartment", 2 if the command is "sort type"
    """
    if cmd_params is None:
        raise ValueError('Invalid command!')

    tokens = cmd_params.split()
    for i in range(0, len(tokens)):
        tokens[i].strip()

    if len(tokens) != 1:
        raise ValueError('Invalid command!')

    if tokens[0] == 'apartment':
        return 1
    elif tokens[0] == 'type':
        return 2
    else:
        raise ValueError('Invalid command!')


def test_get_d_params_sort():
    assert get_d_params_sort('apartment') == 1
    assert get_d_params_sort('type') == 2


test_get_d_params_sort()


######################################
#      Operation D (obtaining)       #
######################################
def sum_of_a_type(apartments, d_params):
    """
    Find the total amount for the expenses having a certain utility type
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param d_params: The utility_type
    :return: The total amount for the expenses having utility_type type
    """
    answer = 0
    utility_type = d_params
    for apartment_id in apartments:
        answer += get_utility_amount(apartments, apartment_id, utility_type)
    return answer


def test_sum_of_a_type():
    apartments = {
        1: {'water': 32, 'heating': 1000, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 0, 'heating': 120, 'electricity': 0, 'gas': 0, 'other': 540, 'number': 2},
        3: {'water': 312, 'heating': 120, 'electricity': 1030, 'gas': 0, 'other': 100, 'number': 3},
    }

    assert sum_of_a_type(apartments, get_d_params_sum('gas')) == 0
    assert sum_of_a_type(apartments, get_d_params_sum('other')) == 690
    assert sum_of_a_type(apartments, get_d_params_sum('water')) == 344


test_sum_of_a_type()


def max_utility(apartments, d_params):
    """
    Find the utility with the maximum expense for a certain apartment
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param d_params: The id of the apartment -> apartment_id
    :return: A tuple consisting of the utility with the maximum expense and its value
             for the apartment with the id of apartment_id
    """
    apartment_id = d_params
    maximum_amount = -1
    utility_type_maximum_amount = ''
    for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
        amount = get_utility_amount(apartments, apartment_id, utility_type)
        if amount > maximum_amount:
            maximum_amount = amount
            utility_type_maximum_amount = utility_type

    return utility_type_maximum_amount, maximum_amount


def test_max_utility():
    apartments = {
        1: {'water': 32, 'heating': 1000, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 0, 'heating': 120, 'electricity': 0, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert max_utility(apartments, get_d_params_max(2, '2')) == ('other', 540)
    assert max_utility(apartments, get_d_params_max(2, '1')) == ('heating', 1000)


test_max_utility()


def sort_apartments_or_types(apartments, d_params):
    """
    Sort the apartments / utilities based on the total amount of the expenses
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param d_params: 1 for apartments, 2 for utilities
    :return: A formatted string with the answer
    """
    if d_params == 1:
        sorted_dictionary = copy_dict(apartments)
        number_of_apartments = len(sorted_dictionary)

        for i in range(1, number_of_apartments + 1):
            for j in range(i + 1, number_of_apartments + 1):
                expenses1 = get_total_expenses(sorted_dictionary, i)
                expenses2 = get_total_expenses(sorted_dictionary, j)

                if expenses1 > expenses2:
                    sorted_dictionary[i], sorted_dictionary[j] = sorted_dictionary[j], sorted_dictionary[i]

        answer = format_display_apartments(sorted_dictionary)
        return answer
    else:
        answer = ''
        utilities = []
        for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
            amount = 0
            for apartment_id in apartments:
                amount += get_utility_amount(apartments, apartment_id, utility_type)
            utilities.append((utility_type, amount))

        number_of_utilities = len(utilities)
        for i in range(0, number_of_utilities):
            for j in range(i + 1, number_of_utilities):
                if utilities[i][1] > utilities[j][1]:
                    utilities[i], utilities[j] = utilities[j], utilities[i]

        for i in range(0, number_of_utilities):
            answer += utilities[i][0] + ": " + str(utilities[i][1]) + '\n'
        return answer


def test_sort_apartments_or_types():
    apartments = {
        1: {'water': 32, 'heating': 1000, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 0, 'heating': 120, 'electricity': 0, 'gas': 0, 'other': 540, 'number': 2},
        3: {'water': 312, 'heating': 120, 'electricity': 1030, 'gas': 0, 'other': 100, 'number': 3},
    }
    assert sort_apartments_or_types(apartments, get_d_params_sort('type')) == \
           'gas: 0\nwater: 344\nother: 690\nelectricity: 1030\nheating: 1240\n'

    assert sort_apartments_or_types(apartments, get_d_params_sort('apartment')) == \
           'The apartments and their expanses with the property entered are:\n' \
           'Apartment number 2:\n------------------------------\n' \
           'water:0\nheating:120\nelectricity:0\ngas:0\nother:540\n' \
           '------------------------------\n\n' \
           'Apartment number 1:\n------------------------------\n' \
           'water:32\nheating:1000\nelectricity:0\ngas:0\nother:50\n' \
           '------------------------------\n\n' \
           'Apartment number 3:\n------------------------------\n' \
           'water:312\nheating:120\nelectricity:1030\ngas:0\nother:100\n' \
           '------------------------------\n\n'


test_sort_apartments_or_types()


######################################
#    Format input for E command      #
######################################
def get_e_params(cmd_params):
    """
    Get the parameters of a type E command
    :param cmd_params: Command parameters input by the user
    :return: A tuple of (1, <utility_type>) - if the command is "filter <type>"
             A tuple of (2, <value>) - if the command is "filter <value>"
    """
    if cmd_params is None:
        raise ValueError('Invalid command!')
    else:
        tokens = cmd_params.split()
        for i in range(0, len(tokens)):
            tokens[i].strip()

        if len(tokens) != 1:
            raise ValueError('Invalid command!')

        if tokens[0] in ['water', 'heating', 'electricity', 'gas', 'other']:
            return 1, tokens[0]
        else:
            try:
                value = int(tokens[0])
                if value <= 0:
                    raise ValueError('Invalid value!')
                return 2, value
            except ValueError:
                raise ValueError('Invalid value!')


def test_get_e_params():
    assert get_e_params('gas') == (1, 'gas')
    assert get_e_params('300') == (2, 300)


test_get_e_params()


######################################
#      Operation E (filtering)       #
######################################
def filter_apartments(apartments, e_params):
    """
    Filter the dictionary based on the command
    :param apartments: The dictionary of dictionaries containing all the information of the apartments
    :param e_params: A tuple of (<type_of_command>, <type> / <value>)
    :return: The new filtered dictionary
    """
    type_of_command = e_params[0]

    if type_of_command == 1:
        utility_type_to_keep = e_params[1]
        for apartment_id in apartments:
            for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
                if utility_type != utility_type_to_keep:
                    set_utility_amount(apartments, apartment_id, utility_type, 0)
    else:
        value = e_params[1]
        for apartment_id in apartments:
            for utility_type in ['water', 'heating', 'electricity', 'gas', 'other']:
                amount = get_utility_amount(apartments, apartment_id, utility_type)
                if amount >= value:
                    set_utility_amount(apartments, apartment_id, utility_type, 0)
    return apartments


def test_filter_apartments():
    apartments = {
        1: {'water': 32, 'heating': 1000, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 0, 'heating': 120, 'electricity': 0, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert filter_apartments(apartments, get_e_params('gas')) == {
        1: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 1},
        2: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 2},
    }

    apartments = {
        1: {'water': 32, 'heating': 1000, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 0, 'heating': 120, 'electricity': 0, 'gas': 0, 'other': 540, 'number': 2},
    }

    assert filter_apartments(apartments, get_e_params('51')) == {
        1: {'water': 32, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 50, 'number': 1},
        2: {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0, 'number': 2},
    }


test_filter_apartments()


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
