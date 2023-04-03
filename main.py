import credentials


def passInfo(name: str, userName: str, email: str, password: str):
    credentials.setEve(name, userName, email, password)


def passVerify(password1: str, password2: str) -> bool:
    if password1 != password2:
        print('Your passwords do not match.')
        pass2 = input('Please enter you password again: ')
        passVerify(password1, pass2)
    return True


def setInfo(name: str):
    userName = input(f'{name}, Please enter the user name that you wish to set for your account: ')
    # Checks if the username is taken or not based on 0 or anything else (Which is 1).
    if not credentials.userName_check(userName):
        if " " in userName:
            print("Your username should not have any spaces.")
            setInfo(name)
        else:
            email = input(f'{name}, Please enter your email: ')

            # TODO: If possible I can possibly add email verification system.
            password1 = input('Please enter your password: ')
            password2 = input('Please enter you password again: ')

            if passVerify(password1, password2):
                print(f'\n\t\tWell Done, {name}\nYou have successfully created an account!')

                passInfo(name, userName, email, password1)
    else:
        print(f"Please choose a different username, {userName} is taken")


def login():
    user = input("Please enter your user name: ")
    if credentials.userName_check(user):
        password = input("Please enter your password: ")
    # TODO: Must check if the User's password matches the corresponding email or username

    else:
        print('Enter a valid response.')


def main():
    # TODO: At last, add a welcoming message first and then present selection

    selection = input("Do you wish to 'sign up' or 'login'? ")

    if selection == 'Sign up':
        name = input('Please enter your full name: ')
        print(f'Nice to meet you {name}.')

        setInfo(name)

    elif selection == 'Login':
        login()


if __name__ == '__main__':
    main()
