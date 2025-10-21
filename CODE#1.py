import os
import socket
import datetime
import getpass
import platform
import subprocess
import sys
import json

# try to import requests (optional); if not installed we'll fall back to urllib
try:
    import requests
except Exception:
    requests = None

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

# ----- Get real public IP and geolocation -----
public_ip = "Unavailable"
city = "Unavailable"
region = "Unavailable"
country = "Unavailable"

def lookup_ip_and_location():
    """
    Returns (public_ip, city, region, country).
    Tries ip-api.com first (gives geo fields), then ipinfo.io, then api.ipify.org (IP only).
    Uses requests if installed, otherwise urllib.
    """
    try:
        # try ip-api.com first (includes city/region/country)
        if requests:
            resp = requests.get("http://ip-api.com/json/", timeout=5)
            if resp.ok:
                data = resp.json()
                ip = data.get("query") or data.get("ip") or "Unavailable"
                city = data.get("city") or "Unavailable"
                region = data.get("regionName") or data.get("region") or "Unavailable"
                country = data.get("country") or "Unavailable"
                return ip, city, region, country
        else:
            from urllib.request import urlopen
            with urlopen("http://ip-api.com/json/", timeout=5) as r:
                raw = r.read().decode("utf-8")
                data = json.loads(raw)
                ip = data.get("query") or data.get("ip") or "Unavailable"
                city = data.get("city") or "Unavailable"
                region = data.get("regionName") or data.get("region") or "Unavailable"
                country = data.get("country") or "Unavailable"
                return ip, city, region, country
    except Exception:
        pass

    try:
        # try ipinfo.io
        if requests:
            resp = requests.get("https://ipinfo.io/json", timeout=5)
            if resp.ok:
                data = resp.json()
                ip = data.get("ip") or "Unavailable"
                city = data.get("city") or "Unavailable"
                region = data.get("region") or "Unavailable"
                country = data.get("country") or "Unavailable"
                return ip, city, region, country
        else:
            from urllib.request import urlopen
            with urlopen("https://ipinfo.io/json", timeout=5) as r:
                raw = r.read().decode("utf-8")
                data = json.loads(raw)
                ip = data.get("ip") or "Unavailable"
                city = data.get("city") or "Unavailable"
                region = data.get("region") or "Unavailable"
                country = data.get("country") or "Unavailable"
                return ip, city, region, country
    except Exception:
        pass

    try:
        # last resort: get IP only via ipify
        if requests:
            resp = requests.get("https://api.ipify.org?format=json", timeout=5)
            if resp.ok:
                data = resp.json()
                ip = data.get("ip") or "Unavailable"
                return ip, "Unavailable", "Unavailable", "Unavailable"
        else:
            from urllib.request import urlopen
            with urlopen("https://api.ipify.org?format=json", timeout=5) as r:
                raw = r.read().decode("utf-8")
                data = json.loads(raw)
                ip = data.get("ip") or "Unavailable"
                return ip, "Unavailable", "Unavailable", "Unavailable"
    except Exception:
        pass

    return "Unavailable", "Unavailable", "Unavailable", "Unavailable"

try:
    public_ip, city, region, country = lookup_ip_and_location()
except Exception:
    public_ip, city, region, country = ("Unavailable",) * 4

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

try:
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("[+] Access logged at:", log_file)
except Exception as e:
    print("[-] Failed to write log:", e)

# ----- Open Fake PDF -----
try:
    if os.path.exists(fake_file):
        if sys.platform.startswith("win"):
            os.startfile(fake_file)
        elif sys.platform.startswith("darwin"):
            subprocess.Popen(["open", fake_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(["xdg-open", fake_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[+] Fake Salary Report opened.")
    else:
        print("[-] SalaryReport.pdf not found — place it in the script folder.")
except Exception as e:
    print("[-] Failed to open fake file:", e)
