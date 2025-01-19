import os
import time
import sys

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    os.system("cls" if os.name == 'nt' else 'clear')
    print("\033[1;33m██████╗ ███████╗██████╗ ██╗   ██╗████████╗    █████╗ ███╗   ██╗████████╗")
    print("\033[1;35m██╔══██╗╚════██║██╔══██╗██║   ██║╚══██╔══╝   ██╔══██╗████╗  ██║╚══██╔══╝")
    print("\033[1;36m██████╔╝█████╗██║██████╔╝██║   ██║   ██║     ███████║██╔██╗ ██║   ██║")
    print("\033[1;32m██╔═══╝ ██╔══╝██║██╔═══╝ ██║   ██║   ██║     ██╔══██║██║╚██╗██║   ██║")
    print("\033[1;34m██║     ███████╗██║██║     ╚██████╔╝   ██║     ██║  ██║██║ ╚████║   ██║")
    print("\033[1;31m╚═╝     ╚══════╝╚═╝╚═╝      ╚═════╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝")
    print("\033[1;33m==============================================================")
    print("\033[1;36m         Welcome To Tools DDOS HUNTER- REN-XPLOIT")
    print("\033[1;37m==============================================================\n")

def print_loading():
    loading = ['[          ]', '[=         ]', '[==        ]', '[===       ]', '[====      ]', '[=====     ]', '[======    ]', '[=======   ]', '[========  ]', '[========= ]', '[==========]']
    for frame in loading:
        sys.stdout.write(f"\r\033[1;32m{frame} Loading... Please wait.")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

def main_menu():
    clear()
    print_banner()
    print("\033[1;34m[1] HTTP Flood (ddosv1)")
    print("\033[1;34m[2] SYN Flood (ddosv2)")
    print("\033[1;34m[3] UDP Flood")
    print("\033[1;34m[4] ICMP Flood")
    print("\033[1;34m[5] Slowloris Attack")
    print("\033[1;34m[6] DNS Amplification")
    print("\033[1;34m[7] NTP Amplification")
    print("\033[1;34m[8] Memcached DDoS")
    print("\033[1;34m[9] Ping of Death")
    print("\033[1;34m[10] Smurf Attack")
    print("\033[1;31m[0] Exit")
    print("\033[1;37m")

def get_choice():
    choice = input("\033[1;37m\nEnter your choice: ")
    return choice

def process_choice(choice):
    if choice == '1':
        print("\033[1;32mRunning HTTP Flood (ddosv1)...")
        print_loading()
        os.system('python ddosv1.py')  # Using python instead of python3
    elif choice == '2':
        print("\033[1;32mRunning SYN Flood (ddosv2)...")
        print_loading()
        os.system('python ddosv2.py')  # Using python instead of python3
    elif choice == '3':
        print("\033[1;32mRunning UDP Flood...")
        # Call UDP Flood function here
    elif choice == '4':
        print("\033[1;32mRunning ICMP Flood...")
        # Call ICMP Flood function here
    elif choice == '5':
        print("\033[1;32mRunning Slowloris Attack...")
        # Call Slowloris function here
    elif choice == '6':
        print("\033[1;32mRunning DNS Amplification...")
        # Call DNS Amplification function here
    elif choice == '7':
        print("\033[1;32mRunning NTP Amplification...")
        # Call NTP Amplification function here
    elif choice == '8':
        print("\033[1;32mRunning Memcached DDoS...")
        # Call Memcached DDoS function here
    elif choice == '9':
        print("\033[1;32mRunning Ping of Death...")
        # Call Ping of Death function here
    elif choice == '10':
        print("\033[1;32mRunning Smurf Attack...")
        # Call Smurf Attack function here
    elif choice == '0':
        print("\033[1;31mExiting program...")
        time.sleep(1)
        exit()
    else:
        print("\033[1;31mInvalid choice! Please select a valid option.")
        time.sleep(2)

if __name__ == "__main__":
    while True:
        main_menu()
        choice = get_choice()
        process_choice(choice)
