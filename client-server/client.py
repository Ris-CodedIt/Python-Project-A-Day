import socket


HOST = "localhost" # this is the host address of the server
PORT = 9090  #the port spercified on the server
ADDR = (HOST,PORT)
FORMAT = "utf-8"



client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR) #establishing a connection with the server

def send_message(msg):
    client.send(msg.encode(FORMAT)) #sending message to the server
    print(client.recv(1024).decode(FORMAT))  #recieving  message to the server


send_message("hey there")
input()
send_message("How are you")
input()
send_message("Thank You")
input()
send_message("close connection")



