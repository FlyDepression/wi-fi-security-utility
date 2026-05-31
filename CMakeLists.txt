cmake_minimum_required(VERSION 3.10)
project(wi-fi-security-utility)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads REQUIRED)

add_executable(wifi_security_utility
    src/main.cpp
    src/wifi_scanner.cpp
    src/wifi_scanner.h
    src/packet_capture.cpp
    src/packet_capture.h
)

target_link_libraries(wifi_security_utility PRIVATE
    Threads::Threads
    pcap
)