def linear_search(data, item):
    n = len(data)
    data.append(item)
    location = 0

    while data[location] != item:
        location += 1

    if location == n:
        return "Item Not Found!"
    else:
        return "Item Found! in location of " + str(location)


print(linear_search([1, 2, 3, 4, 5], 1))
