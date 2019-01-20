def binary_search(data, item):
    lower_bound = 0
    upper_bound = len(data) - 1
    middle = int((lower_bound + upper_bound) / 2)

    while lower_bound < upper_bound and data[middle] != item:
        if item < data[middle]:
            upper_bound = middle - 1

        else:
            lower_bound = middle + 1

        middle = int((lower_bound + upper_bound) / 2)

    if data[middle] == item:
        location = middle
        return "Item found if location of " + str(location)

    else:
        return "Item Not Found!"


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
