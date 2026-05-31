"""Passive Wi-Fi network scanner using Scapy."""

import time
from scapy.all import sniff, Dot11, Dot11Beacon, Dot11ProbeResp
from collections import defaultdict
import threading

class WiFiScanner:
    """Scans for nearby Wi-Fi networks passively."""

    def __init__(self, iface="wlan0mon"):
        self.iface = iface
        self.networks = defaultdict(lambda: {"ssid": "", "bssid": "", "channel": 0, "signal": 0, "encryption": ""})
        self._stop_event = threading.Event()

    def _handle_packet(self, pkt):
        if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
            bssid = pkt[Dot11].addr2
            ssid = pkt[Dot11].info.decode("utf-8", errors="ignore") if pkt[Dot11].info else "<Hidden>"
            try:
                channel = int(ord(pkt[Dot11Beacon if pkt.haslayer(Dot11Beacon) else Dot11ProbeResp].network_stats().get("channel", 0)))
            except:
                channel = 0
            signal = pkt.dBm_AntSignal if hasattr(pkt, "dBm_AntSignal") else -100
            encryption = pkt.sprintf("%Dot11Beacon.cap%") if pkt.haslayer(Dot11Beacon) else "Unknown"

            self.networks[bssid] = {
                "ssid": ssid,
                "bssid": bssid,
                "channel": channel,
                "signal": signal,
                "encryption": encryption
            }

    def start_scan(self, timeout=10):
        """Start passive scanning for `timeout` seconds."""
        print(f"[*] Scanning on {self.iface} for {timeout}s...")
        sniff(iface=self.iface, prn=self._handle_packet, store=False, timeout=timeout)

    def get_networks(self):
        """Return list of discovered networks."""
        return list(self.networks.values())

    def list_networks(self):
        """Print discovered networks."""
        for net in self.get_networks():
            print(f"  SSID: {net['ssid']:20} BSSID: {net['bssid']:17} Ch: {net['channel']:2} Signal: {net['signal']:4} dBm  Enc: {net['encryption']}")

if __name__ == "__main__":
    scanner = WiFiScanner()
    scanner.start_scan(timeout=5)
    scanner.list_networks()