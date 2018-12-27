#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_tail(llnode **x,char value);
int llnode_print_from_head(llnode *x);
int llnode_print_from_tail(llnode *x);
int llnode_add_to_head(llnode **x,char value);
int llnode_del_from_head(llnode**x);
int push(llnode **x, char value);
int pop(llnode **x, char *return_value);
int cmp(const char *a, const char *b);


int main(void) {
   int n=0;
   char value;
   char store;
   int rvalue=0;
   llnode *bracket_list=NULL;

   while (scanf("%c",&value) != EOF) {
      if ((value == '(')||(value == '[')||(value == '{')){
        rvalue = push(&bracket_list,value);
      }
      else if((value == ')')||(value == ']')||(value == '}')){
        if (bracket_list==NULL) {
          printf("FAIL,%d\n", n);
          return 0;
        }else {
          rvalue = pop(&bracket_list,&store);
          if (((value==')')&&(store!='('))||((value==']')&&(store!='['))||((value=='}')&&(store!='{'))) {
            printf("FAIL,%d\n", n);
            return 0;
          }
        }
      }
    n=n+1;
    }
   if (bracket_list==NULL) {
     printf("PASS\n");
   }
   else{
     printf("FAIL,%d\n", n);
   }
   return 0;
}

int llnode_add_to_head(llnode **x,char value) {
  if (x==NULL){return -1;}
  else{
    llnode *old = NULL;
    old = *x;
    *x = (llnode *)malloc(sizeof(llnode));
    (*x)->value = value;
    (*x)->next = old;
    return 0;
  }
}

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_del_from_head(llnode**x){
    if (x==NULL){
        return -1;
    }
    if (*x == NULL) {
        return -1;
    }else{
        llnode *pfirst = *x;
        *x = (*x)->next;
        free(pfirst);
        return 0;
    }
}

int push(llnode **x, char value){
  int rvalue=-1;
  rvalue = llnode_add_to_head(x,value);
  return rvalue;
}

int pop(llnode **x, char *return_value){
  if ((x==NULL)||(return_value==NULL)) { return -1; }
  else{
    int rvalue=-1;
    *return_value = (*x)->value;
    rvalue = llnode_del_from_head(x);
    return rvalue;
  }
}

int cmp(const char *a, const char *b){
  for(;*a == *b;a++, b++);
  if (*(unsigned char *)a<*(unsigned char *)b) {
    return -1;
  }else {
    return 1;
  }
}
