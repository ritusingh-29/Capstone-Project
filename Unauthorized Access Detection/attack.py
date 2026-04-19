import urllib.request
import time
import random

fake_passwords = ["123456", "password", "admin123", "qwerty", "letmein", "root", "toor"]

print(" Initiating Stealth Brute-Force Attack on Port 8000...\n")

print("--- PHASE 1: Manual Guesses ---")
print("Hacker is typing passwords by hand...")
for i in range(1, 3):
    pwd = random.choice(fake_passwords)
    print(f"Attempt {i} [Manual] - Password: [{pwd}] -> FAILED")
    try:
        urllib.request.urlopen(f"http://localhost:8000/login?pwd={pwd}")
    except urllib.error.HTTPError:
        pass
    
    time.sleep(3) 

print("\n--- PHASE 2: Automated Bot Script ---")
print("Hacker got frustrated and launched the brute-force script...")
for i in range(3, 35): 
    pwd = random.choice(fake_passwords)
    print(f"Attempt {i} [Bot] - Password: [{pwd}] -> FAILED")
    try:
        urllib.request.urlopen(f"http://localhost:8000/login?pwd={pwd}")
    except urllib.error.HTTPError:
        pass
    
    time.sleep(0.8) 

print("\n✅ Attack sequence complete! The Grafana dashboard should now be Critical Red!")