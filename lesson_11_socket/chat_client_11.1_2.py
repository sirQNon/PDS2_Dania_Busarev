#Реалізувати чат без графічного інтерфейсу, який дозволить обмінюватися повідомленням між клієнтом та сервером.
#Клієнт повинен отримувати повідомлення

import socket

abon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
abon.connect(("localhost", 61486))

while True:
    data = abon.recv(1024)
    print(data.decode("utf-8"))
    abon.send(input("adon input text: ").encode("utf-8"))