def printInfo():
	print("DFA1 - by x86coder")
	print("Regular language to be recognized: a*b")
	print("(zero or more a's followed by one b)")
	print(" > Input your string/word: ", end="")
	
Q = [0, 1, 2, 3]	# Finite set of states (Q)
S = ['a', 'b']		# Input alphabet (sigma)
s = 0				# Initial state
d = [[1,2], [1,2], [3, 3], [3, 3]]	# Delta function f(x) (multidimensional array)
					# 	values = [[state0], [state1], [state2], [[index for 'a', index for 'b']] ... [state N]]
F = [2]				# Set of acception states (python list object)

character_map = {'a' : 0, 'b' : 1}	# Python dictionary mapping to second-level array indexes

printInfo()
mystring = input()
word = list(mystring)	# Input string to the DFA (with each character separated)

# Run DFA continously until input is consumed
i = 0		# Loop control variable
q = s		# DFA current state
while i < len(mystring):
	secondary_index = character_map[word[i]]
	#print("\t* secondary_index: " + str(secondary_index))
	new_state = d[q][secondary_index] # Access transition pair in set Q x S. Old/current state is in q.
	q = new_state
	i = i+1
	
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
	print("> String was not accepted (X)!")