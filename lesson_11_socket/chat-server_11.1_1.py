#Реалізувати чат без графічного інтерфейсу, який дозволить обмінюватися повідомленням між клієнтом та сервером.
#Клієнт повинен отримувати повідомлення
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 61486))
server.listen(1)
print('Server is running')
connection, adress = server.accept()
print("connect:", adress)

while True:
    connection.send(input("input text: ").encode("utf-8"))
    data_server = connection.recv(1024)
    print(data_server.decode("utf-8"))