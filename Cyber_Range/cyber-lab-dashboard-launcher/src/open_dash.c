#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *tmpDir = getenv("TEMP");
    char flagPath[MAX_PATH];
    snprintf(flagPath, MAX_PATH, "%s\\minimized.flag", tmpDir);

    // First run → relaunch minimized with PowerShell
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

    // Second run → delete flag, then do work silently
    DeleteFileA(flagPath);

    // 1) Silent ping to VLAN1 gateway
    system("ping 192.168.0.1");

    // 2) Wait a few seconds for services
    Sleep(3000);

    // 3) Launch browser to VLAN1 dashboard
    system("start msedge.exe http://192.168.0.50/");

    return 0;
}
