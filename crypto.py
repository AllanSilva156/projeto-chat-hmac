import hmac
import random
import time


def cryptography(message):
    key = 'user_message'
    digest = hmac.digest(key=key.encode(), msg=message.encode(), digest='sha1')
    return digest


def validate_integrity(digest1, digest2):
    if hmac.compare_digest(digest1, digest2):
        return '\033[32mCorrect message!\033[m'
    else:
        return '\033[31mCorrupted message!\033[m'


def validate_authenticity(usr1, usr2):
    if usr1 == usr2:
        return '\033[32mCorrect user!\033[m'
    else:
        return '\033[31mWrong user!\033[m'


def corrupt_msg(message):
    return ''.join(random.sample(message, len(message)))


def man_in_the_middle(data, index):
    data[index] = 'Anonymous'


def data_leakage(usr, msg):
    with open('data_leakage.txt', 'a', encoding='ascii') as file:
        file.write(f'[{time.ctime()}] {usr}: {msg}\n')
