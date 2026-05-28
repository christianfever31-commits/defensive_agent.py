import time
import os

LOG_FILE = "agent_production.log"

def monitor_logs():
    print(f"--- Monitoring {LOG_FILE} for critical failures ---")
    
    # Check if log file exists, if not create it
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Log initialized.\n")

    # Open the file and seek to the end
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1) # Wait for new entries
                continue
            
            # Check for our "Nightmare" trigger words
            if "CRITICAL" in line.upper() or "ERROR" in line.upper():
                print(f"🚨 ALERT: {line.strip()}")
            else:
                print(f"INFO: {line.strip()}")

if __name__ == "__main__":
    try:
        monitor_logs()
    except KeyboardInterrupt:
        print("\nMonitor stopped.")

