#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int get_spent_fuel(int target, vector<int> data) {
    int fuel = 0;

    for (int i = 0; i < data.size(); i++) {
        if (data[i] < target) {
            for (int j = 1; j <= target - data[i]; j++) {
                fuel += j;
            }
        } else if (data[i] > target) {
            for (int j = 1; j <= data[i] - target; j++) {
                fuel += j;
            }
        }
    }

    return fuel;
}

int mean(vector<int> data) {
    int sum = 0;
    for (int i = 0; i < data.size(); i++) {
        sum += data[i];
    }

    return (int)(sum / data.size());
}

int main() {
    ifstream fp("input.txt");

    vector<int> data;
    int line;
    while (fp >> line) {
        data.push_back(line);
        fp.ignore();
    }

    cout << mean(data) << "\n";
    cout << get_spent_fuel(mean(data), data) << "\n";

    return 0;
}