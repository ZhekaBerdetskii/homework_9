dictionary = {}


def input_error(func_to_check):
    def inner(*args, **kwargs):
        try:
            if func_to_check(*args, **kwargs) is None:
                return 'Unknown command'
            else:
                return func_to_check(*args, **kwargs)
        except IndexError:
            return 'Enter name and phone'
        except ValueError:
            return 'Please enter correct phone'
        except KeyError:
            return 'Please enter correct name'
    return inner


@input_error
def parser(data):
    user_input = data.split()
    for key, value in commands.items():
        for item in value:
            if item.startswith(user_input[0].lower()):
                return key(user_input[1:])


def hello_handler(data):
    return 'How can i help you?'


@input_error
def add_handler(data):
    dictionary[data[0].title()] = int(data[1])
    return f'{data[0].title()} {data[1]} was saved'


@input_error
def change_handler(data):
    dictionary[data[0].title()] = int(data[1])
    return f'Phone for {data[0].title()} was changed'


@input_error
def phone_handler(data):
    return dictionary[(data[0].title())]


def show_all_handler(data):
    return dictionary


def exit_handler(data):
    return 'Good bye!'


commands = {
    hello_handler: ['hello'],
    add_handler: ['add'],
    change_handler: ['change'],
    phone_handler: ['phone'],
    show_all_handler: ['show all'],
    exit_handler: ['exit', 'close', 'good bye']
}


def main():
    while True:
        user_input = input('>>>')
        if parser(user_input) == 'Good bye!':
            print(parser(user_input))
            break
        if isinstance(parser(user_input), dict):
            print('|{:^20}|{:^20}|'.format('name', 'phone'))
            print(f'|{"-"*20}|{"-"*20}|')
            for key, value in dictionary.items():
                print('|{:^20}|{:^20}|'.format(key, value))
        else:
            print(parser(user_input))


if __name__ == '__main__':
    main()




