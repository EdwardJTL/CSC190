#include <stdio.h>
#include <stdlib.h>
/*bstNode, add_bst, bNode, pop, push are a set*/
/*avlNode, addNonAvl, qNode, a_pop, a_push are a set*/

/*int main(void) {
  bstNode *root=NULL;
  add_bst(&root,5);
  add_bst(&root,3);
  add_bst(&root,1);
  add_bst(&root,4);
  add_bst(&root,7);
  add_bst(&root,6);
  add_bst(&root,8);
  printTreeInOrder(root);
  printLevelOrder(root);
  return 0;
}*/

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
