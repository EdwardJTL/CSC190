// #include "heap.c"
#include "bs.c"
#include "hs.c"

int main(void){
  int i,j,rval;
  int vals[] = {10,5,7,4,1,3,6,2,0,8};
  // intHeap_T heap;
  // heap.store=(int *)malloc(1000*sizeof(int));
  // heap.size=1000;
  // heap.end=0; /* empty heap condition; obey this spec */
  // heap.compare = lt; /* assuming lt was defined as in part A */
  // for (j = 0; j < 9; j++) {
  //   printf("adding %d\n", vals[j]);
  //   store(&heap, vals[j]);
  //   for (i = 0; i < heap.end; i++){
  //     printf("%d, ", heap.store[i]);
  //   }
  //   printf("\n");
  // }
  // retrieve(&heap, &rval);
  // for (i = 0; i < heap.end; i++){
  //   printf("%d, ", heap.store[i]);
  // }
  // printf("\n");
  // free(heap.store);
  bs(vals, 10, lt);
  for (i = 0; i < 10; i++){
    printf("%d, ", vals[i]);
  }
  printf("\n");
  bs(vals, 10, gt);
  for (i = 0; i < 10; i++){
    printf("%d, ", vals[i]);
  }
  printf("\n");
  rval = hs(vals, 10, lt);
    for (i = 0; i < 10; i++){
    printf("%d, ", vals[i]);
  }
  printf("\n");
  rval = hs(vals, 10, gt);
    for (i = 0; i < 10; i++){
    printf("%d, ", vals[i]);
  }
  printf("\n");
  return 0;
}
