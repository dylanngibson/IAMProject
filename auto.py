import socket

target = input("Enter the target IP address (e.g., 127.0.0.1): ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))


for port in range(start_port, end_port + 1):
    # Creates a socket for each port 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)


    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")

    sock.close()
