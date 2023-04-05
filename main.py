import credentials


def passInfo(name: str, userName: str, email: str, password: str):
    credentials.setEve(name, userName, email, password)


def passVerify(password1: str, password2: str) -> bool:
    if password1 != password2:
        print('Your passwords do not match.')
        pass2 = input('Please enter you password again: ')
        passVerify(password1, pass2)
    return True


def setCredentials(name: str, userName: str):
    email = input(f'{name}, Please enter your email: ')
    splits = email.split('@')
    if splits[1] == 'gmail.com' or splits[1] == 'yahoo.com' or splits[1] == 'outlook.com':
        print('Valid Email')

        # TODO: If possible I can possibly add email verification system.
        password1 = input('Please enter your password: ')
        password2 = input('Please enter you password again: ')

        if passVerify(password1, password2):
            print(f'\n\t\tWell Done, {name}\nYou have successfully created an account!')

            passInfo(name, userName, email, password1)

    else:
        print('Please enter a valid email.')
        setCredentials(name, userName)


def setUsername(name: str):
    userName = input(f'{name}, Please enter the user name that you wish to set for your account: ')
    setInfo(name, userName)


def setInfo(name: str, userName: str):
    if credentials.userName_check(userName):
        print(f"Please choose a different username, {userName} is taken")
        setUsername(name)
    else:
        if " " in userName:
            print("Your username should not have any spaces.")
            setUsername(name)

    setCredentials(name, userName)


def login():
    user = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    if credentials.check(user, password):
        print(f'\nWelcome, {user}')
    else:
        print('Your password or email is incorrect.')


def main():
    # TODO: At last, add a welcoming message first and then present selection

    selection = input("Do you wish to 'sign up' or 'login'? ")

    if selection == 'Sign up':
        name = input('Please enter your full name: ')
        print(f'Nice to meet you {name}.')

        setUsername(name)

    elif selection == 'Login':
        login()


if __name__ == '__main__':
    main()
