def printInfo():
	print("DFA Sample 1 - by x86coder")
	print(" > Input your string to be recognized:")
	
Q = [0, 1, 2]		# Finite set of states
S = ['a', 'b']		# Input alphabet
s = 0			# Initial state
d = {'a' : 3, 'b' : 2}	# Delta function f(x)
F = [1, 2]		# Set of acception states (python list object)

printInfo()
mystring = input()
word = list(mystring)	# Input string to the DFA (with each character separated)

# Run DFA continously until input is consumed
i = 0		# Loop control variable
q = s		# DFA current state
while i < len(mystring):
	#print(d[word[i]])
	q = d[word[i]]
	i = i +1
	
print("> Ending state is: q" + str(q))

# Validate if the ending state is of acception
k = 0
accepted = False
while k < len(F):
	if q == F[k]:
		accepted = True
	k = k + 1

# Just to handle output message
if accepted:
	print("> String is accepted!")
else:
	print("> String was not accepted!")