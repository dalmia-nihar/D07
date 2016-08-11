# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def is_sorted(imp_lst):
	return imp_lst == sorted(imp_lst)


def main(): 
	print(is_sorted(["b","h","a","aa"]))
	print(is_sorted(["a","b","c","z"]))


if __name__ == '__main__':
	main()

