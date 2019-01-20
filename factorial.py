def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

number = int(input("Enter Number : "))
answer = factorial(number)
print('The Factorial Number of %s is %s' %(number, answer))