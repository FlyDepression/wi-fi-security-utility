"""Utility functions for Wi-Fi security operations."""

import socket
import struct
import sys

def check_root():
    """Check if running as root (required for raw sockets)."""
    if sys.platform.startswith("linux") or sys.platform == "darwin":
        import os
        if os.geteuid() != 0:
            print("[!] This tool requires root privileges.")
            sys.exit(1)
    else:
        print("[!] Unsupported OS. Use Linux/macOS with root.")
        sys.exit(1)

def get_default_iface():
    """Get default wireless interface (simplified)."""
    import subprocess
    try:
        result = subprocess.run(["iwconfig"], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if "IEEE 802.11" in line:
                return line.split()[0]
    except:
        pass
    return "wlan0mon"

def mac_to_bytes(mac_str):
    """Convert MAC address string to bytes."""
    return bytes.fromhex(mac_str.replace(":", ""))

def bytes_to_mac(mac_bytes):
    """Convert bytes to MAC string."""
    return ":".join(f"{b:02x}" for b in mac_bytes)

if __name__ == "__main__":
    check_root()
    print(f"Default interface: {get_default_iface()}")