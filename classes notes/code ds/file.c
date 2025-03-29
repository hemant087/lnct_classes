#include <stdio.h>

int main() {
    int a = 10;
    if ((a > 10) || (a++)) {
        printf("%d", a);
    }
    return 0;
}
