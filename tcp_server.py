import socket
from protocol import send_msg, recv_msg

def tcp_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"[TCP SERVER] Listening on {host}:{port}...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[TCP SERVER] Connected by {addr}")
                while True:
                    data = recv_msg(conn)
                    if data is None:
                        print("[TCP SERVER] Client disconnected")
                        break
                    text = data.decode()
                    print(f"[CLIENT]: {text}")
                    response = f"Got it! I also {text}".encode()
                    send_msg(conn, response)
