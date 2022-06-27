"""
  User interface module
"""
from functions import init_apartments, \
                      split_command_params, get_a_params, get_b_params, get_c_params, \
                      add_apartment, modify_apartments, list_apartments, \
                      undo, add_undo, \
                      get_d_params_sort, get_d_params_sum, get_d_params_max, \
                      sum_of_a_type, max_utility, sort_apartments_or_types, \
                      get_e_params, filter_apartments, \
                      format_display_apartments


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

    print('\t (D) Obtain different characteristics of the expenses:')
    print('\t\t sum <type>')
    print('\t\t max <apartment>')
    print('\t\t sort apartment')
    print('\t\t sort type')

    print('\t (E) Filter:')
    print('\t\t filter <type>')
    print('\t\t filter <value>')

    print('\t (F) Filter:')
    print('\t\t undo')

    print('\t (G) Exit the menu:')
    print('\t\t exit')


def start_command_ui():

    apartments = {}
    init_apartments(apartments, 10)
    undo_apartments = []

    while True:
        print_menu()
        user_cmd = input("Write a command: ")
        try:
            cmd_word, cmd_params = split_command_params(user_cmd)

            if cmd_word == 'exit':
                return

            elif cmd_word == 'add':
                add_undo(apartments, undo_apartments)
                apartments = add_apartment(apartments, get_a_params(len(apartments), cmd_params))

            elif cmd_word == 'remove' or cmd_word == 'replace':
                add_undo(apartments, undo_apartments)
                apartments = modify_apartments(apartments, get_b_params(len(apartments), cmd_params))

            elif cmd_word == 'list':
                answer_apartments = list_apartments(apartments, get_c_params(len(apartments), cmd_params))
                print(format_display_apartments(answer_apartments))

            elif cmd_word == 'sum':
                print(sum_of_a_type(apartments, get_d_params_sum(cmd_params)))

            elif cmd_word == 'max':
                answer = max_utility(apartments, get_d_params_max(len(apartments), cmd_params))
                print("The utility with the highest cost for apartment " +
                      str(get_d_params_max(len(apartments), cmd_params)) +
                      " is " + answer[0] + ", costing " + str(answer[1]) + " RON.")

            elif cmd_word == 'sort':
                print(sort_apartments_or_types(apartments, get_d_params_sort(cmd_params)))

            elif cmd_word == 'filter':
                add_undo(apartments, undo_apartments)
                apartments = filter_apartments(apartments, get_e_params(cmd_params))

            elif cmd_word == 'undo':
                if cmd_params is not None:
                    raise ValueError('Invalid command!')
                else:
                    apartments = undo(apartments, undo_apartments)

            else:
                print('Invalid command!')
        except ValueError as ve:
            print(ve)
