#include "../common.h"
#include <iostream>

#define Board vector<vector<int>>

#define BOARD_SIZE 5

using namespace std;

Board replace_in_board(Board board, int n)
{
    for (int x = 0; x < BOARD_SIZE; x++) {
        for (int y = 0; y < BOARD_SIZE; y++) {
            if (board[x][y] == n) {
                board[x][y] = 0;
            }
        }
    }
    return board;
}

bool check_win(Board board)
{
    for (int x = 0; x < BOARD_SIZE; x++) {
        int sum = 0;
        for (int n : board[x])
            sum += n;
        if (sum == 0)
            return true;
    }

    for (int y = 0; y < BOARD_SIZE; y++) {
        int sum = 0;
        for(int x=0;x<BOARD_SIZE;x++)
            sum += board[x][y];
        if (sum == 0)
            return true;
    }

    return false;
}

int sum_board(Board board)
{
    int sum = 0;
    for(vector<int> line : board) {
        for(int e : line) {
            sum += e;
        }
    }
    return sum;
}

int main()
{
    ifstream fp("input.txt");

    string nums_raw;
    getline(fp, nums_raw);
    vector<string> nums = split(nums_raw, ",");

    int num;
    vector<Board> boards;
    while (!fp.eof()) {
        Board board;

        for (int i = 0; i < BOARD_SIZE; i++) {
            vector<int> line;
            for (int j = 0; j < BOARD_SIZE; j++) {
                fp >> num;
                line.push_back(num);
            }
            board.push_back(line);
        }
        boards.push_back(board);
    }
    boards.pop_back();

    for (string sn : nums) {
        int n = stoi(sn);
        for (int i = 0; i < boards.size(); i++) {
            boards[i] = replace_in_board(boards[i], n);

            if (check_win(boards[i])) {
                cout << sum_board(boards[i]) * n << "\n";
                return 0;
            }
        }
    }
}