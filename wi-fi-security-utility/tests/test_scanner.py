"""Unit tests for WiFiScanner."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.scanner import WiFiScanner
from unittest.mock import patch, MagicMock

def test_network_discovery():
    """Test that scanner processes packets correctly."""
    scanner = WiFiScanner(iface="test0")
    
    # Mock a beacon packet
    mock_pkt = MagicMock()
    mock_pkt.haslayer.side_effect = lambda x: x.__name__ in ["Dot11Beacon"]
    mock_pkt[Dot11].addr2 = "00:11:22:33:44:55"
    mock_pkt[Dot11].info = b"TestNetwork"
    mock_pkt.dBm_AntSignal = -45
    mock_pkt.sprintf.return_value = "privacy"

    scanner._handle_packet(mock_pkt)
    networks = scanner.get_networks()
    
    assert len(networks) == 1
    assert networks[0]["ssid"] == "TestNetwork"
    assert networks[0]["bssid"] == "00:11:22:33:44:55"
    assert networks[0]["signal"] == -45
    print("[+] test_network_discovery passed!")

if __name__ == "__main__":
    test_network_discovery()