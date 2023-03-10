/*
Given an integer n do the following:
- If 1 <= n <= 9, print the lowercase number. For example, for 1 print "one"
- If n > 9, print "Greater than 9"
*/

#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    if (n > 9) {
        cout << "Greater than 9" << endl;
    } else {
        cout << numbers[n-1];
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
