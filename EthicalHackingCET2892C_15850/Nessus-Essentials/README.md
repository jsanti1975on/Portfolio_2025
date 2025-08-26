📂 Nessus-Essentials/README.md
# 🔍 Nessus Essentials Lab

## 📌 Overview
This lab documents the installation and configuration of **Nessus Essentials** inside my cyber range environment.  
Nessus was chosen instead of OpenVAS due to stability issues in recent Kali releases.

---

## 🛠️ Steps Performed
1. Registered for Nessus Essentials activation code at Tenable
2. Downloaded Debian `.deb` package via Firefox
3. Installed with:
   ```bash
   sudo dpkg -i Nessus-*.deb
   sudo apt --fix-broken install -y


Enabled and started service:

sudo systemctl enable nessusd
sudo systemctl start nessusd


Accessed https://<ip>:8834/ in Firefox

Accepted certificate warning → selected Nessus Essentials

Entered activation code, created admin account

Waited for plugins to finish compiling

✅ Verification

Plugins finished compiling

Nessus dashboard accessible

Able to create new scans (Basic Network Scan, Host Discovery, etc.)

📷 Screenshots

Installation complete


Plugins Compiled


Dashboard Logged In
