import os
import socket
import threading
from crypto import *

HOST = input("Host: ")
PORT = int(input("Port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f'Server is Up and Listening on {HOST}:{PORT}')

clients = []
usernames = []


def globalMessage(message):
    for client in clients:
        client.send(message)


def handleMessages(client):
    while True:
        try:
            random_num = random.uniform(0, 10)  # Controla as chances de ocorrência de situações críticas
            receive_message_from_client = client.recv(2048).decode('ascii')
            file = open('msgs_crypto.bin', 'rb')
            digest = file.readline()
            file.close()
            correct_user = usernames[clients.index(client)]

            if random_num > 8:  # 20% de chance ocorrer (mensagem corrompida e usuário correto)
                receive_message_from_client = corrupt_msg(receive_message_from_client)
                print(f'\n{usernames[clients.index(client)]}: {receive_message_from_client}')
                print(validate_authenticity(correct_user, usernames[clients.index(client)]))
                print(validate_integrity(digest, cryptography(receive_message_from_client)))

            elif random_num < 1.5:  # 15% de chance ocorrer (mensagem corrompida, usuário errado e vazamento de dados)
                data_leakage(usernames[clients.index(client)], receive_message_from_client)
                man_in_the_middle(usernames, clients.index(client))
                receive_message_from_client = corrupt_msg(receive_message_from_client)
                print(f'\n{usernames[clients.index(client)]}: {receive_message_from_client}')
                print(validate_authenticity(correct_user, usernames[clients.index(client)]))
                print(validate_integrity(digest, cryptography(receive_message_from_client)))
                print(emoji.emojize('\033[33m:warning:WARNING! Data leakage detected\033[m', use_aliases=True))
                client_leaved = clients.index(client)
                client.close()
                clients.remove(clients[client_leaved])
                client_leaved_username = usernames[client_leaved]
                usernames.remove(client_leaved_username)
                break

            else:
                print(f'\n{usernames[clients.index(client)]}: {receive_message_from_client}')
                print(validate_authenticity(correct_user, usernames[clients.index(client)]))
                print(validate_integrity(digest, cryptography(receive_message_from_client)))

            globalMessage(f'{usernames[clients.index(client)]}: {receive_message_from_client}'.encode('ascii'))
        except (ValueError, Exception):
            client_leaved = clients.index(client)
            client.close()
            clients.remove(clients[client_leaved])
            client_leaved_username = usernames[client_leaved]
            print(f'{client_leaved_username} has left the chat...')
            globalMessage(f'{client_leaved_username} has left us...'.encode('ascii'))
            usernames.remove(client_leaved_username)
            break

    os.remove('msgs_crypto.bin')


def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"New Connection: {str(address)}")
            clients.append(client)
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            usernames.append(username)
            globalMessage(f'{username} just joined the chat!'.encode('ascii'))
            user_thread = threading.Thread(target=handleMessages, args=(client,))
            user_thread.start()
        except(ValueError, Exception):
            pass


initialConnection()
