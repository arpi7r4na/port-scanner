import socket
import time
from datetime import datetime

def scan_port(ip,port):
    try: 
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result=sock.connect_ex((ip,port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    
    except KeyboardInterrupt:
        print("\n[-] Scan stopped by user")
        exit()
    except socket.gaierror:
        print("[-] Hostname Could not be resolved")
        exit()
    except socket.error:
        print("[-] Could not connect to the server")
        exit()

def scan_target(ip,start_port,end_port):
    print("-" * 50)
    print(f"Scanning Target: {ip}")
    print(f"Time Started: {str(datetime.now())}")
    print("-"*50)

    for port in range(start_port,end_port+1):
        scan_port(ip,port)

def main():
    
    target_ip = input("[*] Enter target IP to scan: ")
    start_port = int(input("[*] Enter starting port number: "))
    end_port = int(input("[*] Enter ending port number: "))
    
    print("\n[*] Scanning started...")
    start_time = time.time()
    
    scan_target(target_ip, start_port, end_port)
    
    end_time = time.time()
    print(f"\n[*] Scanning completed in {round(end_time - start_time, 2)} seconds")

if __name__ == "__main__":
    main()
    

