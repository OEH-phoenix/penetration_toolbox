Brute Force HTTP Login

Description
This tool attempts multiple passwords to try logging in to a web server.

Installation
This tool requires the requests package. Install it by running:
pip install requests

Or, install it by navigating to the tool's directory and running:
pip install .

Usage
To use the brute force tool, specify the URL, username, and password file as follows:
python brute_force.py http://example.com/login admin passwords.txt
This command will attempt to log in using each password in passwords.txt.
