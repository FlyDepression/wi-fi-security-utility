#include <iostream>
#include "wifi_scanner.h"
#include "packet_capture.h"

int main() {
    std::cout << "Wi-Fi Security Utility v0.1 (Ethical Use Only)\n";
    std::cout << "1. Scan nearby networks\n";
    std::cout << "2. Capture packets (monitor mode required)\n";
    std::cout << "Select option: ";

    int choice;
    std::cin >> choice;

    if (choice == 1) {
        scan_wifi_networks();
    } else if (choice == 2) {
        start_packet_capture();
    } else {
        std::cout << "Invalid option.\n";
    }

    return 0;
}