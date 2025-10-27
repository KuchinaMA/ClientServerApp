import argparse
from tcp_server import tcp_server
from tcp_client import tcp_client
from udp_server import udp_server
from udp_client import udp_client

def main():
    parser = argparse.ArgumentParser(description="TCP/UDP client-server demo")
    parser.add_argument("--protocol", required=True, choices=["tcp", "udp"], help="Protocol type")
    parser.add_argument("--role", required=True, choices=["server", "client"], help="Role (client or server)")
    parser.add_argument("--host", default="localhost", help="Address to connect (client) or bind (server)")
    parser.add_argument("--port", type=int, default=8888, help="Port number (default 8888)")

    args = parser.parse_args()

    if args.protocol == "tcp" and args.role == "server":
        tcp_server(args.host, args.port)
    elif args.protocol == "tcp" and args.role == "client":
        tcp_client(args.host, args.port)
    elif args.protocol == "udp" and args.role == "server":
        udp_server(args.host, args.port)
    elif args.protocol == "udp" and args.role == "client":
        udp_client(args.host, args.port)
    else:
        print("Invalid combination of arguments.")

if __name__ == "__main__":
    main()
