import random
import string
def get_random_password() -> str:
    Letter = string.ascii_uppercase
    letter = string.ascii_lowercase
    numbers = string.digits
    list_simbols =  Letter + letter + numbers
    password = random.sample(list_simbols, 8)
    return''.join(password)
print(get_random_password())

...  # TODO написать функцию генерации случайных паролей


#print(get_random_password())










