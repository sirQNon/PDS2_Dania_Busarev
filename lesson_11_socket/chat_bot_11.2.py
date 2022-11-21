# Реалізувати чат без графічного інтерфейсу, який дозволить обмінюватися повідомленням між клієнтом та сервером.
# Клієнт повинен отримувати повідомлення
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 61487))
server.listen(1)
print('Server is running')
connection, adress = server.accept()
print("connect:", adress)

while True:
    connection.send("\n 4 - stop bot"
                    "\n 3 academy site"
                    "\n 2 github"
                    "\n 1 site youtube ".encode("utf-8"))
    data_server = connection.recv(1024)
    data_server_de = data_server
    data_serevr_int = int.from_bytes(data_server_de, "big")
    if data_serevr_int == 1:
        connection.send("https://www.youtube.com/@Zelenskyy_President".encode())
    elif data_serevr_int == 2:
        connection.send("https://github.com/sirQNon".encode())
    elif data_serevr_int == 3:
        connection.send("https://study.ua/".encode())
    elif data_serevr_int == 4:
        connection.send("bot stop".encode())
        connection.close()
    else:
        connection.send("invalid input".encode())
