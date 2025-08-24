Cyber-Lab Dashboard Launcher — Step-by-Step (GitHub-ready)

Tiny Win32 EXE that opens your lab dashboard. This guide shows how to customize the IP/URL (e.g., for JumpBox on VLAN1), build, and deploy.

1) Get the project

If you already downloaded the ZIP from me, add it to your repo.

Or clone your GitHub repo and copy the folder cyber-lab-dashboard-launcher/ into it.

Project layout:

cyber-lab-dashboard-launcher/
├─ build.sh
├─ README.md
└─ src/
   ├─ open_dash.c
   ├─ icon.rc
   └─ open-dash.ico

2) Prerequisites (build on Debian/Ubuntu/Kali)
sudo apt update
sudo apt install -y mingw-w64


(Optional: wine is only needed if you plan to test the EXE with Wine.)

3) Customize for JumpBox (VLAN1)

Open src/open_dash.c and change both lines:

Before

system("ping 10.10.10.1");
system("start msedge.exe http://10.10.10.30:8000/");


Example (JumpBox on VLAN1)

system("ping 192.168.0.1");                      // <- your JumpBox gateway on VLAN1
system("start msedge.exe http://192.168.0.50:8000/");  // <- your dashboard URL for VLAN1


Tip: If you need two launchers (Mgmt + JumpBox), build once for each network (see Step 6).

4) Build the EXE
cd cyber-lab-dashboard-launcher
./build.sh


Output:

./open-dash.exe


Manual compile (equivalent):

cd src
x86_64-w64-mingw32-windres icon.rc -O coff -o icon.res
x86_64-w64-mingw32-gcc open_dash.c icon.res -o ../open-dash.exe -mwindows -s

5) Run / Test (on Windows)

Copy open-dash.exe to the Windows machine.

Double-click to run. It relaunches minimized, pings the gateway, waits ~5s, and opens Edge to your URL.

If Edge isn’t in PATH, replace msedge.exe with the full path (e.g., C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe).

6) (Optional) Build two profiles (Mgmt & JumpBox)

Mgmt build

# Edit src/open_dash.c to mgmt net values (e.g., 10.10.10.1 and http://10.10.10.30:8000/)
./build.sh
mv open-dash.exe open-dash-mgmt.exe


JumpBox build

# Edit src/open_dash.c to jumpbox net values (e.g., 192.168.0.1 and http://192.168.0.50:8000/)
./build.sh
mv open-dash.exe open-dash-jumpbox.exe


Commit both to your repo.

7) Optional: Auto-launch at login (Windows)

Press Win + R → type shell:startup → Enter.

Place a shortcut to open-dash-*.exe in the Startup folder.

8) Troubleshooting

No browser opens: Confirm Edge path; try full path in system("start ...") or use start "" "http://..." syntax:

system("start \"\" msedge.exe http://192.168.0.50:8000/");


Ping fails: Verify the gateway IP from the target machine (ipconfig on Windows).

Firewall prompts: Allow the EXE to run and let Edge access the network.

Console flash: The build uses -mwindows to suppress a console. If you want a console for debugging, remove -mwindows.

9) Commit & Push (example)
git add cyber-lab-dashboard-launcher
git commit -m "Add Cyber-Lab Dashboard Launcher with JumpBox VLAN1 config"
git push

10) Quick reference (edit points)

File to edit: src/open_dash.c

Replace:

ping 10.10.10.1 → your VLAN1 gateway (e.g., 192.168.0.1)

http://10.10.10.30:8000/ → your VLAN1 dashboard URL (e.g., http://192.168.0.50:8000/)

Rebuild with ./build.sh

If you want this to read the IP/URL from a config file or environment variables (so you don’t recompile for each network), say the word and I’ll drop in that variant.
