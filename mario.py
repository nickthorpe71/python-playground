def pyramid():
	# Get height from user
	while True:
		height = int(input("Height: "))
		if height < 1 or height > 8:
			print("Input height from 1 to 8 inclusive")
			continue
		else:
			break

	result = ''

	for i in range(1, height + 1):
		for l in range(height - i):
			result += ' '
		for l in range(i):
			result += '#'
		result += '  '
		for l in range(i):
			result += '#'
		result += '\n'	
	
	print(result)
	
pyramid()
