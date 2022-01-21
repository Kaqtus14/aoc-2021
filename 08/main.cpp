#include "../common.h"
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fp("input.txt");
    vector<string> lines = read_lines(fp);

    int out = 0;

    for(string line : lines) {
        line.erase(0, line.find(" | ")+3);

        for(string word : split(line, " ")) {
            int l = word.length();
            if((l==2) || (l==3) || (l==4) || (l==7)) {
                out++;
            }
        }
    }
    cout << out << "\n";
}