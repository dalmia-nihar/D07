# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def capitalize_nested(lst):
	cap_list = []
	for incr in lst:
		if type(incr) == list:
			cap_list.append(capitalize_nested(incr))
		else:
			cap_list.append(incr.upper())
	return cap_list

def main(): 
	print(capitalize_nested(['apple', ['bear'], 'cat']))
	print(capitalize_nested(['apple', ['mims', ['UC','Berkeley'], 'bears'], 'cat']))
	print(capitalize_nested(['apple', 'bear', 'cat']))

if __name__ == '__main__':
	main()

