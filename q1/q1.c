#include <stdio.h>

int main(){
    int prev =0;
    int curr =0;
    int count = 0;
    printf("Starting scan\n");
    while(scanf("%d", &curr) > 0){
        if(prev){
            count += curr > prev ? 1 : 0;
        }
        prev = curr;
    }
    printf("%d\n", count);
    return 0;
}