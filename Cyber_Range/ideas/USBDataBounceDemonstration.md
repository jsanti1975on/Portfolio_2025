# USB Data Bounce Demonstration

## 🎯 Objective
This lab demonstrates **USB data bouncing** in a controlled cyber range environment.  
Instead of malware, a **benign portable executable (PE)** (`dashboard-launcher.exe`) is used to simulate how attackers can move payloads between systems **without using network file shares**.

---

## 🔹 Lab Environment
- **Systems**  
  - Windows 7 (EOL)  
  - Windows 10  
  - Windows Server 2022  
  - Windows Small Business Server (SBS)  
  - Exchange Server 2016 (optional test target)  

- **Media**  
  - USB Flash Drive (any size, formatted FAT32 or NTFS)  

- **Executable Payload**  
  - `dashboard-launcher.exe` (compiled from [cyber-lab-dashboard-launcher](../cyber-lab-dashboard-launcher))  

---

## 🔹 Lab Steps

### Step 1 — Prepare the Payload
1. Compile or download `dashboard-launcher.exe`.  
2. Generate a hash to verify later:
   ```powershell
   certutil -hashfile dashboard-launcher.exe SHA256
```

Record the hash in your notes.

📸 Screenshot: Hash output on System A

Step 2 — Stage on System A

Insert USB into System A (e.g., Windows 10).

Copy dashboard-launcher.exe to the USB.

Safely eject the USB.

📸 Screenshot: File copied to USB

Step 3 — Bounce to System B

Insert the USB into System B (e.g., Windows 7 or Server 2022).

Copy the file locally.

Verify integrity:

certutil -hashfile dashboard-launcher.exe SHA256


Confirm the hash matches the original.

📸 Screenshot: Hash output on System B

Step 4 — Remote Bounce Simulation (Optional)

This step shows how USB bouncing can occur remotely using redirection.

Option A: USB/IP (Windows ↔ Windows/Linux)
usbipd list          # list USB devices
usbipd bind -b <BUSID>
usbipd attach -w <BUSID>


The remote system will now see the USB as a local device.

Option B: VMware / VirtualBox Passthrough

Map the USB device from host → guest VM.

Option C: RDP USB Redirection

In an RDP session, enable local resources → devices → USB to forward the flash drive.

📸 Screenshot: Remote system detecting USB as “locally attached”

Step 5 — Documentation

Record SHA256 hashes at each stage.

Note whether the PE executed successfully on each OS.

Highlight the fact that the transfer occurred without SMB, FTP, or HTTP traffic.

📸 Screenshot: Execution of launcher.exe on target machine

🔹 Key Takeaways

USB = Bounce Point → Used for both payload delivery and data exfiltration.

Air-Gap Risk → Even disconnected systems can be bridged via removable media.

Remote Redirection → USB/IP and RDP passthrough extend the concept beyond physical insertion.

Defensive Controls:

Disable autorun on USB devices.

Restrict or monitor USB use with DLP policies.

Use signed media or encrypted company-issued drives.

📂 Screenshots & Evidence

 Hash on System A

 File on USB

 Hash on System B

 Remote bounce (USB/IP or RDP passthrough)

 Execution test results

✅ Status

Lab Ready ✅

Payload: benign PE only (dashboard-launcher.exe)

No malware used in this demonstration.


---


