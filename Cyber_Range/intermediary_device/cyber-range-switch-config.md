# Cyber Range Switch Configuration

This document provides the **clean baseline configuration** for the East and West Cisco Catalyst 3560 switches, 
integrated with the Cisco RV340 router serving as the DHCP server for VLAN 10 (VM and Wi-Fi clients).

##  Network Overview

- **East Switch**
  - Trunk to **West** over Gi0/1 (fiber)
  - Trunk to **RV340** over Fa0/1 (router-on-a-stick)
- **West Switch**
  - Trunk to **East** over Gi0/1
  - **WLC uplink** on Fa0/8 (VLAN 10)
  - **Lightweight AP (PoE)** on Fa0/3 (VLAN 10)
- **Native VLAN = 999** (dedicated transit)
- **VM/Data VLAN = 10**
- **DHCP** provided by Cisco RV340

---

##  East Switch Configuration

```plaintext
hostname East
no ip domain-lookup
service password-encryption

spanning-tree mode pvst
spanning-tree portfast default
spanning-tree bpduguard default
errdisable recovery cause all
errdisable recovery interval 30

vlan 10
 name VM-Network
vlan 999
 name Native-Transit

interface gi0/1
 description Trunk-to-West
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,999
 no shutdown

interface fa0/1
 description Trunk-to-RV340
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,999
 no shutdown
```

---

##  West Switch Configuration

```plaintext
hostname West
no ip domain-lookup
service password-encryption

spanning-tree mode pvst
spanning-tree portfast default
spanning-tree bpduguard default
errdisable recovery cause all
errdisable recovery interval 30

vlan 10
 name VM-Network
vlan 999
 name Native-Transit

interface gi0/1
 description Trunk-to-East
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,999
 no shutdown

interface fa0/8
 description WLC Uplink
 switchport mode access
 switchport access vlan 10
 no shutdown
 spanning-tree portfast
 spanning-tree bpduguard enable

interface fa0/3
 description Lightweight AP (PoE)
 switchport mode access
 switchport access vlan 10
 power inline auto
 no shutdown
 spanning-tree portfast
 spanning-tree bpduguard enable
```

---

## Cisco RV340 Checklist

1. Navigate to **LAN > VLAN Settings**
   - Add **VLAN 10** (172.20.10.0/24)
     - Gateway: `172.20.10.254`
     - DHCP: Enabled (`172.20.10.100–200`)
     - DNS: `10.10.10.1` (pfSense) or `10.10.10.30` (Pi-hole)
   - Add **VLAN 999** (Native/Transit)
     - DHCP: Disabled
2. Configure the port to East (Fa0/1 uplink) as **Tagged for VLAN 10,999** with **PVID 999**.

---

##  Verification Commands

Run these on both East and West:

```plaintext
show interfaces trunk
show spanning-tree interface gi0/1 detail
show cdp neighbors detail
```

You should see:
- Native VLAN = 999
- Allowed VLANs = 10,999
- No CDP mismatch errors
