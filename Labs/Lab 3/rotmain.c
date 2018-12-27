#include "avlrot.c"


int main(void) {
  avlNode* tree = NULL;
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
  avlNode* tree2 = NULL;
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
  return 0;
}
