#напишіть сервер який би отримував у користувача фразу
#а потім надсилав би підраховану кількість слів у відповідь

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 61487))
server.listen(1)
print('Server is running')
connection, adress = server.accept()
print("connect:", adress)

while True:
    connection.send(" pleasse input text: ".encode("utf-8"))
    data_server = connection.recv(1024)
    data_decode = data_server.decode("utf-8")
    print(data_decode)
    refacotr_str = data_decode.split()
    cycle_words = str(len(refacotr_str))
    connection.send(f" words in a phrase, {cycle_words} words ".encode("utf-8"))