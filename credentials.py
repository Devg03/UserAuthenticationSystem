file = open('database.txt', "a+")


def userName_check(userName: str) -> int:
    content = file.read()

    if userName in content:
        return 1
    else:
        return 0


def createFile(name: str, userName: str, email: str, password: str):
    form = f'{name} = [Name: {name}, userName: {userName}, Email: {email}, Password: {password}] '
    file.write(form + "\n")
    file.close()


def main(name: str, userName: str, email: str, password: str):
    users_info = {'name': name, 'Username': userName, 'email': email, 'password': password}

    createFile(name, userName, email, password)
