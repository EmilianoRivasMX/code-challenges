/*
Recieve two positive integers a and b (a <= b) and for each n in the inclusive interval [a,b]:
- If  1 <= n <= 9, then print the enlish lowercase representation of the number.
- Else if n > 9 and its an event number, then print "even".
- Else if n > 9 and its an odd number, then print "odd".
*/

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int a, b;
    string numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    scanf("%d\n%d", &a, &b);
    for (int i = a; i <= b; i++) {
        if (i > 9) {
            if (i % 2 == 0) {
                cout << "even" << endl;
            } else {
                cout << "odd" << endl;
            }
        } else {
            cout << numbers[i-1] << endl;
        }
    }
    return 0;
}