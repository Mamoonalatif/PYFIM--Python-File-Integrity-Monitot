import hashlib
import os
import time

FILES_LIST_PATH = "files_to_monitor.txt"

HASH_DB = {}

def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def get_files_to_monitor():
    try:
        with open(FILES_LIST_PATH, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] File list not found: {FILES_LIST_PATH}")
        return []

def scan_files():
    files = get_files_to_monitor()
    for file in files:
        hash_val = hash_file(file)
        if hash_val is None:
            print(f"[!] File not found: {file}")
            continue
        if file not in HASH_DB:
            HASH_DB[file] = hash_val
            print(f"[+] Monitoring: {file}")
        elif HASH_DB[file] != hash_val:
            print(f"[ALERT] File changed: {file}")
            HASH_DB[file] = hash_val

if __name__ == "__main__":
    print("Starting PyFIM - File Integrity Monitor")
    print(f"Reading files to monitor from: {FILES_LIST_PATH}")
    while True:
        scan_files()
        time.sleep(10) 
