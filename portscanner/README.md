Port Scanner

Description
This tool uses nmap to scan an IP address and check if certain ports are open.

Installation
This tool requires the nmap package. Install it by running:
pip install python-nmap

Or, install it by navigating to the tool's directory and running:
pip install .

Usage
To use the port scanner, specify the IP address and port range as follows:
python portscanner.py 192.168.1.1 20-80
This command will scan ports 20 to 80 on the specified IP address.
