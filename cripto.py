import hmac
import random


def criptografa(autor, mensagem):
    resumo = hmac.digest(key=autor.encode(), msg=mensagem.encode(), digest='sha256')
    return resumo


def valida(resumo1, resumo2):
    if hmac.compare_digest(resumo1, resumo2):
        return 'Mensagem validada!'
    else:
        return 'Mensagem corrompida!'


def hacker(mensagem):
    return ''.join(random.sample(mensagem, len(mensagem)))
