#include <stdio.h>
#include <stdlib.h>

int bs(int *x,int size,int (*compare)(int x,int y)) {
    if (size<1) {
        return -1;
    }
    if (x == NULL) {
        return -1;
    }
    else{
      int n = size;
      int swapping = 0;
      while (swapping == 0){
          int swapped = 0;
          int i;
          for (i=1;i<n;i+=1){
              if ((*compare)(x[i-1],x[i]) == 1) {
                  int temp = x[i-1];
                  x[i-1] = x[i];
                  x[i] = temp;
                  swapped = 1;
              }
          }
          n = n-1;
          if (swapped == 0){
              swapping = 1;
          }
      }
  }
    return 0;
}

int lt(int x,int y){
  if(x<y){
    return 1;
  }else{return 0;}
}

int gt(int x,int y){
  if(x>y){
    return 1;
  }else{return 0;}
}
