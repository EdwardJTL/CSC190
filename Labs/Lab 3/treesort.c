#include <stdio.h>
#include <stdlib.h>
#include "structsfuncs.h"
#include "structsfuncs.c"

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
