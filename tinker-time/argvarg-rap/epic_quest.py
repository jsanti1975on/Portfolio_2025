import argparse
import time
import shutil

BANNER_LINES = [
    r"   ___      _               _                _             ",
    r"  / _ \ ___| |__   ___ _ __(_)_ __   __ _   / \   _ __ ___ ",
    r" / /_\/ _ \ '_ \ / _ \ '__| | '_ \ / _` | / _ \ | '__/ _ \\",
    r"/ /_\\  __/ |_) |  __/ |  | | | | | (_| |/ ___ \| | |  __/",
    r"\____/\___|_.__/ \___|_|  |_|_| |_|\__, /_/   \_\_|  \___|",
    r"                                   |___/                  ",
    r"        ARG, VARG, ARQ, VARQ – ARGUMENT PARSER"
]

def print_centered_banner():
    """Print the ASCII banner centered to the terminal width."""
    width = shutil.get_terminal_size((80, 20)).columns
    for line in BANNER_LINES:
        print(line.center(width))

def epic_print(text, delay=0.05):
    """Print text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    parser = argparse.ArgumentParser(
        description="Arg, varg, arq, varq – argument parser (Epic Adventure Edition)"
    )
    parser.add_argument("-n", "--name", help="Your hero name", required=True)
    parser.add_argument("-q", "--quest", help="Your quest objective", default="slay the bugs")
    parser.add_argument("-w", "--weapon", help="Your weapon of choice", default="keyboard")
    parser.add_argument("-d", "--difficulty", help="Difficulty level", choices=["easy", "hard"], default="hard")

    args = parser.parse_args()

    # Show banner centered
    print_centered_banner()
    time.sleep(1)

    epic_print(f"🏰 Welcome, {args.name}!")
    epic_print(f"Your quest: {args.quest}")
    epic_print(f"Armed with your trusty {args.weapon}, you embark on your journey...")

    time.sleep(1)
    if args.difficulty == "hard":
        epic_print("⚔️ Fierce enemies block your path!")
        time.sleep(1)
        epic_print("💥 You engage in battle...")
    else:
        epic_print("🐛 The bugs are weak and flee before you.")

    time.sleep(1)
    epic_print("✅ Quest complete! The terminal kingdom is safe once more.")

if __name__ == "__main__":
    main()
#  run it from the terminal with:
#  python epic_quest.py -n "YourHeroName" -q "Your Quest" -w "Your Weapon" -d hard
#  Example: python epic_quest.py -n "Lady Ava" -q "restore the server" -w "Python sword" -d hard
