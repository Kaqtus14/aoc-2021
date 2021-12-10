#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ifstream fp("input.txt");

    vector<int> data;
    int line;
    while (fp >> line) {
        data.push_back(line);
    }

    int count = 0;
    for (int i = 1; i < data.size() - 2; i++) {
        if ((data[i - 2] + data[i - 1] + data[i]) <
            (data[i - 1] + data[i] + data[i + 1])) {
            count++;
        }
    }
    cout << count << "\n";

    return 0;
}