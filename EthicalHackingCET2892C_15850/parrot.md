# 🐦 Parrot OS CET2894 Lab Setup  

## 📌 Lab Purpose  
This lab prepared a **Parrot Security 6.4** virtual machine for coursework in **CET2894**.  
The VM must be saved and snapshotted for reuse.  

**Requirements:**  
- Hostname = student **last name**  
- Username = student **first name**  
- Verify tools: **Armitage**, **Metasploit DB**, **Python/IDLE**, and **Johnny**  
- Final deliverable = screenshot with `date`, `hostnamectl`, and `history` visible  

---

## 🔎 What Was Tried  
- ✅ Installed Parrot Security 6.4 from official ISO (checksum verified)  
- ⚠️ Initial hostname was set to `parrot` → caused `sudo` errors  
- ⚠️ Editing `/etc/hosts` with **nano** was difficult due to keybinding confusion (`CTRL+R` vs `CTRL+O`)  
- ⚠️ Attempted to use **Sublime Text** (`subl`, `sublime-text`) → CLI binary not linked by default  
- ⚠️ Tried to install **kerbrute** with `dpkg -i` → failed because file was not a `.deb` package  

---

## ✅ What Worked  

### Fixing Hostname
```bash
# Set hostname
sudo hostnamectl set-hostname santiago

# Overwrite /etc/hosts
sudo tee /etc/hosts >/dev/null <<'EOF'
127.0.0.1   localhost
127.0.1.1   redacted
::1         localhost ip6-localhost ip6-loopback
ff02::1     ip6-allnodes
ff02::2     ip6-allrouters
EOF

# Reboot to apply
sudo reboot
