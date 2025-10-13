import socket
from protocol import send_msg, recv_msg

def tcp_client(host, port):
    with socket.create_connection((host, port)) as s:
        print(f"[TCP CLIENT] Connected to {host}:{port}")
        print("Type 'exit' to quit")
        while True:
            message = input("You: ")
            if message.lower() == "exit":
                print("[TCP CLIENT] Exiting...")
                break
            send_msg(s, message.encode())
            reply = recv_msg(s)
            if reply is None:
                print("[TCP CLIENT] Server closed connection")
                break
            print(f"Server says: {reply.decode()}")
