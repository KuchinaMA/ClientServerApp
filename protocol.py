import struct

def send_msg(sock, data: bytes):
    length = struct.pack("!I", len(data))
    sock.sendall(length + data)

def recv_msg(sock):
    hdr = recv_exact(sock, 4)
    if not hdr:
        return None
    length = struct.unpack("!I", hdr)[0]
    return recv_exact(sock, length)

def recv_exact(sock, n):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            return None
        data += chunk
    return data
