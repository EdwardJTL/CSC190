for i in $(cat test.txt) ; do echo $i | ./a.out ; done
for i in $(cat test.txt) ; do echo $i | python test.py ; done

