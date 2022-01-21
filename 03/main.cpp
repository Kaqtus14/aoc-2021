#include "../common.h"
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ifstream fp("input.txt");
    vector<string> lines = read_lines(fp);

    string gamma, epsilon;
    for (int i = 0; i < lines[0].length(); i++) {
        int ones = 0, zeros = 0;

        for (int j = 0; j < lines.size(); j++) {
            if (lines[j][i] == '0')
                zeros++;
            else
                ones++;
        }

        if (ones > zeros) {
            gamma += "1";
            epsilon += "0";
        } else {
            gamma += "0";
            epsilon += "1";
        }
    }

    cout << stoi(gamma, 0, 2) * stoi(epsilon, 0, 2) << "\n";
}