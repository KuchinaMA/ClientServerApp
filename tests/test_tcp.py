import socket
import struct
from test_utils import run_server, stop_server

TCP_PORT = 12345

#==============================================================

def tcp_send_message(message):
    s = socket.create_connection(('127.0.0.1', TCP_PORT))
    payload = message.encode()
    s.sendall(struct.pack('!I', len(payload)) + payload)
    reply_len_bytes = s.recv(4)
    reply_len = struct.unpack('!I', reply_len_bytes)[0]
    reply = s.recv(reply_len)
    s.close()
    return reply.decode()

def print_result(name, status):
    print(f"[TCP] {name:<25} {'PASSED' if status else 'FAILED'}")

#==============================================================

def test_tcp_small_message():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'tcp', '--role', 'server', '--port', str(TCP_PORT)])
    try:
        reply = tcp_send_message("Hello TCP")
        print_result("small message", "Hello TCP" in reply)
    finally:
        stop_server(server)

def test_tcp_large_message():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'tcp', '--role', 'server', '--port', str(TCP_PORT)])
    try:
        message = "A" * 25000
        reply = tcp_send_message(message)
        print_result("large message", "Got it!" in reply)
    finally:
        stop_server(server)

def test_tcp_multiple_messages():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'tcp', '--role', 'server', '--port', str(TCP_PORT)])
    try:
        messages = ["First", "Second", "Third"]
        success = True
        for msg in messages:
            reply = tcp_send_message(msg)
            if msg not in reply:
                success = False
                break
        print_result("multiple messages", success)
    finally:
        stop_server(server)

def test_tcp_empty_message():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'tcp', '--role', 'server', '--port', str(TCP_PORT)])
    try:
        reply = tcp_send_message("")
        print_result("empty message", "Got it!" in reply)
    finally:
        stop_server(server)

def test_tcp_repeat_messages():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'tcp', '--role', 'server', '--port', str(TCP_PORT)])
    try:
        success = True
        for _ in range(3):
            reply = tcp_send_message("RepeatTCP")
            if "RepeatTCP" not in reply:
                success = False
        print_result("repeat messages", success)
    finally:
        stop_server(server)

def test_tcp_netcat():
    import subprocess
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'tcp', '--role', 'server', '--port', str(TCP_PORT)])
    try:
        cmd = "(printf '\\x00\\x00\\x00\\x04ping'; sleep 1) | nc 127.0.0.1 " + str(TCP_PORT) + " -q 1"
        result = subprocess.run(cmd, shell=True)
        print_result("netcat compatibility", result.returncode == 0)
    finally:
        stop_server(server)

#==============================================================

if __name__ == "__main__":
    test_tcp_small_message()
    test_tcp_large_message()
    test_tcp_multiple_messages()
    test_tcp_empty_message()
    test_tcp_repeat_messages()
    test_tcp_netcat()
