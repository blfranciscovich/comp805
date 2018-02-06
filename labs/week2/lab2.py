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

#def squared_nums_2(num_list):
	"""
	Squares numbers in num_list
	num_list: list of numbers
	Returns: list of these numbers squared

	I added this because I did this last semester to include negative squared numbers
	"""
#	result = [ ]
#	for num in num_list:
#		if num > 0:
#			num = num ** 2
#			result.append(num)
#		else:
#			num = num ** 2 * -1
#			result.append(num)
#	return result

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

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictonary by 10
	inventory: a dictionary with:
		key: string that is ther name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	"""
	for key, value in inventory.items(): #iteritems
		inventory[key] = value + 10
	return (inventory)

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed
	"""
	for key in list(inventory.keys()):
		if inventory[key] == 0:
			del inventory[key]
	return (inventory)

def average_grades(grades):
	"""
	Takes grade values from a dictionary and averages them into a final grade
	grades: a dictionary of grades with:
	key: string of students name
	value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student
	"""
	for key, value in grades.items():
		grades[key] = sum(value) / float(len(value))
	return (grades)

