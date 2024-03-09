import requests
from termcolor import colored

def main():
    with open("urls.txt", "r") as file:
        for link in file.readlines():
            link = link.rstrip("\n")
            response = requests.get(
                url=str(link),
            )
            
            if response.status_code == 200:
                try:
                    response = response.raw
                    print(colored(f"URL: {link}\n", "blue")+
                          colored(f"Resp: {response}\n", "green"))
                except requests.exceptions.RequestException as e:
                    print(colored(f"Error: {e}", "red"))
            else:
                print(colored(f"Error: {response.status_code}, {response.text}", "red"))

if __name__ == "__main__":
    main()