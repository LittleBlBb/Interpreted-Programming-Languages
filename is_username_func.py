import re

def is_username(username):
    if '@' in username:
        return False
    match = re.match(r'^[а-яА-ЯёЁa-zA-Z][a-zA-ZёЁа-яА-Я0-9_]{2,19}', username)
    return match is not None

def is_username_with_exceptions(username):
    if '@' in username:
        raise ValueError ("Передано некорректное значение (это не имя пользователя)")

    match = re.match(r'^[а-яА-ЯёЁa-zA-Z][a-zA-ZёЁа-яА-Я0-9_]{2,19}', username)
    if match is None:
        raise ValueError ("Передано некорректное значение (это не имя пользователя)")
    return match is not None

usernames = ["Kertis", "kertis@gmail.com", "123", "_username"]
print("Введите 1 чтобы решить задачу функцией без обработки ошибок")
print("Введите 2 чтобы решить задачу функцией c обработкой ошибок")
choice = int(input())

if choice == 1:
    for username in usernames:
        print (f"username: {username} \n" +
               f"Result: {is_username(username)}")
if choice == 2:
    for username in usernames:
        print (f"username: {username} \n" +
               f"Result: {is_username_with_exceptions(username)}")
else:
    exit()