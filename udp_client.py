import socket

def udp_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"[UDP CLIENT] Ready to send to {host}:{port}")
        print("Type 'exit' to quit")
        while True:
            message = input("You: ")
            if message.lower() == "exit":
                print("[UDP CLIENT] Exiting...")
                break
            s.sendto(message.encode(), (host, port))
            data, _ = s.recvfrom(65535)
            print(f"Server says: {data.decode()}")
