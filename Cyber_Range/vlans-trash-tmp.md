🛰️ Cyber Range – West Configuration Plan
1. Network Overview

WAN / IoT (VLAN 1) → 192.168.0.0/24

Provided by ISP modem.

Used for IoT devices, Wi-Fi TVs, and guest traffic.

Management (VLAN 2) → 10.10.10.0/24

Core management network for ESXi hosts, pfSense, and admin jump servers.

VM Production (VLAN 10) → 172.20.10.0/24

Routed by Cisco RV340.

Dedicated to VMs and lab “production” services.

2. Cisco 3560 (West Switch)
VLAN Creation
vlan 2
 name MGMT
vlan 10
 name VM_NET

Trunk Uplinks (to pfSense and RV340)
interface range fa0/1 - 2
 switchport mode trunk
 channel-group 1 mode active


Native VLAN = 1

Allowed VLANs: 1,2,10

Access Ports

Assign servers or jumpbox NICs to VLAN 2 (management) or VLAN 10 (VM network).

3. pfSense (Hardware Firewall @ 10.10.10.1)

WAN: 192.168.0.x/24 (uplink to modem).

LAN: 10.10.10.1/24 (management).

OPT1: 172.20.10.1/24 (VM network).

DHCP

Configure pools per VLAN if desired.

Firewall Rules

Allow only necessary flows:

Jumpbox ↔ Mgmt network

Mgmt ↔ VM net (admin traffic)

IoT isolated, no direct access

4. Jump Server

Location: 192.168.0.0/24 (IoT/WAN zone).

Dual NICs:

NIC1 → 192.168.0.x/24

NIC2 (tagged or vNIC) → 10.10.10.x/24

Purpose: Single point of entry for management access. Prevents direct exposure of ESXi or pfSense.

5. Cisco RV340

Role: Internal router for VM Network.

VLAN 10 Interface:

172.20.10.254/24 (default gateway for VMs).

Default route → pfSense @ 10.10.10.1.

Managed via WebGUI.

6. Security Notes

Do not expose RV340 WAN on 192.168.0.0/24.

pfSense should remain the only WAN firewall.

Enforce VLAN isolation with ACLs and pfSense rules.

✅ This plan keeps IoT traffic contained, management separate, and VM production routed securely.




1. Check USB device status

Run the following to make sure the system sees your USB-to-serial adapter:

lsusb


You should see something like Prolific Technology, Inc. PL2303 Serial Port or FTDI USB Serial Device depending on the chipset.

Also check the kernel messages:

dmesg | grep tty


You should see lines like:

[ 1234.567890] usb 1-1.2: ch341-uart converter now attached to ttyUSB0


That tells you which device node was created (e.g., /dev/ttyUSB0).

2. Verify device node

List the ttyUSB devices:

ls -l /dev/ttyUSB*


You should see /dev/ttyUSB0 (or sometimes ttyUSB1, etc.).

3. Install a terminal program

You’ll need a serial terminal emulator. On Kali:

sudo apt update
sudo apt install minicom screen picocom -y


Any of those will work. I recommend screen for quick connections and minicom if you want a more router-like feel.

4. Open terminal session to the switch

Cisco console defaults: 9600 baud, 8 data bits, no parity, 1 stop bit, no flow control.

Using screen:

sudo screen /dev/ttyUSB0 9600


Using minicom (first configure with sudo minicom -s):

sudo minicom -D /dev/ttyUSB0 -b 9600


Using picocom:

sudo picocom -b 9600 /dev/ttyUSB0

5. Exit terminal session

For screen: press Ctrl+A then K (and confirm).

For minicom: Ctrl+A then X.

For picocom: Ctrl+A then Ctrl+X.
