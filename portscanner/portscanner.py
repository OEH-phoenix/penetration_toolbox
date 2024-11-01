import argparse
import nmap

def scan_ports(ip, port_range):
    try:
        nm = nmap.PortScanner()
        nm.scan(ip, port_range)
        for host in nm.all_hosts():
            print(f"Scanning IP: {host}")
            for proto in nm[host].all_protocols():
                print(f"\nProtocol: {proto}")
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    print(f"Port: {port}\tState: {state}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("ip", type=str, help="IP address to scan")
    parser.add_argument("port_range", type=str, help="Port range, e.g., 20-80")
    args = parser.parse_args()

    scan_ports(args.ip, args.port_range)
