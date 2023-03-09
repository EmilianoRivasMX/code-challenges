/*
Write a function int max_of_four(int a, int b, int c, int d) 
which returns the maximum of the four arguments it receives.
*/

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
    int numbers[4] = {a, b, c, d};
    
    // Sol 1: Using sort function
    // sort(numbers, numbers + 4);
    // return numbers[3];

    // Sol 2: Using bubble algorithm
    int aux;
    for (int i = 0; i < 4; i++) {
        for (int j = i+1; j < 4; j++) {
            if (numbers[i] < numbers[j]) {
                aux = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = aux;
            }
        }
    }
    return numbers[0];
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}