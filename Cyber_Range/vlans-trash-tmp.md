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


===== Completed - Below is quik and dirty save for recall =====

<img width="1130" height="1094" alt="cyber-range-image" src="https://github.com/user-attachments/assets/396ffea1-8556-40fb-9163-35f498bf694d" />

Perfect — thanks for the screenshot, I see you’re on the East switch with VLAN 10 already created. You want to bundle Fa0/7 and Fa0/8 into an EtherChannel, trunk it, and then tie it to VLAN 10 (172.20.10.0/24) for your ESXi server.

Here’s your step list for the Cisco 3560:

🔹 Step 1 – Enter Global Config
enable
configure terminal

🔹 Step 2 – Create the EtherChannel (Port-Channel 2)

We’ll use LACP (802.3ad) since ESXi supports it.

interface range fa0/7 - 8
 switchport mode trunk
 channel-group 2 mode active


This creates Port-Channel 2 and adds Fa0/7 + Fa0/8 to it.

🔹 Step 3 – Configure the Port-Channel Interface

Now configure the logical port-channel itself:

interface port-channel 2
 switchport mode trunk
 switchport trunk allowed vlan 10


This ensures only VLAN 10 traffic passes between your ESXi host and the switch.

🔹 Step 4 – Verify

Check EtherChannel status:

show etherchannel summary


You should see Po2(SU) meaning it’s up and using LACP.

Check trunk:

show interfaces trunk


You should see Port-Channel 2 with VLAN 10 allowed.

🔹 Step 5 – ESXi Side

On ESXi, configure the vSwitch uplinks (vmnic2 + vmnic3) for Link Aggregation (LACP):

Go to Networking → vSwitch1 → Edit.

Under Teaming and Failover, set Load Balancing to Route based on IP hash.

Add vmnic2 and vmnic3 as Active uplinks.

Enable LACP (active mode) for the uplink group.

✅ At this point, your ESXi host will talk to the East switch on a 2x100 Mbps aggregated trunk, carrying VLAN 10 for your 172.20.10.0/24 West network.

Would you like me to also print the running-config snippet you should expect on the switch after applying these commands (so you can compare to your console output)?

You said:
we need to do do the 802.11 command on the trunk first?
ChatGPT said:

Good question 👍 — you don’t need to use any dot1q or 802.1q encapsulation command on the switch trunk.

Here’s why:

On Catalyst switches (like your 3560), trunk encapsulation used to be selectable between ISL and 802.1q with this command:

switchport trunk encapsulation dot1q


But on newer IOS versions and on 3560/2960 family switches, the hardware only supports 802.1Q, so the command is either hidden or not available. The switch defaults to dot1q.

✅ For your setup (3560 + ESXi)

You only need:

switchport mode trunk
switchport trunk allowed vlan 10


No extra 802.1q command is required — it’s already implied.

🔹 Order of operations

When you configure an EtherChannel trunk:

Define the physical interfaces (set trunk + channel-group).

Configure the Port-Channel interface (set trunk, allowed VLANs, etc.).

Example:

interface range fa0/7 - 8
 switchport mode trunk
 channel-group 2 mode active

interface port-channel 2
 switchport mode trunk
 switchport trunk allowed vlan 10


That’s enough. The switch automatically uses 802.1q.

👉 Do you want me to also add the VLAN 10 native VLAN configuration (so that untagged traffic from ESXi maps to VLAN 10), or do you want it strictly tagged VLAN 10 only?

You said:
Great - in an effort to recall - print the cyber range update progress based on what was just done.
ChatGPT said:

Here’s a recap of your Cyber Range update progress based on what you just completed:

✅ Current Progress Recap
1. Switch (Cisco 3560 – East) Configuration

Hostname successfully set to East.

VLANs created and verified:

VLAN 1 (default)

VLAN 2 (MGMT)

VLAN 10 (Production / West network) → bound to ports Fa0/3–Fa0/7, Gi0/1.

EtherChannel configured (so far Fa0/1–Fa0/2 are aggregated for router uplink).

