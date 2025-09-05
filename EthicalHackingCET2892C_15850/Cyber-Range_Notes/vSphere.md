📝 Lab Guide – Importing OVF Templates into ESXi

This guide documents how I deployed lab machines (Windows 7, Windows 10, DC01, DC02, Metasploitable2) into ESXi from pre-built OVF templates.

It also covers troubleshooting the common error:

Line 25: Unsupported hardware family "vmx-21"

📌 Step 1 – Upload OVF Files to Datastore

Log into ESXi host web UI → Storage → Datastore Browser.

Create a new folder for the VM (e.g., OSeven).

Upload the following files:

.ovf

.vmdk

.mf (optional but recommended)

<img width="1891" height="961" alt="OVF_Edit" src="https://github.com/user-attachments/assets/eb2f1cf0-16b9-4e0e-a061-825de222171a" />

<img width="1031" height="669" alt="Line 25 Unsupported Hardware" src="https://github.com/user-attachments/assets/5b6d6b4c-9026-4565-bd87-150a8801eedb" />

<img width="1031" height="669" alt="Line 25 Unsupported Hardware" src="https://github.com/user-attachments/assets/e7e55e69-d603-4dff-922b-1ec3c825fdd2" />

📷 Helper Images

📌 Step 2 – Deploy OVF

Navigate to Virtual Machines → Create / Register VM.

Select Deploy a virtual machine from an OVF or OVA file.

Choose the uploaded .ovf, .vmdk, and .mf.

Select storage → choose datastore.

Assign NIC → map to CyberRange3 Port Group (connected to pfSense 10.16.32.0/24).

Review → Finish.

📷 Screenshot Placeholder – Deploy OVF Wizard

⚠️ Common Error: Unsupported Hardware Family

During deployment, I hit the following error:

Line 25: Unsupported hardware family "vmx-21"


📷 Screenshot Placeholder – Error message during OVF import

🔧 Step 3 – Fixing the Hardware Compatibility
Option A – Edit OVF File

Download the .ovf file.

Open in Notepad++ or VS Code.

Find line:

<vssd:VirtualSystemType>vmx-21</vssd:VirtualSystemType>


Replace with:

<vssd:VirtualSystemType>vmx-14</vssd:VirtualSystemType>


(for ESXi 7.x; for ESXi 6.7 use vmx-13)

Save → Re-upload → Retry deployment.

📷 Screenshot Placeholder – OVF file before/after edit

Option B – Create VM Manually

Create New VM → Custom.

Select guest OS type (Windows/Linux).

When asked for disks → Use Existing Disk → select .vmdk from datastore.

Finish → Attach NIC to CyberRange3.

Option C – Re-export VM at Lower Compatibility

If VM is still available in Workstation/Fusion:

VM settings → Compatibility / Hardware Compatibility.

Downgrade to Workstation 14.x / ESXi 6.7.

Re-export OVF.

📌 Step 4 – Power On and Verify

Power on the imported VM.

Open console → verify OS boots.

Assign IP (static or DHCP from pfSense).

Ping pfSense gateway 10.16.32.1 to confirm connectivity.

📷 Screenshot Placeholder – Successful VM boot in ESXi console

✅ Key Takeaways

OVF deployments may fail if virtual hardware version (vmx-XX) is too new for ESXi.

Quick fix: Edit .ovf file and downgrade hardware version.

Long-term fix: Export VMs at the correct compatibility level.

Once deployed, ensure VMs are connected to the correct lab network (CyberRange3) for Nessus scanning.

💡 With these fixes, I successfully deployed my class lab VMs into ESXi and connected them to my Cyber Range (10.16.32.0/24) behind pfSense.
