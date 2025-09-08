#!/usr/bin/env python3
# topology_anim.py - curses-based ASCII animation
# Usage: python3 topology_anim.py
import curses, time

BOX_RV = (1, 22)
BOX_EAST = (7, 8)
BOX_WEST = (13, 42)

def draw_box(stdscr, y, x, w, h, title_lines):
    stdscr.addstr(y, x, "+" + "-"*(w-2) + "+")
    for i in range(1, h-1):
        stdscr.addstr(y+i, x, "|")
        stdscr.addstr(y+i, x+w-1, "|")
    stdscr.addstr(y+h-1, x, "+" + "-"*(w-2) + "+")
    for i, line in enumerate(title_lines):
        stdscr.addstr(y+1+i, x+2, line[:w-4])

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)
    phase = 0

    while True:
        stdscr.erase()

        draw_box(stdscr, BOX_RV[0], BOX_RV[1], 24, 5, [
            "Cisco RV340 Router",
            "GW 172.20.10.254"
        ])
        draw_box(stdscr, BOX_EAST[0], BOX_EAST[1], 22, 6, [
            "East 3560 Switch",
            "Gi0/1 Trk to West",
            "Fa0/1 Trk to RV340"
        ])
        draw_box(stdscr, BOX_WEST[0], BOX_WEST[1], 22, 6, [
            "West 3560 Switch",
            "Gi0/1 Trk to East",
            "Fa0/8 -> WLC (V10)"
        ])
        stdscr.addstr(19, 10, "VLAN10: 172.20.10.0/24 (DHCP on RV340)")
        stdscr.addstr(21, 42, "Native VLAN 999 on all trunks")

        stdscr.addstr(6, 33, "|")
        stdscr.addstr(7, 34, "───────┐")
        stdscr.addstr(12, 28, "───────────────┐")
        stdscr.addstr(13, 44, "│")
        stdscr.addstr(14, 44, "│")
        stdscr.addstr(15, 44, "│")

        if phase % 2 == 0:
            stdscr.addstr(19, 10, "VLAN10: 172.20.10.0/24 (DHCP on RV340)", curses.A_REVERSE)
            stdscr.addstr(21, 42, "Native VLAN 999 on all trunks", curses.A_REVERSE)

        col = 30 + (phase % 8)
        stdscr.addstr(7, col, "●")
        col2 = 28 + (phase % 15)
        stdscr.addstr(12, col2, "◈")
        row3 = 13 + (phase % 4)
        stdscr.addstr(row3, 44, "◆")

        stdscr.refresh()
        phase += 1
        time.sleep(0.12)

        try:
            ch = stdscr.getch()
            if ch in (ord('q'), 27):
                break
        except curses.error:
            pass

if __name__ == "__main__":
    curses.wrapper(main)
