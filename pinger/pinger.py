import argparse
from scapy.all import sr1, IP, ICMP

def ping_host(ip):
    try:
        packet = IP(dst=ip)/ICMP()
        response = sr1(packet, timeout=2, verbose=0)
        if response:
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Ping Tool")
    parser.add_argument("ip", type=str, help="IP address to ping")
    args = parser.parse_args()

    ping_host(args.ip)
