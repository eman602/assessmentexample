	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
	new_item =input.lower()
	eg = new_item[-1]
	ey= new_item[-2]
	
	if eg=='y' and ey=='p':
		return True
	return False

print(endsPy("pyiscool"))

## second method of finding answer
def  checking(input):
	word = 'py'
	if word in input:
		return True
	return False

print(checking("hhhpy"))