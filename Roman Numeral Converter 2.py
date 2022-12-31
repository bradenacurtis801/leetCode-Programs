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
        try:
		if val not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
    			raise ValueError
		elif tempDict[input[index+1]] > tempDict[val] and [tempDict[input[index+1]] > tempDict[val] for val in input[index+2:]]:
			decimalVal += tempDict[input[index+1]] - tempDict[input[index]]
		elif tempDict[input[index-1]] > tempDict[input[index]]:
			decimalVal += tempDict[index]
        except IndexError:
      
            



roman_decimal('CMI')			