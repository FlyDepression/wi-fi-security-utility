#ifndef WIFI_SCANNER_H
#define WIFI_SCANNER_H

#include <vector>
#include <string>

struct WiFiNetwork {
    std::string ssid;
    std::string bssid;
    int signal_strength;
    std::string security;
};

void scan_wifi_networks();

#endif