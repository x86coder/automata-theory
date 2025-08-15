def printInfo():
	print("DFA1 - example")
	print(" > Input your string to be recognized:")
	
	
S = ['a', 'b']
s = 0
A = [1, 2]
d = {'a' : 3, 'b' : 2}

printInfo()
mystring = input()
word = list(mystring)

i = 0		# Loop control variable
q = 0		# Initial state
while i < len(mystring):
	#print(d[word[i]])
	
	q = d[word[i]]
	i = i +1
	
print("> Ending state is: q" + str(q))

k = 0
accepted = False
while k < len(A):
	if q == A[k]:
		accepted = True
	k = k + 1
	
if accepted:
	print("> String is accepted!")
else:
	print("> String was not accepted!")