#!/usr/bin/env bash
# Simple blinking WEST banner for terminal recordings
trap 'tput cnorm; tput sgr0; echo' EXIT
tput civis

BOLD=$(tput bold 2>/dev/null || echo "")
RED=$(tput setaf 1 2>/dev/null || echo "")
GRN=$(tput setaf 2 2>/dev/null || echo "")
YEL=$(tput setaf 3 2>/dev/null || echo "")
CYN=$(tput setaf 6 2>/dev/null || echo "")
RST=$(tput sgr0 2>/dev/null || echo "")

while :; do
  clear
  echo -e "${BOLD}${CYN}=================  WEST 3560 SWITCH  =================${RST}"
  echo -e "${BOLD}${GRN}Gi0/1 Trunk → East   ${RST}|  Native: ${YEL}VLAN 999${RST}  |  Allowed: ${YEL}10,999${RST}"
  echo -e "${BOLD}${GRN}Fa0/8  → WLC (VLAN10)${RST} |  Fa0/3 → AP (VLAN10, PoE)${RST}"
  echo
  echo -e "${BOLD}${YEL}TIP:${RST} If you still see a native mismatch, mirror the SAME native on EAST."
  sleep 0.6
  echo -e "${BOLD}${RED}REMINDER:${RST} Disable BPDU Guard on trunks. Enable it only on access ports."
  sleep 0.6
done
