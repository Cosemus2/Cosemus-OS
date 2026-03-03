#-----------------------IMPORTS-----------------------
from html import parser
import networkscan
import os
import socket
import threading
import ipaddress
import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

#-----------------------GET LOCAL IP VIA CONNECTION-----------------------
def get_local_ip_via_connection():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting IP via connection: {e}")
        return None
local = get_local_ip_via_connection()
local = '.'.join(local.split('.')[:-1])  # Keep only the first octet for /24 network
local += '.0'
devices = []

#-----------------------CHECK IF A PORT IS OPEN-----------------------
def check_single_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            status = "open"
    except (socket.timeout, ConnectionRefusedError, OSError):
        status = "closed"
   
    return {f"{ip}:{port}": status}

#-----------------------GO THROUGH EACH IP, CHECK EACH PORT FOR IP-----------------------
def main():
    ports = [21, 22, 23, 80, 88, 139, 443, 445, 554, 1433, 2049, 3306, 3389, 6379]
    ip_list = devices if devices else [str(ip) for ip in ipaddress.IPv4Network(args.ip, strict=False)]
    final_results = {}


    tasks = [(ip, port) for ip in ip_list for port in ports]
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(check_single_port, ip, port) for ip, port in tasks]
       
        for future in tqdm(as_completed(futures), total=len(tasks), desc="Scanning Ports", unit="port"):
            final_results.update(future.result())
    # Output results + Sorting (Fixed)
    with open('netscan_results.txt', 'w') as file:
        def sort_key(item):
            ip_port = item[0]
            ip, port = ip_port.split(":")
            ip_parts = list(map(int, ip.split(".")))
            return (*ip_parts, int(port))
        final_results = dict(sorted(final_results.items(), key=sort_key))
        json.dump(final_results, file, indent=4)
    print(f"\nResults saved to netscan_results.txt")

if __name__ == "__main__":
    my_network = f"{str(local)}/24"
    my_scan = networkscan.Networkscan(my_network)
    my_scan.run()
    for i in my_scan.list_of_hosts_found:
        devices.append(i)
    main()
