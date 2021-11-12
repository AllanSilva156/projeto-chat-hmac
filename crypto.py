import hmac
import random
import emoji
import time


def cryptography(message):
    key = 'user_message'
    digest = hmac.digest(key=key.encode(), msg=message.encode(), digest='sha1')
    return digest


def validate_integrity(digest1, digest2):
    if hmac.compare_digest(digest1, digest2):
        return emoji.emojize('\033[32m:heavy_check_mark:Correct message!\033[m', use_aliases=True)
    else:
        return emoji.emojize('\033[31m:x: Corrupted message!\033[m', use_aliases=True)


def validate_authenticity(usr1, usr2):
    if usr1 == usr2:
        return emoji.emojize('\033[32m:heavy_check_mark:Correct user!\033[m', use_aliases=True)
    else:
        return emoji.emojize('\033[31m:x: Wrong user!\033[m', use_aliases=True)


def corrupt_msg(message):
    return ''.join(random.sample(message, len(message)))


def man_in_the_middle(data, index):
    data[index] = 'Anonymous'


def data_leakage(usr, msg):
    with open('data_leakage.txt', 'a', encoding='ascii') as file:
        file.write(f'[{time.ctime()}] {usr}: {msg}\n')
