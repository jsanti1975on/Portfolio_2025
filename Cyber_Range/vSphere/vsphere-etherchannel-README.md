# vSphere EtherChannel Configuration Guide

This document explains how to configure EtherChannel between VMware vSphere (Standard Switch) and Cisco Catalyst switches. It is designed as a lab/portfolio reference with steps for capture and validation.

---

## 📘 References
- [VMware KB: Configure Virtual Switch with an EtherChannel](https://knowledge.broadcom.com/external/article/321425)
- [VMware KB: Example Configuration of LACP](https://knowledge.broadcom.com/external/article/324490/example-configuration-of-lacp-on-vmware.html)
- [StarWind Blog: vSwitch Load Balancing Options](https://www.starwindsoftware.com/blog/esxi-vsphere-vswitch-load-balancing-options-pros-cons)
- [SysAdmin Tutorials: Network Teaming with Cisco EtherChannel](https://www.sysadmintutorials.com/tutorials/vmware-vsphere-4/vcenter4/network-teaming-with-cisco-etherchannel/)

---

## 🔧 vSphere Standard Switch Setup

1. **Create a vSwitch**
   - Add two or more physical NICs (uplinks).
   - Ensure they show as *Active*.

2. **Set NIC Teaming Policy**
   - Go to **vSwitch > Edit Settings > NIC Teaming**.
   - Policy: `Route based on IP hash`.
   - Notify Switches: `Yes`.
   - Failback: `Yes`.

3. **Port Group Settings**
   - Create a Port Group (e.g., `P_Ether`).
   - VLAN ID: `10` (must match switch config).
   - NIC Teaming: Inherit from vSwitch (unless override is needed).

---

## 🖧 Cisco Switch Configuration (Example)

```bash
conf t
!
interface range fa0/1 - 2
 description ESXi-Uplinks
 switchport mode trunk
 switchport trunk native vlan 10 <== Example Only: native 999
 switchport trunk allowed vlan 10,20
 channel-group 1 mode on
!
interface Port-channel1
 switchport mode trunk
 switchport trunk native vlan 10
!
end
wr mem
```

---

## ✅ Verification

On **Cisco**:
```bash
show etherchannel summary
show interfaces trunk
```

On **ESXi**:
- vSwitch shows both uplinks as Active.
- Port Group inherits IP Hash setting.

---

## 🎥 Capture Plan for Portfolio

1. Screenshot vSwitch settings (uplinks, IP Hash).
2. Screenshot Port Group config with VLAN 10.
3. Capture Cisco CLI showing `show etherchannel summary`.
4. Optional: create a mismatch (different VLAN) and capture error message, then fix it.
5. Document before/after results in GitHub repo.

---

## 📌 Notes
- EtherChannel requires **matching settings** on both ends.
- Do not mix load balancing types (must be IP Hash on vSphere + EtherChannel on Cisco).
- If using LACP, you must configure on both Cisco and a vDS (not vSS).

---
