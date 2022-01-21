#include "../common.h"
#include <fstream>
#include <iostream>

using namespace std;

int check(vector<string> data, int x, int y) {
    if((x > 0) && (data[x-1][y] <= data[x][y]))
        return -1;
    if((x < data.size()-1) && (data[x+1][y] <= data[x][y]))
        return -1;
    if((y > 0) && (data[x][y-1] <= data[x][y]))
        return -1;
    if((y < data[0].length()-1) && (data[x][y+1] <= data[x][y]))
        return -1;
    return data[x][y] - '0' + 1;
}

int main()
{
    ifstream fp("input.txt");
    vector<string> lines = read_lines(fp);
    int out = 0;

    for (int x = 0; x < lines.size(); x++) {
        for (int y = 0; y < lines[0].length(); y++) {
            int c = check(lines, x, y);
            if (c != -1) {
                out += c;
            }       
        }
    }
    cout << out << "\n";
}