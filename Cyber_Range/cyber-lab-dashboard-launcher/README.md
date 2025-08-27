This launcher is for demonstration and kiosk workflows in a controlled, consented lab. It does not persist, elevate, obfuscate, or communicate beyond opening a local dashboard URL after a short delay. All use occurs on systems I own/manage.


# Cyber-Lab Dashboard Launcher (Win32, no console)

<img width="1657" height="887" alt="exe-00" src="https://github.com/user-attachments/assets/bf68d0e8-ceac-4002-acb2-8bb68e1a8d5a" />


A tiny Windows launcher that opens your lab dashboard **without flashing a console** by relaunching itself minimized via **PowerShell**. Useful for kiosk/JumpBox workflows and as a teaching step before moving to config-driven variants.

---

## Repository Layout

```bash
cyber-lab-dashboard-launcher/
├─ README.md
├─ build.sh # one-command build on Kali/Debian/Ubuntu
├─ .gitignore
└─ src/
├─ open_dash.c # PowerShell minimized relaunch + ping + open URL
├─ icon.rc # embeds app icon into the EXE
└─ open-dash.ico # multi-resolution icon (16..256px)
```

## Prerequisites (builder host)

```bash
sudo apt update
sudo apt install -y mingw-w64 imagemagick
```

## Build

```bash
./build.sh
# Output: ./open-dash.exe
```

> *Copy open-dash.exe to a Windows machine and double-click*

## Configure (edit hardcoded targets)
> In src/open_dash.c, set the active network:

```c
// VLAN1 example
system("ping 172.20.10.1");
system("start msedge.exe http://172.20.10.30:8000/");

// Mgmt example
// system("ping 10.10.10.1");
// system("start msedge.exe http://10.10.10.30:8000/");
```
> Rebuild to bake changes into the EXE.

## Icon (multi-resolution .ico)

> Place your PNG in src/ (ideally 512×512, transparent background), then run:
```bash
cd src
convert myicon.png -resize 256x256 \
  -define icon:auto-resize=16,32,48,64,128,256 \
  open-dash.ico
```
> Rebuild to embed.

## Source Code

```bash
src/open_dash.c
```

```c
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *tmpDir = getenv("TEMP");
    char flagPath[MAX_PATH];
    snprintf(flagPath, MAX_PATH, "%s\\minimized.flag", tmpDir);

    // First run → relaunch minimized with PowerShell (prevents console flash)
    if (GetFileAttributesA(flagPath) == INVALID_FILE_ATTRIBUTES) {
        FILE *f = fopen(flagPath, "w");
        if (f) fclose(f);

        char exePath[MAX_PATH];
        GetModuleFileNameA(NULL, exePath, MAX_PATH);

        char cmd[MAX_PATH + 200];
        snprintf(cmd, sizeof(cmd),
                 "powershell -windowstyle minimized -command \"Start-Process '%s'\"",
                 exePath);
        system(cmd);
        return 0;
    }

    // Second run (now headless): delete flag, then do the work
    DeleteFileA(flagPath);

    // 1) Ping gateway (adjust for current VLAN)
    system("ping 172.20.10.1");

    // 2) Allow services to settle
    Sleep(5000);

    // 3) Launch dashboard in Edge (adjust URL)
    system("start msedge.exe http://172.20.10.30:8000/");

    return 0;
}
```

```bash
src/icon.rc
```

```Plaintext
// Embed the application icon into the EXE
IDI_ICON1 ICON "open-dash.ico"
```

```bash
build.sh
```

```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/src"

# Compile resources and link a GUI app (no console window)
x86_64-w64-mingw32-windres icon.rc -O coff -o icon.res
x86_64-w64-mingw32-gcc open_dash.c icon.res -o ../open-dash.exe -mwindows -s

echo "[+] Built $(cd .. && pwd)/open-dash.exe"
```

> How It Works (brief)

On first launch, the EXE creates a temp flag and uses:

powershell -windowstyle minimized -command "Start-Process 'open-dash.exe'"


to relaunch itself minimized (no console flash).

On the second run, it removes the flag, pings the gateway, waits, then opens the dashboard URL.

Future Work (extension ideas)

Config/INI + environment variable overrides (no recompile).

Auto-detect VLAN (10.x vs 172.20.x) and choose URL automatically.

Add version metadata in icon.rc (FileVersion/ProductVersion).

Replace system("start ...") with ShellExecuteA for default-browser launch.
