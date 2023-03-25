def passVerify(name: str, pass1: str, pass2: str):
    if pass1 == pass2:
        print(f'\n\t\tWell Done, {name}\nYou have successfully created an account!')
    else:
        while pass1 != pass2:
            print('Your passwords do not match.')
            pass2 = input(f'{name}, Please enter you password again: ')
            passVerify(name, pass1, pass2)

    # TODO: Needs to add to the User's object


def signUp():
    name = input('Please enter your full name: ')
    print(f'Nice to meet you {name}.')

    # TODO: Needs to create a hash map or an object that bundles an user information

    userName = input(f'{name}, Please enter the user name that you wish to set for your account: ')

    # TODO: Username should not have spaces
    # TODO: Needs to check if this username is taken or not through iterating the credentials file

    email = input(f'{name}, Please enter your email: ')

    # TODO: Needs to add it to the User's object
    # TODO: If possible I can possibly add email verification system.

    password1 = input('Please enter your password: ')
    password2 = input('Please enter you password again: ')

    passVerify(name, password1, password2)


def login():
    userOrEmail = input("Please enter your user name or email: ")
    # TODO: Must setup the User's object first in order to verify if the username or email even exists

    password = input("Please enter your password: ")
    # TODO: Must check if the User's password matches the corresponding email or username


def page():
    # TODO: At last, add a welcoming message first and then present selection

    selection = input("Do you wish to 'sign up' or 'login'? ")

    if selection == 'Sign up':
        signUp()
    elif selection == 'Login':
        login()
    else:
        print('Enter a valid response.')


page()
