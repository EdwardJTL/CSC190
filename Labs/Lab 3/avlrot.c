#include <stdio.h>
#include <stdlib.h>
#include "structsfuncs.h"
#include "structsfuncs.c"

int isAVL(avlNode **root);
int getDepth(avlNode **root);
int max(int a, int b);
int rotate(avlNode **root,unsigned int Left0_Right1);
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1);

int isAVL(avlNode **root){
  if (root == NULL) {
    return -1;
  }else{
    if (((*root)->l == NULL)&&((*root)->r == NULL)) {
      return 0;
    }else{
      int ldepth = 0;
      int rdepth = 0;
      int diff = 0;
      if ((*root)->l != NULL) {
        ldepth = getDepth (&((*root)->l));
      }if ((*root)->r != NULL) {
        rdepth = getDepth (&((*root)->r));
      }
      diff = ldepth - rdepth;
      if ((diff > 1)||(diff < -1)) {
        return -1;
      }
    }
    if ((*root)->l != NULL) {
      return isAVL(&((*root)->l));
    }if ((*root)->r != NULL) {
      return isAVL(&((*root)->r));
    }
    return 0;
  }
}

int getDepth(avlNode **root){
  if (root == NULL) {
    return -1;
  }
  int ldepth = 0;
  int rdepth = 0;
  int depth = 1;
  if ((*root)->l != NULL){
    ldepth = getDepth(&((*root)->l));
  }if ((*root)->r != NULL) {
    rdepth = getDepth(&((*root)->r));
  }
  depth += max(ldepth,rdepth);
  return depth;
}

int max(int a, int b){
  if (a>b) {
    return a;
  }else{
    return b;
  }
}

int rotate(avlNode **root,unsigned int Left0_Right1){
  /*which will rotate the tree defined by root+pivot in the direction
defined by Left0Right1 (if 0, go left; if 1 go right).

If you're rotating Right, where is the pivot relative to the root? left child
If you're rotating Left, where is the pivot relative to the root? right child*/
  avlNode* old_root = *root;
  avlNode* new_root = NULL;
  avlNode* move_node = NULL;
  if ((root == NULL)||(*root == NULL)) {
    return -1;
  }else if(Left0_Right1 == 1){ /*right rotation*/
    new_root = (*root)->l;
    if (new_root == NULL) {
      return -1;
    }
    move_node = new_root->r;
    new_root->r = old_root;
    old_root->l = move_node;
    *root = new_root;
  }else if (Left0_Right1 == 0) {/*left rotation*/
    new_root = (*root)->r;
    if (new_root == NULL) {
      return -1;
    }
    move_node = new_root->l;
    new_root->l = old_root;
    old_root->r = move_node;
    *root = new_root;
  }
  return 0;
}

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
  if ((root==NULL)||(*root==NULL)) {
    return -1;
  }if (MajLMinR0_MajRMinL1 == 0) {
    if ((*root)->r == NULL) {
      return -1;
    }
    rotate(&((*root)->r),1);
    rotate(root,0);
  }if (MajLMinR0_MajRMinL1 == 1) {
    if ((*root)->l == NULL) {
      return -1;
    }
    rotate(&((*root)->l),0);
    rotate(root,1);
  }
  return 0;
}
