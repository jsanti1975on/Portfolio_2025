#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/src"

x86_64-w64-mingw32-windres icon.rc -O coff -o icon.res
x86_64-w64-mingw32-gcc open_dash.c icon.res -o ../open-dash.exe -mwindows -s

echo "[+] Built $(cd .. && pwd)/open-dash.exe"
