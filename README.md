**DecoyDocs — CODE#1**

**What this is**

_CODE#1_ is a simple **defensive decoy script** that mimics a sensitive document (e.g., SalaryReport.pdf).
When run, it opens a fake/decoy PDF (if present) and writes a human‑readable access record to a logs folder on the Desktop. It’s designed for classroom demos and local, low‑risk detection of casual snooping.

**Quick summary**

Presents a believable _ “salary report” PDF_ and logs a timestamped access entry to_ ~/Desktop/logs/access_log.txt._

**What the script does**

- Looks for SalaryReport.pdf in the same folder where the script is run.
- Creates a logs folder on the current account’s Desktop (if missing).
- Appends a readable log entry (Date/Time, Accessed By (username), Device Name, Public IP placeholder, Location forced to Coimbatore/Tamil Nadu/India, OS) to access_log.txt inside the logs folder.
- Attempts to open the fake PDF with the OS default viewer (so the interaction appears normal).

  ## **Installation & Implementation Guide (CODE#2)**
  - This short guide shows one safe way to place the CODE#1 script on a machine so it behaves as a decoy: it looks like a sensitive file, opens a fake salary PDF when clicked, and writes an access log to a logs folder. Only deploy on machines you own or where you have explicit written permission. Misuse of deception tools may be illegal or violate policy.

**Overview**

- A folder named like a sensitive item (example: SalaryReport) containing:
- A single executable named to look like a report (e.g. Salary_Report.exe) — this is your decoy app (converted from the Python script).
- A fake SalaryReport.pdf that opens when the decoy is launched.
- A logs folder (on Desktop or another path you configured) where access_log.txt will be appended each time the decoy is opened.

**1) Create a folder with a “sensitive” name**
- On the target computer, create a new folder and give it a convincing, sensitive-looking name such as SalaryReport, Payroll_2025, or Executive_Salaries.
- This is the folder an intruder will explore; keeping the name realistic increases the decoy’s believability.

**2) Save the Python script inside that folder and give it a credible name**

- Save your original CODE#1 Python file into the folder created above.
- Rename the file so it looks like a real document or report name (for example, Salary_Report.py). The exact name you choose should match how you want it to appear to a casual viewer.

**3) Convert the Python script to a stand‑alone executable (so it looks like an app/file)**

A. Preparation (one-time)
- Install Python (if not already): download from python.org and install for all users or current user. Make sure “Add Python to PATH” is checked.
- Open Command Prompt or PowerShell as a normal user (no admin required for packaging).

B. Recommended: 
- create and use a virtual environment (keeps packages clean)

Command Prompt
```bash
cd C:\path\to\SalaryReport        (go to your folder)
python -m venv venv
venv\Scripts\activate
```
PowerShell
```bash
cd C:\path\to\SalaryReport
python -m venv venv
.\venv\Scripts\Activate.ps1
```
C. Install PyInstaller
```bash
pip install --upgrade pip
pip install pyinstaller
```

D. Simple one-file executable (no bundled PDF)

Command Prompt
```bash
pyinstaller --onefile --noconsole your_script.py
```
PowerShell
```bash
pyinstaller --onefile --noconsole your_script.py
```
After it finishes, the .exe will be at:
```bash
C:\path\to\SalaryReport\dist\your_script.exe
```

**4) Create the fake (dummy) salary PDF and point the script to it**

- Create a harmless dummy PDF named SalaryReport.pdf (or whatever name you used) and put it inside the same folder as the executable.
- The PDF should contain fake, clearly non-sensitive placeholder text (e.g., “CONFIDENTIAL — DEMO ONLY” or fabricated sample figures). This keeps the demo realistic without leaking real data.
- Open the Python script file (or its source copy) and ensure the path used by the script to locate the PDF matches the actual PDF path. If the script expects the PDF in the same folder as the executable, make sure the PDF is indeed there.

**5) Create the logs folder in the path specified by the script**

