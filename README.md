# PyFIM – File Integrity Monitor

PyFIM is a simple Python-based File Integrity Monitoring (FIM) tool that detects unauthorized file modifications using hashing and real-time alerts.

## Features
- Monitors critical files for changes using SHA-256 hashing
- Detects and alerts on unauthorized modifications
- Easy to configure: just list files to monitor in a text file

## Usage

1. **List files to monitor:**
   - Add absolute file paths (one per line) to `files_to_monitor.txt`.

2. **Run the monitor:**
   ```sh
   python pyfim.py
   ```

3. **Test:**
   - Edit any monitored file while PyFIM is running.
    <img width="1917" height="1023" alt="Screenshot 2025-08-21 194020" src="https://github.com/user-attachments/assets/115ceb8d-b422-4a64-b681-9ae3e6d7f16b" />
   <img width="1919" height="1019" alt="Screenshot 2025-08-21 194041" src="https://github.com/user-attachments/assets/f818a1eb-41d1-4c39-a51d-1c9dbe02c7e8" />

   - The script will alert you in the terminal if a file changes.
   - <img width="569" height="96" alt="Screenshot 2025-08-21 194438" src="https://github.com/user-attachments/assets/b7cb5143-7b90-436d-ba33-3abb2b370f59" />


## Example Output
```
Starting PyFIM - File Integrity Monitor
Reading files to monitor from: files_to_monitor.txt
[+] Monitoring: c:\testfile.txt
[ALERT] File changed: c:\testfile.txt
```

## Real-World Use
File Integrity Monitoring is a key component in intrusion detection and is used in SOCs and EDR systems.



**Author:** Your Name
