# Author: the_4th_c1ph3r

from termcolor import colored
text = colored('--------------mac-gic by the4thc1ph3r--------------', 'red', attrs=['blink'])
print(text)

from colorama import Fore, Back, Style
import subprocess
import string
import random
import re

def get_random_mac_address():
    """
    Generate and return a MAC address in the format of Linux
    """
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

def get_current_mac_address(iface):
    """
    Get the current MAC address of the specified network interface
    using the 'ifconfig' command.
    """
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def change_mac_address(iface, new_mac_address):
    """
    Change the MAC address of the specified network interface.
    """
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_address}", shell=True)
    subprocess.check_output(f"ifconfig {iface} up", shell=True)

def main():
    network_interface = input("Enter the network interface (e.g., eth0 or wlan0): ")
    new_mac = get_random_mac_address()
    change_mac_address(network_interface, new_mac)
    print(f"MAC address successfully changed to: {Fore.RED +new_mac}")

if __name__ == "__main__":
    main()
