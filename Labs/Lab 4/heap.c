#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

struct llnode{
  int val;
  struct llnode *pnext;
};
typedef struct llnode ll;

int initHeap (HeapType *pHeap,int size);
int inorder  (HeapType *pHeap, int **output, int *o_size);
int preorder (HeapType *pHeap, int **output, int *o_size);
int postorder(HeapType *pHeap, int **output, int *o_size);
int addHeap(HeapType *pHeap, int key);
int findHeap(HeapType *pHeap, int key);
int delHeap(HeapType *pHeap, int *key);
int power(int base, int exp);
int fakeadd(HeapType *pHeap, int item);
int printArray(HeapType *pHeap);
int inorder_help(HeapType *pHeap, ll**root, int id);
int preorder_help(HeapType *pHeap, ll**root, int id);
int postorder_help(HeapType *pHeap, ll**root, int id);
int ll_add(ll**root, int item);
int ll_print( ll *p);
int converter(int **output, ll *list, int size);
int swap(HeapType *pHeap, int index_a, int index_b);
int getParent(int child);
int childCompare(HeapType* pHeap, int index);/*return index of bigger child; return -1 if out of end/size*/
int findHeap_helper(HeapType *pHeap, int key, int index);

int initHeap (HeapType *pHeap,int size){
  if ((pHeap == NULL)||(size < 1)) {
    return -1;
  }
  else{
    int i = 0;
    pHeap->size = size;
    pHeap->end = 0;
    pHeap->store = (int *)malloc(sizeof(int)*size);
    for (i=0;i<size;i++){
      pHeap->store[i] = 0;
    }
    return 0;
  }
}

int addHeap(HeapType *pHeap, int key){
  if (pHeap == NULL) {
    return -1;
  }if (pHeap->store == NULL) {
    return -1;
  }else{
    int index = pHeap->end;
    int parent = getParent(index);
    if (index <= pHeap->size) {
      pHeap->store[index] = key;
      pHeap->end += 1;
      while (pHeap->store[index] > pHeap->store[parent]) {
        swap(pHeap, index, parent);
        index = parent;
        parent = getParent(index);
      }
    }
    return 0;
  }
}

