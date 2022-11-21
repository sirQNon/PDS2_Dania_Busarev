#Реалізувати чат без графічного інтерфейсу, який дозволить обмінюватися повідомленням між клієнтом та сервером.
#Клієнт повинен отримувати повідомлення

import socket

abon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
abon.connect(("localhost", 61487))

while True:
    data = abon.recv(1024)
    print(data.decode())
    input_number = int(input(" input numer: "))
    int_to_bytes = input_number.to_bytes(input_number, "big")
    abon.send(int_to_bytes)