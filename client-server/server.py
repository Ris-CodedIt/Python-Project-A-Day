import socket
import threading


HOST = "localhost" # this is the address of the host (the one hosting this server the server)
PORT = 9090 # the port to user for the connection
ADDR = (HOST,PORT)
FORMAT = "utf-8" # the format you want to use when encoding and decording your messages
CLOSE_CONNECTION_MESSAGE = "close connection"



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #initilalizing a socket
server.bind(ADDR) #binding the server to the host


# this function handles every client connection in a seperate thread
def process_connection(conn,addr):
    print(f"coneected to: [{addr}]")
    while True:
        message = conn.recv(1024).decode(FORMAT) #recieving message from the client
        if message == CLOSE_CONNECTION_MESSAGE:
            break
        print(f"[{addr}]: {message}")
        conn.send(f"got your messsage ".encode(FORMAT)) # sending message to the client
    conn.send(f"closing connection ".encode(FORMAT))  
    conn.close() #closing the connection with a client 
    print(f"connection with {addr} closed")



# this is the function to start the server
def start_server():
    server.listen() # listening on the specified port
    print("[LISTENING]....server is now listening")
    while True:
        communication_socket, address = server.accept() #accepting a connecion with a client
        thread = threading.Thread(target=process_connection, args=(communication_socket,address)) #initializing a thread for the accepted client
        thread.start()



print("[START]....server has started")
start_server()

