import socket
import subprocess
import time
from test_utils import run_server, stop_server

UDP_PORT = 12346

#==============================================================

def udp_send_message(message, retries=5):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    for i in range(retries):
        s.sendto(message.encode(), ('127.0.0.1', UDP_PORT))
        try:
            reply, _ = s.recvfrom(65535)
            s.close()
            return reply.decode()
        except socket.timeout:
            if i == retries-1:
                s.close()
                raise
            continue

def print_result(name, status):
    print(f"[UDP] {name:<25} {'PASSED' if status else 'FAILED'}", flush=True)

#==============================================================

def test_udp_small_message():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'udp', '--role', 'server', '--port', str(UDP_PORT)])
    try:
        reply = udp_send_message("Hello UDP")
        print_result("small message", "Hello UDP" in reply)
    finally:
        stop_server(server)

def test_udp_multiple_messages():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'udp', '--role', 'server', '--port', str(UDP_PORT)])
    try:
        messages = ["Msg1", "Msg2", "Msg3"]
        success = True
        for msg in messages:
            reply = udp_send_message(msg)
            if msg not in reply:
                success = False
                break
        print_result("multiple messages", success)
    finally:
        stop_server(server)

def test_udp_empty_message():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'udp', '--role', 'server', '--port', str(UDP_PORT)])
    try:
        reply = udp_send_message("")
        print_result("empty message", "Got it!" in reply)
    finally:
        stop_server(server)

def test_udp_repeat_messages():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'udp', '--role', 'server', '--port', str(UDP_PORT)])
    try:
        success = True
        for _ in range(3):
            reply = udp_send_message("Repeat")
            if "Repeat" not in reply:
                success = False
        print_result("repeat messages", success)
    finally:
        stop_server(server)

def test_udp_netcat():
    server = run_server(['python3', '-u', 'main.py', '--protocol', 'udp', '--role', 'server', '--port', str(UDP_PORT)])
    try:
        cmd = f"echo -n 'ping' | nc -u -w2 127.0.0.1 {UDP_PORT}"
        result = subprocess.run(cmd, shell=True, timeout=3, capture_output=True, text=True)
        print_result("netcat compatibility", result.returncode == 0)
    finally:
        stop_server(server)

#==============================================================

if __name__ == "__main__":
    test_udp_small_message()
    test_udp_multiple_messages()
    test_udp_empty_message()
    test_udp_repeat_messages()
    test_udp_netcat()