int swap(HeapType *pHeap, int index_a, int index_b){
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

int findHeap(HeapType *pHeap, int key){
  /*
   -1 for error (not okay)
   0 for okay: not found
   1 for okay: found
   */
  if (pHeap == NULL) {
    return -1;
  }if (pHeap->store == NULL) {
    return -1;
  }else{
    return findHeap_helper(pHeap, key, 0);
  }
}

int findHeap_helper(HeapType *pHeap, int key, int index){
  if (pHeap->store[index] == key) {
    return 1;
  }if (pHeap->store[index] < key) {
    return 0;
  }else{
    int lchild = 0;
    int rchild = 0;
    int ls = 0;
    int rs = 0;
    lchild = 2*index+1;
    rchild = 2*index+2;
    if (lchild<(pHeap->end)) {
      ls = findHeap_helper(pHeap, key, lchild);
    }
    if (rchild<(pHeap->end)) {
      rs = findHeap_helper(pHeap, key, rchild);
    }
    if ((ls == 1)||(rs == 1)) {
      return 1;
    }else{
      return 0;
    }
  }
}


int delHeap(HeapType *pHeap, int *key){
  if ((pHeap == NULL)||(key == NULL)) {
    return -1;
  }if (pHeap->store == NULL) {
    return -1;
  }if (pHeap->end == 0) {
    return -1;
  }else{
    int child = 0, index = 0;
    *key = pHeap->store[0];
    child = childCompare(pHeap, 0);
    while (child != -1) {
      pHeap->store[index] = pHeap->store[child];
      index = child;
      child = childCompare(pHeap, index);
    }
    pHeap->end -=1;
    return 0;
  }
}

int childCompare(HeapType* pHeap, int index){
  if (pHeap == NULL) {
    return -1;
  }if (pHeap->store == NULL) {
    return -1;
  }else{
    int lchild = index*2+1;
    int rchild = index*2+2;
    int s1 = 0, s2 = 0, lval = 0, rval = 0;
    if (lchild < pHeap->end) {
      s1 = 1;
      lval = pHeap->store[lchild];
    }
    if (rchild < pHeap->end) {
      s2 = 1;
      rval = pHeap->store[rchild];
    }
    if ((s1==0)&&(s2==0)) {
      return -1;
    }if ((s1==1)&&(s2==0)) {
      return lchild;
    }if ((s1==0)&&(s2==1)) {
      return rchild;
    }else{
      if (lval>rval) {
        return lchild;
      }else{
        return rchild;
      }
    }
  }
}

int inorder  (HeapType *pHeap, int **output, int *o_size){
  if ((pHeap == NULL)||(output == NULL)||(o_size==NULL)) {
    return -1;
  }
  if (pHeap->store == NULL) {
    return -1;
  }else{
    ll* l = NULL;
    *o_size = pHeap->end;
    inorder_help(pHeap, &l, 0);
    converter(output, l, *o_size);
  }
  return 0;
}

int inorder_help(HeapType *pHeap, ll**root, int id){
  if (root == NULL) {
    return -1;
  }else{
    int size = pHeap->end;
    int left = 2*id+1;
    int right = 2*id+2;
    int item;
    item = pHeap->store[id];
    if (left<size) {
      inorder_help(pHeap, root, left);
    }
    ll_add(root, item);
    if (right<size) {
      inorder_help(pHeap, root, right);
    }
    return 0;
  }
}

int preorder  (HeapType *pHeap, int **output, int *o_size){
  if ((pHeap == NULL)||(output == NULL)||(o_size==NULL)) {
    return -1;
  }
  if (pHeap->store == NULL) {
    return -1;
  }else{
    ll* l = NULL;
    *o_size = pHeap->end;
    preorder_help(pHeap, &l, 0);
    converter(output, l, *o_size);
  }
  return 0;
}

int preorder_help(HeapType *pHeap, ll**root, int id){
  if (root == NULL) {
    return -1;
  }else{
    int size = pHeap->end;
    int left = 2*id+1;
    int right = 2*id+2;
    int item;
    item = pHeap->store[id];
    ll_add(root, item);
    if (left<size) {
      preorder_help(pHeap, root, left);
    }
    if (right<size) {
      preorder_help(pHeap, root, right);
    }
    return 0;
  }
}

int postorder  (HeapType *pHeap, int **output, int *o_size){
  if ((pHeap == NULL)||(output == NULL)||(o_size==NULL)) {
    return -1;
  }
  if (pHeap->store == NULL) {
    return -1;
  }else{
    ll* l = NULL;
    *o_size = pHeap->end;
    postorder_help(pHeap, &l, 0);
    converter(output, l, *o_size);
  }
  return 0;
}

int postorder_help(HeapType *pHeap, ll**root, int id){
  if (root == NULL) {
    return -1;
  }else{
    int size = pHeap->end;
    int left = 2*id+1;
    int right = 2*id+2;
    int item;
    item = pHeap->store[id];
    if (left<size) {
      postorder_help(pHeap, root, left);
    }
    if (right<size) {
      postorder_help(pHeap, root, right);
    }
    ll_add(root, item);
    return 0;
  }
}

int ll_add(ll**head, int item){
  if (head == NULL) {
     return -1;
  }
  if (*head == NULL) {
     *head = ( ll *) malloc(sizeof(ll));
     (*head) -> val = item;
     (*head) -> pnext = NULL;
     return 0;
  } else {
     return ll_add(&((*head)->pnext), item);
  }
}

int ll_free( ll *p) {
   if (p==NULL) {
      return -1;
   } else {
       ll *f=p->pnext;
      free(p);
      return ll_free(f);
   }
}

int converter(int **output, ll *list, int size){
  if (list==NULL) {
    return -1;
  }else{
    int value, i = 0;
    ll *p = list;
    *output = (int *)malloc(sizeof(int)*size);
    for (i=0;i<size;i++){
      value = p->val;
      (*output)[i] = value;
      p = p->pnext;
    }
    ll_free(list);
    return 0;
  }
}

int ll_print( ll *p) {
   if (p==NULL) {
      return 0;
   } else {
      printf("val = %d\n",p->val);
      return ll_print(p->pnext);
   }
}

int fakeadd(HeapType *pHeap, int item){
  pHeap->store[pHeap->end] = item;
  pHeap->end += 1;
  return 0;
}

int printArray(HeapType *pHeap){
  int i = 0;
  for (i=0;i<pHeap -> end;i++){
    printf("%d ", pHeap->store[i]);
  }
  printf("\n");
  return 0;
}

int power(int base, int exp){
  int i = 0;
  int r = 1;
  for (i=0;i<exp;r*=base,i++);
  return r;
}


int getParent(int child){
  if (child <= 0) {
    return 0;
  }else{
    int parent = 0;
    if (child % 2 == 1) {
      parent = (child-1)/2;
    }else{
      parent = (child/2)-1;
    }
    return parent;
  }
}
