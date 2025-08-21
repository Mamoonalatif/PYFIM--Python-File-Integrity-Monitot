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
   - The script will alert you in the terminal if a file changes.

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
