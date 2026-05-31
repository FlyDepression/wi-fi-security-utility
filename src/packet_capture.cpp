#include "packet_capture.h"
#include <iostream>
#include <pcap.h>

void start_packet_capture() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_if_t* alldevs;
    pcap_if_t* d;

    if (pcap_findalldevs(&alldevs, errbuf) == -1) {
        std::cerr << "Error finding devices: " << errbuf << "\n";
        return;
    }

    std::cout << "Available interfaces:\n";
    for (d = alldevs; d; d = d->next) {
        std::cout << d->name << "\n";
    }

    std::cout << "Enter interface name: ";
    std::string iface;
    std::cin >> iface;

    pcap_t* handle = pcap_open_live(iface.c_str(), BUFSIZ, 1, 1000, errbuf);
    if (handle == nullptr) {
        std::cerr << "Couldn't open device " << iface << ": " << errbuf << "\n";
        return;
    }

    std::cout << "Starting packet capture (Ctrl+C to stop)...\n";
    pcap_loop(handle, 0, [](unsigned char* user, const struct pcap_pkthdr* h, const unsigned char* bytes) {
        process_packet(bytes, h->len);
    }, nullptr);

    pcap_close(handle);
}

void process_packet(const unsigned char* packet, int length) {
    static int count = 0;
    std::cout << "Packet #" << ++count << " (" << length << " bytes)\n";
    // In a real tool, you would parse Wi-Fi headers here
}