#ifndef PACKET_CAPTURE_H
#define PACKET_CAPTURE_H

#include <string>

void start_packet_capture();
void process_packet(const unsigned char* packet, int length);

#endif