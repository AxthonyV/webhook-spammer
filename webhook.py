import requests
import time
import os
from pystyle import Colors, Colorate, Center

# Colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"

logo = """

 ___       __   _______   ________  ___  ___  ________  ________  ___  __       
|\\  \\     |\\  \\|\\  ___ \\ |\\   __  \\|\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\     
\\ \\  \\    \\ \\  \\ \\   __/|\\ \\  \\|\\ /\\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|_   
 \\ \\  \\  __\\ \\  \\ \\  \\_|/_\\ \\   __  \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\  
  \\ \\  \\|\\__\\_\\  \\ \\  \\_|\\ \\ \\  \\|\\  \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\ 
   \\ \\____________\\ \\_______\\ \\_______\\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\
    \\|____________|\\|_______|\\|_______|\\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|
                                                                                

                [+] Webhook Tool [+]                          GitHub: @AxthonyV
"""

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_menu(webhook_name):
    print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "\n[1] Spam Webhook", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "[2] Delete Webhook", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "\nSelect an option (1-2): ", 1))
    print(f"\n\n{green}[+] Logged into webhook: {webhook_name}{white}")

def delete_webhook(url):
    try:
        response = requests.delete(url)
        if response.status_code == 204:
            print(f"\n{green}[✓] Webhook successfully deleted{white}")
        else:
            print(f"\n{red}[✗] Error deleting webhook{white}")
    except Exception as e:
        print(f"\n{red}[✗] Error: {str(e)}{white}")
    time.sleep(2)

def spam_webhook(url):
    try:
        message = input(f"\n{yellow}[?] Spam message: {white}")
        delay = float(input(f"{yellow}[?] Delay between messages (seconds): {white}"))
        amount = int(input(f"{yellow}[?] Number of messages (0 for infinite): {white}"))
        
        count = 0
        print(f"\n{cyan}[+] Starting spam... (Press Ctrl+C to stop){white}")
        
        while True:
            response = requests.post(url, json={"content": message})
            if response.status_code == 204:
                count += 1
                print(f"{green}[✓] Message sent ({count}){white}")
            else:
                print(f"{red}[✗] Error sending message{white}")
                
            if amount > 0 and count >= amount:
                break
                
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print(f"\n\n{yellow}[!] Spam stopped by user{white}")
    except Exception as e:
        print(f"\n{red}[✗] Error: {str(e)}{white}")
    
    time.sleep(2)

def main():
    while True:
        clear()
        print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))
        url = input(f"{cyan}[>] Enter webhook URL: {white}")
        
        # Verify webhook and get information
        try:
            response = requests.get(url)
            if response.status_code == 200:
                webhook_info = response.json()
                webhook_name = webhook_info.get("name", "Unknown")
            else:
                print(f"\n{red}[✗] Invalid webhook{white}")
                time.sleep(2)
                continue
        except:
            print(f"\n{red}[✗] Invalid URL{white}")
            time.sleep(2)
            continue
            
        while True:
            clear()
            print_menu(webhook_name)
            try:
                option = input(f"{cyan}[>] {white}").strip()
                
                if option == "1":
                    spam_webhook(url)
                elif option == "2":
                    delete_webhook(url)
                    break  # Return to start after deletion
                else:
                    print(f"\n{red}[✗] Invalid option{white}")
                    time.sleep(1)
            except KeyboardInterrupt:
                clear()
                print(f"\n{yellow}[!] Exiting...{white}")
                return

if __name__ == "__main__":
    main()