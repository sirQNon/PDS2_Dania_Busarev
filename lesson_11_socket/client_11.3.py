#напишіть сервер який би отримував у користувача фразу
#а потім надсилав би підраховану кількість слів у відповідь

import socket

abon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
abon.connect(("localhost", 61487))

while True:
    data = abon.recv(1024)
    print(data.decode("utf-8"))
    abon.send(input(" input text: ").encode("utf-8"))