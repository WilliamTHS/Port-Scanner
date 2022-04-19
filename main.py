import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()

print_lock = threading.Lock()

ip = input("[?] Input IP Address > ")
print("")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " is Opened ✅")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=900) as executor:
    for port in range(999999):
        executor.submit(scan, ip, port + 1)