- Decide where you want logs to be written. This README follows the example used in CODE#1 — a logs folder on the current user’s Desktop.
- Create a logs folder at that location (e.g., C:\Users\<user>\Desktop\logs on Windows or ~/Desktop/logs on macOS/Linux).
- Alternatively, change the script’s logs_folder variable to a different path and create that folder instead.
- Confirm the script/executable has write permission to that folder. If it cannot write logs, the decoy won’t record access events

**6) Test the setup (important)**

- Double‑click the executable (Salary_Report.exe) inside the SalaryReport folder.

Confirm that:

- The fake PDF opens in the default viewer.
- A new entry was appended to access_log.txt inside your logs folder.
- Inspect the log entry to ensure it contains the expected metadata (timestamp, username, hostname, OS, etc.).
- If the PDF doesn’t open or no log appears, re-check:
- That the PDF filename and path match what the script expects.
- That the logs folder path is correct and writable by the user account running the executable.

**7) Hardening recommendations**

- Keep the logs folder in a place less obvious than the Desktop if you need more resilience (but remember local logs can be deleted by an attacker).
- Consider periodically copying logs to a secure external collector or a sync location under your control.
- Do not store SMTP/API credentials or other secrets inside the script or checked‑in files. Use environment variables or a secure secret store for production use.

**8) Responsible use & legal checklist** 

- Before you deploy anywhere, confirm all of the following:
- You own the machine or have explicit written authorization to run deception/testing tools on it.
- Everyone who needs to respond to alerts/logs (e.g., an instructor or security team) has been informed about the experiment and how to interpret alerts.
- No real personal data, credentials, or actual company secrets are included in the decoy content or repository.
- You have an incident response plan in case the decoy triggers a real incident.

**9) Quick troubleshooting pointers**

- If the executable fails to launch the PDF: verify the PDF path and file name match exactly; file extension case sensitivity can matter on some systems.
- If logs are missing: check folder permissions, and make sure the script is not being blocked by antivirus while trying to write files.
- If packaging the script produced warnings from security software: test only in isolated/demo environments and review anti‑malware logs.

**DecoyDocs — CODE#2**

**What this is**

_CODE#2_ is a defensive decoy script that mimics a sensitive credentials file (e.g., Updated_Credentials.pdf).
When run, it opens a fake/decoy PDF (if present) and sends an email alert to a configured address with minimal metadata (timestamp, username, hostname, decoy filename). It’s intended for classroom demos and low‑risk detection of unauthorized local access.

**Quick summary**

- Presents a believable “credentials” PDF and alerts the owner by email while also optionally writing a local log entry.

**What the script does**

- Looks for Updated_Credentials.pdf in the same folder where the script is run (or uses an embedded copy if bundled).
- Opens the fake PDF in the default viewer so the interaction appears normal.
- Sends a concise alert email to the configured recipient containing timestamp, local username, hostname, and the decoy filename (no file contents).
- Optionally writes a local log entry (if configured in the script).
- Email credentials and recipient are read from environment variables (keeps secrets out of the repo)

## **Installation & Implementation Guide (CODE#2)**

- This guide shows how to place CODE#2 on a machine so it behaves as a decoy: it opens a dummy credentials PDF and sends an email alert. Only deploy on machines you own or where you have explicit written permission. Misuse of deception or alerting tools can be illegal or violate policy.
- CODE#2 is a defensive decoy script that mimics a sensitive credentials file (e.g., Updated_Credentials.pdf).
- When run, it opens a fake/decoy PDF (if present) and sends an email alert to a configured address with minimal metadata (timestamp, username, hostname, decoy filename). It’s intended for classroom demos and low‑risk detection of unauthorized local access.

**Overview**

- You will create a folder named like a sensitive item (example: AWSCredentials) containing:
- A single executable named to look like a credentials file (e.g., Updated_Credentials.exe) — converted from the Python script.
- A fake Updated_Credentials.pdf that opens when the decoy is launched (or bundled into the exe).
- Optionally a logs folder where local logs are written.

