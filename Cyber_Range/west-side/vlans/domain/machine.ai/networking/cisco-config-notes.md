# 🏗️ DHCP Transition – Cisco RV340 → Windows Server (machine.ai Domain)

This guide documents the workflow for installing new servers in the `machine.ai` domain
on the **10.10.20.0/24** subnet.  
During initial VM builds, the **Cisco RV340** provides DHCP.  
Once servers are patched and promoted into the domain, DHCP is handed over to a
Windows Server (GAN) for enterprise-style management.

---

## ⚙️ Phase 1 – Initial VM Install (DHCP on RV340)

- VLAN: **10.10.20.0/24**  
- RV340 interface: **10.10.20.254**  
- Temporary DHCP scope:
  - Start: `10.10.20.100`
  - End: `10.10.20.149`
  - Gateway: `10.10.20.254`
  - DNS: `Use DNS from ISP` (temporary)

➡️ All new VMs (ANN, GAN, NLG, EXCH01, Win10/11 clients) boot, install OS, and
receive temporary IP addresses from the RV340.

---

## ⚙️ Phase 2 – Assign Static IPs

After OS + VMware Tools installation:

| Hostname | Role(s)        | Static IP     | DNS Setting |
|----------|----------------|---------------|-------------|
| ANN      | AD DS, DNS     | `10.10.20.1`  | 10.10.20.1 |
| GAN      | AD DS, DHCP    | `10.10.20.2`  | 10.10.20.1 |
| NLG      | File Server    | `10.10.20.3`  | 10.10.20.1 |
| EXCH01   | Exchange 2019  | `10.10.20.50` | 10.10.20.1 |

---

## ⚙️ Phase 3 – Promote Domain Controllers

1. Promote **ANN (10.10.20.1)** to a new forest:  
   - Domain = `machine.ai`  
   - DNS service installed  

2. Promote **GAN (10.10.20.2)** to a secondary DC:  
   - Replicates AD DS & DNS from ANN  
   - Prepare to host DHCP role

---

## ⚙️ Phase 4 – Transition DHCP

### On RV340
1. Navigate: **LAN → VLAN Settings → VLAN5 (10.10.20.0/24)**  
2. Change **DHCP Type** from `Server` → `Relay`  
3. Set **DHCP Server IP** → `10.10.20.2` (GAN)

### On GAN (10.10.20.2)
1. Add the **DHCP Server role**  
2. Create a new scope:
   - Start: `10.10.20.100`
   - End: `10.10.20.200`
   - Gateway: `10.10.20.254`
   - DNS: `10.10.20.1`
3. **Authorize** the DHCP server in AD DS

---

## ⚙️ Phase 5 – Client Verification

- Deploy a Windows 10/11 client in VLAN5  
- During install → address comes from RV340  
- After handoff → address comes from GAN DHCP scope  
- Verify:
  - Lease in range `10.10.20.100–200`
  - DNS resolves `machine.ai`
  - Client joins domain successfully

---

## ✅ Summary

- RV340 DHCP simplifies initial server builds  
- Windows DHCP (GAN) provides enterprise-grade control  
- AD authorization ensures secure, centralized management  
- `machine.ai` domain fully operational on 10.10.20.0/24
