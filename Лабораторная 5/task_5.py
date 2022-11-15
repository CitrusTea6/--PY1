import random
import string


def get_random_password(n=8) -> str:
    list_digits = string.ascii_uppercase + string.ascii_lowercase + string.digits
    list_password = random.sample(list_digits, n)
    password = "".join(list_password)
    return password


print(get_random_password())