**1) Create a folder with a “sensitive” name**
- On the target computer, create a new folder and give it a convincing name such as AWSCredentials, AWS_keys, or Updated_Credentials.
- This folder is the decoy location an intruder will explore; make the name realistic to increase believability.

**2) Save the Python script inside that folder and give it a credible name**

- Save your CODE#2 Python script into the folder (for example cred_decoy.py).
- Rename the file so it appears legitimate (for example Updated_Credentials.py or AWS-Creds.py).

**3) Configure email settings (use environment variables)**

- SMTP_HOST — SMTP server hostname (e.g., smtp.example.com)
- SMTP_PORT — SMTP port (usually 587 for STARTTLS or 465 for SSL)
- SMTP_USER — SMTP username (email address or service user)
- SMTP_PASS — SMTP password / app password / API key
- ALERT_TO — recipient email address for alerts
- ALERT_FROM — optional from address

**4) Convert the Python script to a stand‑alone executable**

A. Preparation (one‑time)
- Install Python if not present and ensure “Add Python to PATH” is enabled.
- Open Command Prompt or PowerShell (normal user).

B. Recommended: 
- create and use a virtual environment

Command Prompt
```bash
cd C:\path\to\AWSCredentials
python -m venv venv
venv\Scripts\activate
```
PowerShell
```bash
cd C:\path\to\AWSCredentials
python -m venv venv
.\venv\Scripts\Activate.ps1
```

C. Install PyInstaller
```bash
pip install --upgrade pip
pip install pyinstaller
```

D. Build a single .exe

- If you want the PDF kept beside the exe:
```bash
pyinstaller --onefile --noconsole --name Updated_Credentials cred_decoy.py
```
- If you want a single file that bundles the PDF (optional):
```bash
pyinstaller --onefile --noconsole --name Updated_Credentials --add-data "Updated_Credentials.pdf;." cred_decoy.py
```
- If you bundle the PDF, ensure your script resolves the bundled resource (use sys._MEIPASS when sys.frozen is true).
After building, the executable will be in:
```bash
C:\path\to\AWSCredentials\dist\Updated_Credentials.exe
```
- Place Updated_Credentials.pdf next to the exe if you did not bundle it.

**5) Create the fake (dummy) credentials PDF and point the script to it**

- Create a harmless dummy PDF named Updated_Credentials.pdf and place it inside the same folder as the executable (or bundle it).
- The PDF should contain clearly fake placeholder text such as “DEMO ONLY — NO REAL CREDENTIALS”.
- Ensure the script’s PDF path logic matches your packaging choice (external file or bundled resource).

**6) Test the setup (important)**

- Open a fresh terminal (to pick up env vars) or simply double‑click Updated_Credentials.exe.

Confirm:

- The fake PDF opens in the default viewer.
- An email alert arrives at the ALERT_TO address containing the expected metadata (timestamp, username, hostname, decoy filename).
- If enabled, a local log entry is appended to the logs folder.
- If email does not arrive, check:
- The script’s console/log output (temporarily remove --noconsole while testing).
- That environment variables are exported and visible to the process.
- SMTP server, port, and authentication method (use app passwords or API keys where applicable).

**7) Hardening & best practices**

- Keep SMTP/API credentials out of source control.  
- Use transactional email providers or app passwords for better security.  
- Implement simple rate limiting (no more than one alert per X minutes).  
- Consider bundling the PDF only if your script handles `sys._MEIPASS`.

**8) Responsible use & legal checklist**

- You own the machine or have explicit written authorization.  
- Responders know the decoy is in use.  
- No real personal data or credentials are included.  
- An incident response plan exists.

**9) Quick troubleshooting**

- No email: verify env vars, SMTP host/port, and auth method.  
- PDF won’t open: if bundled, confirm `--add-data` and `sys._MEIPASS` usage; if external, ensure PDF is beside the exe.  
- AV flags exe: test in isolated environments and consult security if needed.

---

## License
This project is under a custom license that allows personal and educational use only. Public forks and redistribution are prohibited without permission explicitly from me !

---

## Credits

Created by Vasuntthara
