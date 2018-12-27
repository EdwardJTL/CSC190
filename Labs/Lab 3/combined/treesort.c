#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

struct qNode_bst {
   bstNode *pval;
   struct qNode_bst *nxt;
};
typedef struct qNode_bst bNode;

int add_bst(bstNode **root,int val);
int addNonAvl(avlNode **root,int val);
int printTreeInOrder(bstNode *root);
int push(bNode **root,bstNode *node);
int pop(bNode **root,bstNode** r_node);
int printLevelOrder(bstNode *root);
int a_printLevelOrder(avlNode *root);
int a_printTreeInOrder(avlNode *root);
int a_push(qNode **root,avlNode *node);
int a_pop(qNode **root,avlNode** r_node);
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1);


int main(void) {
    int value = 0;
    int rvalue = 0;
    bstNode* tree = NULL;

    while (scanf("%d", &value) != EOF) {
      add_bst(&tree, value);
    }
    rvalue = printTreeInOrder(tree);
    if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }
    return 0;
}

int add_bst(bstNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (bstNode*)malloc(sizeof(bstNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      return 0;
   } else {
     int rvalue = -1;
      if ((*root)->val > val){
        rvalue = add_bst(&((*root)->l), val);
      }
      else if((*root)->val < val){
        rvalue = add_bst(&((*root)->r), val);
      }else if ((*root)->val == val) {
        return 0;
      }
      return rvalue;
   }
}

int addNonAvl(avlNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (avlNode*)malloc(sizeof(avlNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      return 0;
   } else {
     int rvalue = -1;
      if ((*root)->val > val){
        rvalue = addNonAvl(&((*root)->l), val);
      }
      else if((*root)->val < val){
        rvalue = addNonAvl(&((*root)->r), val);
      }
      return rvalue;
   }
}

int printTreeInOrder(bstNode *root){
  int rvalue;
  if (root == NULL) {
    return -1;
  }
  if (root->l != NULL) {
    rvalue = printTreeInOrder(root->l);
  }
  printf("%d\n", root->val);
  if (root->r != NULL) {
    rvalue = printTreeInOrder(root->r);
  }
  return 0;
}

int push(bNode **root,bstNode *node){
  if ((root == NULL)||(node == NULL)) {
    return -1;
  }else if (*root == NULL) {
    *root = (bNode *)malloc(sizeof(bNode));
    (*root)->pval = node;
    (*root)->nxt = NULL;
  }else{
    return push(&((*root)->nxt),node);
  }
  return 0;
}

int pop(bNode **root,bstNode** r_node){
  if ((root == NULL)||(r_node == NULL)) {
    return -1;
  }else if(*root != NULL){
    bNode* temp_nxt;
    *r_node = (*root)->pval;
    temp_nxt = (*root)->nxt;
    free (*root);
    *root = temp_nxt;}
    return 0;
}

int printLevelOrder(bstNode *root){
  int rvalue;
  bNode* queue = NULL;
  if (root == NULL) {
    return -1;
  }else {
    rvalue = push(&queue,root);
    while (queue != NULL) {
      bstNode* item = NULL;
      rvalue = pop(&queue, &item);
      if (rvalue != -1) {
        printf("%d ", item->val);
        rvalue = push(&queue,item->l);
        rvalue = push(&queue,item->r);
      }
    }
  }
  printf("\n");
  return 0;
}

int a_printLevelOrder(avlNode *root){
  int rvalue;
  qNode* queue = NULL;
  if (root == NULL) {
    return -1;
  }else {
    rvalue = a_push(&queue,root);
    while (queue != NULL) {
      avlNode* item = NULL;
      rvalue = a_pop(&queue, &item);
      if (rvalue != -1) {
        printf("%d ", item->val);
        rvalue = a_push(&queue,item->l);
        rvalue = a_push(&queue,item->r);
      }
    }
  }
  printf("\n");
  return 0;
}

int a_pop(qNode **root,avlNode** r_node){
  if ((root == NULL)||(r_node == NULL)) {
    return -1;
  }else if(*root != NULL){
    qNode* temp_nxt;
    *r_node = (*root)->pval;
    temp_nxt = (*root)->nxt;
    free (*root);
    *root = temp_nxt;}
    return 0;
}

int a_push(qNode **root,avlNode *node){
  if ((root == NULL)||(node == NULL)) {
    return -1;
  }else if (*root == NULL) {
    *root = (qNode *)malloc(sizeof(qNode));
    (*root)->pval = node;
    (*root)->nxt = NULL;
  }else{
    return a_push(&((*root)->nxt),node);
  }
  return 0;
}

int a_printTreeInOrder(avlNode *root){
  int rvalue;
  if (root == NULL) {
    return -1;
  }
  if (root->l != NULL) {
    rvalue = a_printTreeInOrder(root->l);
  }
  printf("%d\n", root->val);
  if (root->r != NULL) {
    rvalue = a_printTreeInOrder(root->r);
  }
  return 0;
}
