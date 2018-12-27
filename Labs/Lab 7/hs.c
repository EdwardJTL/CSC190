#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
} intHeap_T;

int store(intHeap_T* heap,int value);
int retrieve(intHeap_T* heap,int *rvalue);
int swap(intHeap_T *pHeap, int index_a, int index_b);
int getParent(int n);

int store(intHeap_T* heap,int value) {
  if (heap == NULL) {
    return -1;
  }if (heap->store == NULL) {
    return -1;
  }if (heap->compare == NULL) {
    return -1;
  }else{
    int index = heap->end;
    int parent = getParent(index);
    if (index <= heap->size) {
      heap->store[index] = value;
      heap->end += 1;
      while (heap->compare(heap->store[parent], heap->store[index]) == 1) {
        swap(heap, index, parent);
        index = parent;
        parent = getParent(index);
      }
    }
    return 0;
  }
}

int retrieve(intHeap_T* heap,int *rvalue) {
  if ((heap == NULL)||(rvalue == NULL)) {
    return -1;
  }if (heap->store == NULL) {
    return -1;
  }if (heap->end == 0) {
    return -1;
  }if (heap->compare == NULL) {
    return -1;
  }else{
    int child = 0, index = 0, moving = 1;
    int rc = 0, lc = 0;
    *rvalue = heap->store[0];
    heap->store[0] = heap->store[heap->end-1];
    heap->end -= 1;
    while (moving == 1) {
      moving = 0;
      lc = index * 2 + 1;
      rc = index * 2 + 2;
      if (lc < heap->end) {
        int swap_child = lc;
        if (rc < heap -> end){
          if (heap->compare(heap->store[lc], heap->store[rc])) {
            swap_child = rc;
          }
        }
        if (heap->compare(heap->store[index], heap->store[swap_child])) {
              swap(heap, index, swap_child);
              index = swap_child;
              moving = 1;
        }
      }
    }
    return 0;
  }
}

int swap(intHeap_T *pHeap, int index_a, int index_b){
  if (pHeap == NULL) {
    return -1;
  }if (pHeap->store == NULL) {
    return -1;
  }if ((index_a<0)||(index_a > pHeap->size)) {
    return -1;
  }if ((index_b<0)||(index_b > pHeap->size)) {
    return -1;
  }else{
    int holder;
    holder = pHeap->store[index_a];
    pHeap->store[index_a] = pHeap->store[index_b];
    pHeap->store[index_b] = holder;
    return 0;
  }
}

int getParent(int n){
  return ((int) (n-1)/2);
}

int hs(int *x,int size,int (*compare)(int x,int y)) {
  intHeap_T heap;
  heap.store = (int *)malloc(size*sizeof(int));
  heap.size = size;
  heap.end = 0;
  heap.compare = compare;
  if (x == NULL) {
    return -1;
  }else{
    int i;
    for (i = 0; i < size; i++) {
      store(&heap, x[i]);
    }
    for (i = 0; i < size; i++) {
      retrieve(&heap, &(x[i]));
    }
  }
  free(heap.store);
  return 0;
}
