#include <stdio.h>

unsigned int rot_soln(unsigned int x, int n){
  unsigned int accum = x;
  unsigned int shift_out;
  int i = 0;
  if (n>0){
    for (i = 0; i < n; i++) {
      shift_out = (~accum >> 31) & 0x1;
      accum = accum << 1;
      accum = accum | shift_out;
    }
  }else if (n<0) {
    for (i = 0; i < -n; i++) {
      shift_out = ~accum & 0x1;
      accum = accum >> 1;
      accum = accum | (shift_out << 31);}
  }else{
    accum = ((x>>16)&0xffff)^(x&0xffff);
  }
  return accum;
}

unsigned int rot(unsigned int x, int n){
  if (n>0) {
    unsigned int a, b;
    int c;
    a = 0x1;
    for (c=0;c<n;c++){
      a = a<<1;
      b= 0x1;
      a = a|b;}
    a = a<<(32-n);
    b = x & a;
    b = b>>(32-n);
    a = a>>(32-n);
    b = b^a;
    x = x<<n;
    x = x|b;
  } else if (n<0) {
    unsigned int a, b;
    int c;
    a = 0x1;
    for(c=0;c<-n;c++){
      a = a<<1;
      b = 0x1;
      a = a|b;}
    b = x&a;
    b = b^a;
    b = b<<(32+n);
    x = x >> (-n);
    x = x|b;
  }else{
    unsigned int btm, top;
    btm = 0xFFFF;
    top = 0xFFFF0000;
    btm = x & btm;
    top = (x&top)>>16;
    x = btm^top;
  }
  return x;
}

int main(void) {
  unsigned int i;
  printf("Solution:\n");
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,1),1 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,2),2 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,3),3 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,4),4 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,-1),-1 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,-2),-2 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,-3),-3 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,-4),-4 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot_soln(i,0),0 );
  i = 0xaaaa5555; printf("%08x %08x n=%d\n",i,rot_soln(i,0),0 );
  /**/
  printf("My code:\n");
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,1),1 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,2),2 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,3),3 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,4),4 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,-1),-1 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,-2),-2 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,-3),-3 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,-4),-4 );
  i = 0xaaaaaaaa; printf("%08x %08x n=%d\n",i,rot(i,0),0 );
  i = 0xaaaa5555; printf("%08x %08x n=%d\n",i,rot(i,0),0 );
  return 0;
}
