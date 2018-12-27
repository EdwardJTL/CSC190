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
