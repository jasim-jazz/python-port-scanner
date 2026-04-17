import socket
import threading
from queue import Queue
import argparse

parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
parser.add_argument("target", help="Target IP or domain")
parser.add_argument("-p", "--ports", help="Port range (e.g., 1-1000)", default="1-1000")
parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
parser.add_argument("-o", "--output", help="Save output to file")

args = parser.parse_args()

target = args.target
start_port, end_port = map(int, args.ports.split("-"))
num_threads = args.threads

queue = Queue()
open_ports = []

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Proxy"
}


def grab_banner(sock):
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return "No banner"


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            service = common_ports.get(port, "Unknown")

            banner = grab_banner(sock)

            output = f"[+] Port {port} OPEN | Service: {service}\n    Banner: {banner[:100]}"
            print(output)

            open_ports.append(output)

        sock.close()

    except Exception:
        pass


def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()


for port in range(start_port, end_port + 1):
    queue.put(port)

threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

queue.join()

if args.output:
    with open(args.output, "w") as f:
        for line in open_ports:
            f.write(line + "\n")

print("\nScan completed!")