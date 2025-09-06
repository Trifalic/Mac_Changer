import subprocess
import string
import random
import re
import argparse

def get_random_mac_address():
    """Generate a valid random MAC address."""
    first_byte = random.choice("02" "24" "26" "28" "2A" "2C" "2E" "30" "32" "34" "36" "38" "3A" "3C" "3E")
    mac = [first_byte + random.choice(string.hexdigits.upper())]

    for _ in range(5):
        mac.append(''.join(random.choices(string.hexdigits.upper(), k=2)))

    return ':'.join(mac)

def get_current_mac_address(iface):
    """Get current MAC address using 'ip link'."""
    output = subprocess.check_output(f"ip link show {iface}", shell=True, text=True)
    mac_search = re.search(r"link/ether (\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output)
    if mac_search:
        return mac_search.group(1)
    return None

def change_mac_address(iface, new_mac_address):
    """Change MAC address using 'ip' command."""
    subprocess.run(f"ip link set dev {iface} down", shell=True, check=True)
    subprocess.run(f"ip link set dev {iface} address {new_mac_address}", shell=True, check=True)
    subprocess.run(f"ip link set dev {iface} up", shell=True, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python MAC Address Changer for Linux")
    parser.add_argument("interface", help="Network interface name (e.g., eth0, wlan0)")
    parser.add_argument("-r", "--random", action="store_true", help="Generate a random MAC address")
    parser.add_argument("-m", "--mac", help="Specify a new MAC address to set")

    args = parser.parse_args()
    iface = args.interface

    if args.random:
        new_mac_address = get_random_mac_address()
    elif args.mac:
        new_mac_address = args.mac
    else:
        print("[-] Error: You must specify either --random or --mac <address>")
        exit(1)

    print(f"[*] Current MAC address: {get_current_mac_address(iface)}")
    print(f"[*] Changing MAC address to: {new_mac_address}")

    change_mac_address(iface, new_mac_address)

    updated_mac = get_current_mac_address(iface)
    print(f"[+] New MAC address: {updated_mac}")

    if updated_mac == new_mac_address:
        print("[✔️] MAC address changed successfully!")
    else:
        print("[❌] Failed to change MAC address.")
