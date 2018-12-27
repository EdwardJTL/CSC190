from sortlib import *

v1=[10,9,8,7,6,5,4,3,2,1,0]
v2=[100,1,1000,9,8,7,2,2000,10]
v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

for i in [v1, v2, v3]:
   x=list(i)
   selection_sort(x)
   print x

   x=list(i)
   heapify(x)
   print x

   x=list(i)
   heap_sort(x)
   print x

   x=list(i)
   merge_sort(x)
   print x

   x=list(i)
   quick_sort(x,0,len(x)-1)
   print x