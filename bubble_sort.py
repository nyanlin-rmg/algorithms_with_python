def bubble_sort(data):
    i = len(data)
    while i > 1:
        for k in range(0, i-1):
            if data[k] >= data[k+1]:
                temp = data[k]
                data[k] = data[k+1]
                data[k+1] = temp
        i = i - 1
    return data


data = [1, 2, 6, 4, 9, 8, 3, 5, 7]
result = bubble_sort(data)
print(result)
