"""
lab2.py
Bridget Franciscovich
1/30/2018
"""
def squared_nums(num_list):
	"""
	Squares numbers in num_list
	num_list: list of numbers
	Returns: list of these numbers squared
	"""
	result = [ ] # initialize list to hold result
	#iterate through num_list and square each element
	for num in num_list:
		#num = pow(num, 2)
		num = num ** 2
		result.append(num)
	return result

def check_title(title_list):
	"""
	Removes strings in the title_list that have numbers and aren't title case
	title_list: list of strings
	Returns: list of strings that are titles
	"""
	result = [ ]
	for title in title_list:
		if title.istitle():
			result.append(title)
	return result



