import graph as gr

x=gr.graph()
x.addVertex(6)

x.addEdge(0,1,False,1)
x.addEdge(0,0,False,1)
x.addEdge(0,2,False,1)
x.addEdge(1,3,False,1)
x.addEdge(2,3,False,1)
x.addEdge(4,5,True,1)

print "Checking Traverse: "
print "Test 1 expected output: [[0, 1, 2, 3], [4, 5]]\nTest 1 output:         ",x.traverse(None,True)
print "Test 2 expected output: [[0, 2, 3, 1], [4, 5]]\nTest 2 output:         ",x.traverse(None,False)
print "Test 3 expected output: [4, 5]\nTest 3 output:         ",x.traverse(4,False)
print "Test 4 expected output: [0, 2, 3, 1]\nTest 4 output:         ",x.traverse(0,False)
print "Done checking traverse \n  \n"

print "Checking connectivity: "
print "Test 1 expected output: [True, False]\nTest 1 output:         ",x.connectivity(4,5)
print "Test 2 expected output: [True, True]\nTest 2 output:         ",x.connectivity(0,2)
print "Test 3 expected output: [True, True]\nTest 3 output:         ",x.connectivity(0,3)
print "Done checking connectivity \n \n"

print "Checking path: "
print "Test 1 expected output: [[1, 0, 2], [2, 0, 1]]\nTest 1 output:         ",x.path(1,2)
print "Test 1 alt output:      [[1, 3, 2], [2, 3, 1]]"
print "Test 2 expected output: [[4, 5], []]\nTest 2 output:         ",x.path(4,5)
print "Test 3 expected output: [[0, 1, 3], [3, 1, 0]]\nTest 3 output:         ",x.path(0,3)

print "Done checking!\nAuto-tester by Devansh Ranade"