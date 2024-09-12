import socket

# Define server address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for connection...")

# Accept a connection from the client
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Chat loop
while True:
    # Receive message from the client
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")

    # Send a message back to the client
    message = input("You: ")
    conn.send(message.encode())

# Close the connection
conn.close()
