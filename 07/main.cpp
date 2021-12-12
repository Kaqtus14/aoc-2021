#include <fstream>
#include <iostream>
#include <vector>

#include "../common.h"

using namespace std;

int get_spent_fuel(int target, vector<int> data)
{
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

int main()
{
    ifstream fp("input.txt");
    vector<int> data = read_ints_comma(fp);

    cout << mean(data) << "\n";
    cout << get_spent_fuel(mean(data), data) << "\n";

    return 0;
}