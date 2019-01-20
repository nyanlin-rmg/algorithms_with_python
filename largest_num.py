data = [5, 3, 5, 1, 4, 20, 0, 9, 10]
n = len(data)
location = 0
k = 0
maximum = data[k]
for k in range(n):
	if (maximum < data[k]):
		location = k
		maximum = data[k]

print("Maximum Number : " + str(maximum))
print("Location : " + str(location))