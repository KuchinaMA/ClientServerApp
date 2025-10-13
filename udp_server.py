import socket

def udp_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', port))
        print(f"[UDP SERVER] Listening on port {port}...")
        while True:
            data, addr = s.recvfrom(65535)
            text = data.decode()
            print(f"[CLIENT {addr}]: {text}")
            response = f"Got it! I also {text}".encode()
            s.sendto(response, addr)
