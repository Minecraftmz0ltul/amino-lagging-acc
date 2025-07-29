import subprocess
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def print_menu():
    clear()
    print(Fore.BLUE + "=" * 50)
    print(Fore.MAGENTA + Style.BRIGHT + f"{'🔥 LAG MODE LAUNCHER 🔥':^50}")
    print(Fore.BLUE + "=" * 50)
    print()
    print(Fore.YELLOW + "  [1] 🐢 Lag Mode")
    print(Fore.GREEN + "  [2] ⚡ No Lag Mode")
    print(Fore.RED + "  [Q] ❌ Quit")
    print()

def main():
    while True:
        print_menu()
        choice = input(Fore.CYAN + "\nPick your mode (1/2/Q): ").strip().lower()

        if choice == "1":
            slow_print(Fore.YELLOW + "\n[+] Running lag.py 🐌")
            subprocess.run(["python", "lag.py"])
            break
        elif choice == "2":
            slow_print(Fore.GREEN + "\n[+] Running no.lag.py ⚡")
            subprocess.run(["python", "no.lag.py"])
            break
        elif choice == "q":
            slow_print(Fore.RED + "\n[!] Peace out gamer 👋")
            break
        else:
            slow_print(Fore.RED + "\nInvalid option, bro. Try again 😭")

if __name__ == "__main__":
    main()
