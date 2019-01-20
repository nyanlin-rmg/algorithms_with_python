def largest_number(data):
    n = len(data)
    location = 0
    maximun = data[0]
    for k in range(n):
        if maximun < data[k]:
            location = k
            maximun = data[k]

    result = {"Maximum Number": maximun, "Location": location}
    return result


data = ['a', 'b', 'c', 'e', 'f', 'd', 'y', 'j', 'w', 'l']
result = largest_number(data)

for key, value in result.items():
    print(str(key) + " is " + str(value))
