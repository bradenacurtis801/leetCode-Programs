def roman_decimal(input):
	decimalVal = 0
	tempDict = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	
	for index, val in enumerate(input):
		if val not in ['I','V','X','L','C','D','M']:
			raise ValueError
		elif tempDict[input[index+1]] > val and [tempDict[input[index+1]] > val for val in tempDict[input[index+2:-1]]]
			