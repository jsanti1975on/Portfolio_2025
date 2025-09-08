#!/usr/bin/env bash
# topology_anim.sh - ANSI/ASCII animation for terminal recordings
# Usage: chmod +x topology_anim.sh && ./topology_anim.sh
# Quit: Ctrl-C

set -euo pipefail

# Hide cursor on start, restore on exit
tput civis || true
cleanup(){ tput cnorm || true; tput sgr0 || true; echo; }
trap cleanup EXIT

# Colors
BOLD=$(tput bold 2>/dev/null || echo "")
RESET=$(tput sgr0 2>/dev/null || echo "")
GREEN=$(tput setaf 2 2>/dev/null || echo "")
CYAN=$(tput setaf 6 2>/dev/null || echo "")
YELLOW=$(tput setaf 3 2>/dev/null || echo "")
MAGENTA=$(tput setaf 5 2>/dev/null || echo "")

ORIGIN_ROW=2
ORIGIN_COL=4
cursor(){ printf "\033[%d;%dH" "$1" "$2"; }

clear

draw_static(){
  cursor $((ORIGIN_ROW+0)) $((ORIGIN_COL+20)); echo "${BOLD}${CYAN}+----------------------+${RESET}"
  cursor $((ORIGIN_ROW+1)) $((ORIGIN_COL+20)); echo "${BOLD}${CYAN}|  Cisco RV340 Router |${RESET}"
  cursor $((ORIGIN_ROW+2)) $((ORIGIN_COL+20)); echo "${BOLD}${CYAN}|  GW 172.20.10.254   |${RESET}"
  cursor $((ORIGIN_ROW+3)) $((ORIGIN_COL+20)); echo "${BOLD}${CYAN}+----------+-----------+${RESET}"

  cursor $((ORIGIN_ROW+6)) $((ORIGIN_COL+8));  echo "${BOLD}${GREEN}+--------------------+${RESET}"
  cursor $((ORIGIN_ROW+7)) $((ORIGIN_COL+8));  echo "${BOLD}${GREEN}|   East 3560 SW     |${RESET}"
  cursor $((ORIGIN_ROW+8)) $((ORIGIN_COL+8));  echo "${BOLD}${GREEN}| Gi0/1 ⇄ Trk to W   |${RESET}"
  cursor $((ORIGIN_ROW+9)) $((ORIGIN_COL+8));  echo "${BOLD}${GREEN}| Fa0/1 ⇄ Trk to RV  |${RESET}"
  cursor $((ORIGIN_ROW+10)) $((ORIGIN_COL+8)); echo "${BOLD}${GREEN}+---------+----------+${RESET}"

  cursor $((ORIGIN_ROW+12)) $((ORIGIN_COL+40)); echo "${BOLD}${GREEN}+--------------------+${RESET}"
  cursor $((ORIGIN_ROW+13)) $((ORIGIN_COL+40)); echo "${BOLD}${GREEN}|   West 3560 SW     |${RESET}"
  cursor $((ORIGIN_ROW+14)) $((ORIGIN_COL+40)); echo "${BOLD}${GREEN}| Gi0/1 ⇄ Trk to E   |${RESET}"
  cursor $((ORIGIN_ROW+15)) $((ORIGIN_COL+40)); echo "${BOLD}${GREEN}| Fa0/8 → WLC (V10)  |${RESET}"
  cursor $((ORIGIN_ROW+16)) $((ORIGIN_COL+40)); echo "${BOLD}${GREEN}| Fa0/3 → AP  (V10)  |${RESET}"
  cursor $((ORIGIN_ROW+17)) $((ORIGIN_COL+40)); echo "${BOLD}${GREEN}+---------+----------+${RESET}"

  cursor $((ORIGIN_ROW+18)) $((ORIGIN_COL+10)); echo "VLAN10: 172.20.10.0/24 (DHCP on RV340)"
  cursor $((ORIGIN_ROW+21)) $((ORIGIN_COL+40)); echo "Native VLAN 999 on all trunks"
}

draw_token(){ cursor "$1" "$2"; echo -en "$3"; }
blink_label(){ 
  local row=$1 col=$2 text=$3 phase=$4
  cursor "$row" "$col"
  if (( phase % 2 )); then echo -en "\033[7m${text}\033[0m"; else echo -en "${BOLD}${text}${RESET}"; fi
}

phase=0
while :; do
  clear
  draw_static
  blink_label $((ORIGIN_ROW+18)) $((ORIGIN_COL+10)) "VLAN10: 172.20.10.0/24 (DHCP on RV340)" "$phase"
  blink_label $((ORIGIN_ROW+21)) $((ORIGIN_COL+40)) "Native VLAN 999 on all trunks" "$phase"

  col=$((ORIGIN_COL+30 + (phase % 8)))
  draw_token $((ORIGIN_ROW+6)) "$col" "${YELLOW}●${RESET}"

  col2=$((ORIGIN_COL+28 + (phase % 15)))
  draw_token $((ORIGIN_ROW+11)) "$col2" "${CYAN}◈${RESET}"

  row3=$((ORIGIN_ROW+12 + (phase % 4)))
  draw_token "$row3" $((ORIGIN_COL+44)) "${MAGENTA}◆${RESET}"

  phase=$((phase+1))
  sleep 0.15
done
