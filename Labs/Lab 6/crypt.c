#include <stdio.h>

unsigned char FSR(unsigned char x);
unsigned char prng(unsigned char x, unsigned char pattern);
int crypt(char *data,unsigned int size,unsigned char password);

unsigned char prng(unsigned char x, unsigned char pattern){
  return FSR(x) ^ pattern;
}

int crypt(char *data,unsigned int size,unsigned char password){
  int i;
  unsigned char prngVal = password;
  if ((size <= 1) || (password == 0)){
    return -1;
  }
  for (i=0;i<size;i++){
    prngVal = prng(prngVal, 0xb8);
    data[i] = data[i] ^ prngVal;
  }
  return 0;
}

unsigned char FSR(unsigned char x){
   unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
   unsigned char r = x >> 1;        /* shift right   */
   unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
   r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
   return r;
}
