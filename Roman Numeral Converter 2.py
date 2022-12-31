def roman_decimal(input):
    input = input.upper()
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
            elif index < len(input) -1 and tempDict[input[index+1]] > tempDict[val]:
                if all([tempDict[input[index+1]] > tempDict[val] for val in input[index+2:]]) and all([tempDict[input[index + 1]] <= tempDict[val] for val in input[:index]]):
                    decimalVal += tempDict[input[index+1]] - tempDict[input[index]]
                else:
                    raise ValueError
            elif index == 0 or tempDict[input[index - 1]] >= tempDict[val]:
                decimalVal += tempDict[val]
        except IndexError:
            continue
    return decimalVal


print(roman_decimal('xcix'))
