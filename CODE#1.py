import smtplib
import requests
import platform
import socket
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ===== YOUR EMAIL SETTINGS =====
SENDER_EMAIL = "decoyalerts18@gmail.com"
APP_PASSWORD = "enrm dpec loki rhrk"   # Your Google App Password
RECEIVER_EMAIL = "decoyalerts18@gmail.com"  # You can use same or different email

# ===== PATH TO DUMMY PDF =====
DUMMY_PDF = r"C:\Users\VASUNDHARA\Desktop\Credentials\AWS_Credentials.pdf"


def get_system_info():
    """Collect IP, location, and device details"""
    try:
        # Get Public IP
        ip = requests.get("https://api.ipify.org?format=json").json()["ip"]

        # Get Location
        location_data = requests.get(f"https://ipapi.co/{ip}/json/").json()
        city = location_data.get("city", "Unknown")
        region = location_data.get("region", "Unknown")
        country = location_data.get("country_name", "Unknown")

        # Device Info
        device = platform.platform()
        hostname = socket.gethostname()

        return ip, f"{city}, {region}, {country}", device, hostname

    except Exception as e:
        return "Unknown", "Unknown", "Unknown", str(e)


def send_email():
    """Send alert email with system info"""
    ip, location, device, hostname = get_system_info()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subject = "🚨 ALERT: Decoy File Accessed 🚨"
    body = f"""
    Alert! Someone tried to open the decoy file.

    📅 Time: {current_time}
    🌍 Location: {location}
    💻 Device: {device}
    🖥️ Hostname: {hostname}
    🌐 IP Address: {ip}
    """

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("✅ Alert email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


def open_dummy_pdf():
    """Open dummy PDF so attacker sees it"""
    try:
        os.startfile(DUMMY_PDF)  # Works on Windows
        print("📄 Dummy PDF opened.")
    except Exception as e:
        print(f"❌ Could not open PDF: {e}")


if __name__ == "__main__":
    send_email()
    open_dummy_pdf()
