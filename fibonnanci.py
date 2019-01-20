def fibonnanci(count):
	try:
		count = int(count)
		i = range(0, count)
		num1 = 0
		num2 = 1
		result = []
		for item in i:
			result.append(num1)
			num3 = num1 + num2
			num1 = num2
			num2 = num3
		return result
	except ValueError:
		return "Try Later!"

times = input("Enter Count Times:")
print(fibonnanci(times))