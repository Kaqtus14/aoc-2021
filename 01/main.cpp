#include <fstream>
#include <iostream>
#include <vector>

#include "../common.h"

using namespace std;

int main() {
    ifstream fp("input.txt");
    vector<int> data = read_ints(fp);

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