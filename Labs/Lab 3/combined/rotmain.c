#include <stdio.h>
#include <stdlib.h>
#include "avlrot.c"

int main(void) {
  avlNode* tree = NULL;
  avlNode* tree2 = NULL;
  avlNode* tree3 = NULL;
  addNonAvl(&tree,3);
  addNonAvl(&tree,1);
  addNonAvl(&tree,18);
  addNonAvl(&tree,19);
  addNonAvl(&tree,11);
  addNonAvl(&tree,8);
  a_printTreeInOrder(tree);
  a_printLevelOrder(tree);
  printf("%d\n", getDepth(&tree));
  printf("%d\n", isAVL(&tree));
  printf("minor right, major left\n");
  dblrotate(&tree,0);
  a_printTreeInOrder(tree);
  a_printLevelOrder(tree);
  printf("%d\n", getDepth(&tree));
  printf("%d\n", isAVL(&tree));
  /*tree 2*/
  printf("tree 2\n");
  addNonAvl(&tree2,16);
  addNonAvl(&tree2,10);
  addNonAvl(&tree2,18);
  addNonAvl(&tree2,8);
  addNonAvl(&tree2,12);
  addNonAvl(&tree2,13);
  a_printTreeInOrder(tree2);
  a_printLevelOrder(tree2);
  printf("%d\n", getDepth(&tree2));
  printf("%d\n", isAVL(&tree2));
  printf("minor left, major right\n");
  dblrotate(&tree2,1);
  a_printTreeInOrder(tree2);
  a_printLevelOrder(tree2);
  printf("%d\n", getDepth(&tree2));
  printf("%d\n", isAVL(&tree2));
  addNonAvl(&tree3,16);
  addNonAvl(&tree3,13);
  addNonAvl(&tree3,18);
  addNonAvl(&tree3,19);
  printf("tree 3\n");
  a_printTreeInOrder(tree3);
  a_printLevelOrder(tree3);
  printf("tree 3 rotate left\n");
  rotate(&tree3,0);
  a_printTreeInOrder(tree3);
  a_printLevelOrder(tree3);
  printf("tree 3 rotate right\n");
  rotate(&tree3,1);
  a_printTreeInOrder(tree3);
  a_printLevelOrder(tree3);
  return 0;
}
