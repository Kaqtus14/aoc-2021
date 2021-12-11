#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>

#include "../common.h"

using namespace std;

map<char, int> SCORES = {{')', 1}, {']', 2}, {'}', 3}, {'>', 4}};
map<char, char> BRACKETS = {{'(', ')'}, {'[', ']'}, {'{', '}'}, {'<', '>'}};

vector<char> process_line(string line) {
    vector<char> expected;

    for (auto c : line) {
        if (BRACKETS.count(c)) {
            expected.push_back(BRACKETS[c]);
        } else {
            if (expected.back() != c) {
                return {};
            }
            expected.pop_back();
        }
    }
    return expected;
}

int main() {
    ifstream fp("input.txt");

    string line;
    vector<long> scores;

    while (fp >> line) {
        long score = 0;
        vector<char> expected = process_line(line);
        if (expected.size() == 0) {
            continue;
        }
        reverse(expected.begin(), expected.end());

        for (auto e : expected) {
            score *= 5;
            score += SCORES[e];
        }
        scores.push_back(score);
    }

    cout << fixed;  // dont use scientific notation
    cout << median(scores) << "\n";
    return 0;
}