#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream fp("input.txt");

    int pos = 0, depth = 0, aim = 0;

    while (true) {
        string direction;
        int amount;

        if (!(fp >> direction)) {
            break;
        }
        fp >> amount;

        if (direction == "forward") {
            pos += amount;
            depth += amount * aim;
        } else if (direction == "up") {
            aim -= amount;
        } else if (direction == "down") {
            aim += amount;
        }
    }

    cout << pos * depth << "\n";
    return 0;
}