import os
import socket
import datetime
import getpass
import platform
import subprocess
import sys

# -------- Paths --------
fake_file = os.path.join(os.getcwd(), "SalaryReport.pdf")  # PDF name
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
logs_folder = os.path.join(desktop_path, "logs")
os.makedirs(logs_folder, exist_ok=True)
log_file = os.path.join(logs_folder, "access_log.txt")

# ----- System Info -----
username = getpass.getuser()
hostname = socket.gethostname()
date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os_info = f"{platform.system()} {platform.release()}"

# ----- Force Location to Coimbatore -----
city = "Coimbatore"
region = "Tamil Nadu"
country = "India"
public_ip = "127.0.0.1"  # Optional: you can keep actual public IP if needed
location = f"{city}, {region}, {country}"

# ----- Write Log -----
log_entry = f"""
Date/Time   : {date_time}
Accessed By : {username}
Device Name : {hostname}
Public IP   : {public_ip}
Location    : {location}
OS          : {os_info}
----------------------------------------
"""
with open(log_file, "a") as f:
    f.write(log_entry)

print("[+] Access logged at:", log_file)

# ----- Open Fake PDF -----
if os.path.exists(fake_file):
    if sys.platform.startswith("win"):
        os.startfile(fake_file)
    elif sys.platform.startswith("darwin"):
        subprocess.Popen(["open", fake_file])
    else:
        subprocess.Popen(["xdg-open", fake_file])
    print("[+] Fake Salary Report opened.")
else:
    print("[-] SalaryReport.pdf not found — place it in the script folder.")
