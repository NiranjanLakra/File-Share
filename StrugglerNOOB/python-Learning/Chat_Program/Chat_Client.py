import socket

# Define server address and port to connect to
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print("Connected to the server!")

# Chat loop
while True:
    # Send a message to the server
    message = input("You: ")
    client_socket.send(message.encode())

    # Receive a message from the server
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

# Close the connection
client_socket.close()