Preparing Fa0/7–Fa0/8 to be bundled into another EtherChannel for the ESXi server trunk on VLAN 10.

2. Router (Cisco RV340 – West Edge Gateway)

IP: 172.20.10.254 (Default Gateway for VLAN10).

Connected to East switch via aggregated link (Fa0/1–Fa0/2).

Confirmed reachability from inside the ESXi environment.

3. ESXi Host (172.20.10.103)

Connected to East switch via Fa0/7–Fa0/8 (ready for LACP trunk).

VMkernel NIC on VLAN10 subnet (172.20.10.103/24) is live.

Verified end-to-end connectivity:

Successful ping from Red Hat workstation VM inside ESXi → 172.20.10.254 (RV340 Gateway).

4. Client VM (Red Hat Workstation)

Network config: 172.20.10.103/24, default gateway 172.20.10.254.

Successfully pinged gateway with 0% packet loss.

Proof that VLAN10 + RV340 + East switch trunk are working.

🔜 Next Steps to Advance the Cyber Range

Finalize EtherChannel for ESXi uplink

Bundle Fa0/7–Fa0/8 into Port-channel 2 with mode active (LACP).

Configure trunking to allow VLAN10.

ESXi Networking Config

Create a vSwitch uplink bound to Port-channel (LACP).

Tag VLAN10 for production workloads.

Optionally create separate Port Groups (MGMT, VLAN10).

Domain Integration

Prepare your orkidz-west.arpa AD/DNS server to hand out IPs to clients in VLAN10.

Add the Red Hat workstation as a domain client (if desired).

Cyber Range Growth

Connect additional West servers (file server, AD DC, test VMs).

Begin cross-zone testing (East ↔ West) for routing and firewall rules via pfSense.

Would you like me to print the exact Cisco commands to finish the Fa0/7–Fa0/8 LACP trunk setup for ESXi (Port-channel 2, VLAN10 trunk), so you can paste them directly into your switch config?

You said:
Print the cli steps using putty on the win 11 jump box to link fa0/7 - 8
ChatGPT said:

Perfect — here’s a step-by-step CLI guide you can follow on your Windows 11 jump box using PuTTY to configure Fa0/7 and Fa0/8 into an LACP trunk (Port-channel 2) on your Cisco 3560 switch.

🔌 Steps in PuTTY (Windows 11 Jump Box)
1. Launch PuTTY and Open Console Session

Plug in your USB-to-Serial console cable.

Open Device Manager → check the COM port assigned (e.g., COM3).

Launch PuTTY → select Serial.

Serial line: COM3 (or whatever you saw in Device Manager).

Speed: 9600.

Click Open.

Press Enter until you see the switch prompt.

2. Enter Global Config Mode
Switch> enable
Switch# configure terminal

3. Change Hostname to West
Switch(config)# hostname West
West(config)#

4. Create the Port-Channel (Channel-group 2)
West(config)# interface range fa0/7 - 8
West(config-if-range)# channel-group 2 mode active
West(config-if-range)# exit


mode active = LACP (industry standard).

Both interfaces are now logically bundled into Port-channel 2.

5. Configure Port-Channel 2 as a Trunk
West(config)# interface port-channel 2
West(config-if)# switchport mode trunk
West(config-if)# switchport trunk allowed vlan 10
West(config-if)# exit

6. Verify EtherChannel & Trunk
West# show etherchannel summary
West# show interfaces trunk


Po2 should show up as SU (Layer 2, in use).

Trunk should list VLAN 10 as allowed and active.

✅ At this point:

Fa0/7 + Fa0/8 are bundled as Port-channel 2.

The trunk is carrying VLAN10 to your ESXi host.

The ESXi vSwitch uplink (vmnic2/vmnic3) will need to be set to LACP to complete the bundle.

Would you like me to also print the matching ESXi host steps (so vmnic2 + vmnic3 are bound to LACP in vSwitch1), right after you finish the Cisco side?

For screen: press Ctrl+A then K (and confirm).

For minicom: Ctrl+A then X.

For picocom: Ctrl+A then Ctrl+X.
