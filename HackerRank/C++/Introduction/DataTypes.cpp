/*
Recieve space-separated values: int, long, char, float, and double, respectively. 
Then print each one in a new line.

Note: The floating point value should be correct up to 3 decimal places 
and the double to 9 decimal places.
*/

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int i;
    long l;
    char c;
    float f;
    double d;

    scanf("%d %ld %c %f %lf", &i, &l, &c, &f, &d);
    printf("%d\n%ld\n%c\n%.3f\n%.9lf", i, l, c, f, d);
    return 0;
}