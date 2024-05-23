import requests

def main():
    with open("urls.txt", "r") as file:
        for link in file.readlines():
            link = link.rstrip("\n")
            response = requests.get(
                url=str(link),
            )
            
            if response.status_code == 200:
                try:
                    print(f"""
                    url: {link}
                    resp: {response.status_code}
                    """)
                except requests.exceptions.RequestException as e:
                    print(f"error: {e}")
            else:
                print(f"error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    main()
    
