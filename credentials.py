file = open('database.txt', "a+")


def userName_check(userName: str) -> bool:
    with open("database.txt") as dataB:
        for item in dataB:
            if item.__contains__(userName):
                return True
            else:
                return False


def createFile(name: str, userName: str, email: str, password: str):
    form = f'{userName} = [Name: {name}, userName: {userName}, Email: {email}, Password: {password}] '
    file.write(form + "\n")
    file.close()


def setEve(name: str, userName: str, email: str, password: str):
    users_info = {'name': name, 'Username': userName, 'email': email, 'password': password}

    createFile(users_info['name'], users_info['Username'], users_info['email'], users_info['password'])
