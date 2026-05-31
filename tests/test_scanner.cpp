#include "../src/wifi_scanner.h"
#include <cassert>

void test_scan_output() {
    // This would be more comprehensive in a real test
    std::cout << "Running scanner tests...\n";
    scan_wifi_networks();  // Just verify it runs without crashing
    std::cout << "Scanner test passed.\n";
}

int main() {
    test_scan_output();
    return 0;
}