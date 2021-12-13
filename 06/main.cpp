#include "../common.h"
#include <iostream>
#include <map>

using namespace std;

typedef map<int, unsigned long> fc;

fc count_fish(vector<int> data)
{
    fc fish;

    for (auto f : data)
        fish[f]++;

    return fish;
}

unsigned long sum_fish(fc fish)
{
    unsigned long sum = 0;

    for (auto pair : fish)
        sum += pair.second; // i love c++

    return sum;
}

fc day(fc fish)
{
    fc new_fish;
    for (int i = 0; i <= 9; i++)
        new_fish[i] = 0;

    for (auto pair : fish) {
        if (pair.first == 0) {
            new_fish[6] += pair.second;
            new_fish[8] += pair.second;
        } else {
            new_fish[pair.first - 1] += pair.second;
        }
    }
    return new_fish;
}

int main()
{
    ifstream fp("input.txt");
    auto data = read_ints_comma(fp);
    auto fish = count_fish(data);

    for (int i = 0; i < 256; i++)
        fish = day(fish);

    cout << sum_fish(fish) << "\n";
}