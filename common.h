#include <bits/stdc++.h>

#include <iostream>
#include <vector>

template <typename T>
void print_vector(std::vector<T> v)
{
    std::cout << "[";
    for (auto e : v) {
        std::cout << e << " ";
    }
    std::cout << "]\n";
}

float mean(std::vector<int> v)
{
    float sum = 0;
    for (auto e : v) {
        sum += e;
    }
    return sum / (float)v.size();
}

// https://stackoverflow.com/questions/1719070/what-is-the-right-approach-when-using-stl-container-for-median-calculation/1719155#1719155
long median(std::vector<long> v)
{
    size_t n = v.size() / 2;
    nth_element(v.begin(), v.begin() + n, v.end());
    return v[n];
}

std::vector<std::string> read_lines(std::ifstream& fp)
{
    std::vector<std::string> out;
    std::string line;
    while (getline(fp, line)) {
        out.push_back(line);
    }
    return out;
}

std::vector<std::string> split(std::string s, std::string delim)
{
    std::vector<std::string> out;

    while(true) {
        size_t pos = s.find(delim);
        if(pos == std::string::npos) {
            out.push_back(s);
            return out;
        }

        out.push_back(s.substr(0, pos));
        s.erase(0, pos+delim.length());
    }
}

std::vector<int> read_ints(std::ifstream& fp)
{
    std::vector<int> out;
    int line;
    while (fp >> line) {
        out.push_back(line);
    }
    return out;
}

std::vector<int> read_ints_comma(std::ifstream& fp)
{
    std::vector<int> out;
    int line;
    while (fp >> line) {
        out.push_back(line);
        fp.ignore();
    }
    return out;
}