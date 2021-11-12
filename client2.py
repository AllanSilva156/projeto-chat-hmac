import socket
import threading
from crypto import *

ServerIP = input('Server IP: ')
PORT = int(input('Port: '))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    username = input('Enter a username: ')
    client.connect((ServerIP, PORT))
    print(f'Connected Sucessfully to {ServerIP}:{PORT}')
except (ValueError, Exception):
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')


def receiveMessage():
    while True:
        try:
            message = client.recv(2048).decode('ascii')
            if message == 'getUser':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except (ValueError, Exception):
            print('ERROR: Check your connection or server might be offline')


def sendMessage():
    while True:
        msg = input()
        with open('msgs_crypto.bin', 'wb') as file:
            file.write(cryptography(msg))
        client.send(msg.encode('ascii'))


thread1 = threading.Thread(target=receiveMessage, args=())
thread2 = threading.Thread(target=sendMessage, args=())

thread1.start()
thread2.start()
