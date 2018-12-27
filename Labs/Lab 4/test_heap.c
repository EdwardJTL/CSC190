#include "heap.c"

int main(void){
  HeapType* root = (HeapType *)malloc(sizeof(HeapType));
  HeapType* root2 = (HeapType *)malloc(sizeof(HeapType));
  HeapType* root3 = (HeapType *)malloc(sizeof(HeapType));
  int size = 50;
  int rvalue = 0;
  int i = 0;
  int o_size = 0;
  int *array = NULL;
  int popped = 0;
  /*testing init function*/
  rvalue = initHeap(root,size);
  rvalue = initHeap(root2,size);
  rvalue = initHeap(root3,size);
  printf("malloced, status: %d\n", rvalue);
  /*[end] testing init function*/
  /*testing getDepth and Fake Add*/
  printf("Testing Fake Add\n");
  for (i=9;i>0;i--){
  rvalue = fakeadd(root,i);
  printf("added %d, status: %d\n", i, rvalue);
  printf("end value is now %d\n",root->end);
  rvalue = printArray(root);
  printf("\n");
  }
  /*[end]testing getDepth and Fake Add*/
  /*testing in order function*/
  printf("Testing inorder\n");
  rvalue = inorder(root, &array, &o_size);
  printf("size:%d, status:%d\n",o_size,rvalue);
  for (i=0;i<o_size;i++){
    printf("%d ", array[i]);
  }
  printf("\n");
  free(array);
  /*[end]testing in order function*/
  /*testing in order function*/
  printf("Testing preorder\n");
  rvalue = preorder(root, &array, &o_size);
  printf("size:%d, status:%d\n",o_size,rvalue);
  for (i=0;i<o_size;i++){
    printf("%d ", array[i]);
  }
  printf("\n");
  free(array);
  /*[end]testing in order function*/
  /*testing in order function*/
  printf("Testing postorder\n");
  rvalue = postorder(root, &array, &o_size);
  printf("size:%d, status:%d\n",o_size,rvalue);
  for (i=0;i<o_size;i++){
    printf("%d ", array[i]);
  }
  printf("\n");
  free(array);
  /*[end]testing in order function*/
  /*testing addHeap*/
  printf("testing addHeap\n");
  for (i=10;i<=17;i++){
  rvalue = addHeap(root,i);
  printf("added %d, status: %d\n", i, rvalue);
  printf("end value is now %d\n",root->end);
  printf("printing array\n");
  rvalue = printArray(root);
  printf("printing inorder\n");
  rvalue = inorder(root, &array, &o_size);
  printf("size:%d, status:%d\n",o_size,rvalue);
  for (i=0;i<o_size;i++){
    printf("%d ", array[i]);
  }
  printf("\n");
  free(array);
  printf("\n");
  }
  /*[end]testing addHeap*/

  /*testing findHeap*/
  printf("testing findHeap\n");
  for (i=0;i<=20;i++){
    rvalue = findHeap(root, i);
    printf("looking for: %d, status: %d\n", i, rvalue);
  }

  printf("testing findHeap on root2\n");
  printf("adding nodes\n");
  for (i=13;i<=35;i++){
  rvalue = addHeap(root2,i);}
  printf("printing array\n");
  rvalue = printArray(root2);
  for (i=10;i<=15;i++){
    rvalue = findHeap(root2, i);
    printf("looking for: %d, status: %d\n", i, rvalue);
  }
  /*[end]testing findHeap*/
  /*testing delHeap*/
  printf("testing delHeap function on root\n");
  rvalue = delHeap(root, &popped);
  printf("status:%d, popped value: %d\n", rvalue,popped);
  printf("current array\n");
  rvalue = printArray(root);
  printf("inorder\n");
  rvalue = inorder(root, &array, &o_size);
  printf("size:%d, status:%d\n",o_size,rvalue);
  for (i=0;i<o_size;i++){
    printf("%d ", array[i]);
  }
  printf("\n");
  free(array);
  /*[end]testing delHeap*/
  /*gabe stuff*/
  printf("testing addHeap\n");
  for (i=0;i<=12;i+=1){
  rvalue = addHeap(root3,i);
  printf("added %d, status: %d\n", i, rvalue);
  printf("end value is now %d\n",root3->end);
  printf("printing array\n");
  rvalue = printArray(root3);
  printf("printing inorder\n");
  rvalue = inorder(root3, &array, &o_size);
  printf("size:%d, status:%d\n",o_size,rvalue);
  for (i=0;i<o_size;i++){
    printf("%d ", array[i]);
  }
  printf("\n");
  free(array);
  printf("\n");
  }
  /**/
  free(root);
  free(root2);
  printf("freed, status: %d\n", rvalue);
  return 0;
}
