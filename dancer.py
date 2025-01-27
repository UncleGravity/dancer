import time
import random
import sys
import subprocess
from datetime import datetime, time as dt_time

def is_work_hours():
    current_time = datetime.now().time()
    start_time = dt_time(9, 0)  # 9:00 AM
    end_time = dt_time(18, 00)  # 6:00 PM
    return start_time <= current_time <= end_time

def run_wlrctl_command(command):
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running wlrctl command: {e}")
        return False

def switch_tabs():
    try:
        while True:
            if is_work_hours():
                # Focus Chromium and send Ctrl+Tab
                run_wlrctl_command(['wlrctl', 'window', 'focus', 'chromium'])
                run_wlrctl_command(['wlrctl', 'keyboard', 'type', '\t', 'modifiers', 'CTRL'])
                print(f"Ctrl+Tab sent in Chromium at {datetime.now().strftime('%I:%M:%S %p')}")
            else:
                current_time = datetime.now().strftime('%I:%M:%S %p')
                print(f"Outside operating hours ({current_time}). Waiting...")
            
            # Wait for 30 seconds before the next check
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\nScript terminated by user")
        sys.exit()

if __name__ == "__main__":
    print("Tab switcher started. Press Ctrl+C to exit.")
    print("Operating hours: 9:00 AM to 6:00 PM")
    print("Will switch tabs every 30 seconds during operating hours")
    switch_tabs()
