def quick(data, n, beg, end, loc):
    left = beg
    right = end
    loc = beg

    while data[loc] <= data[right] and loc != right:
        right += 1

    if loc == right:
        return data

    if data[loc] > data[right]:
        temp = data[loc]
        data[loc] = data[right]
        data[right] = temp

        loc = right

    while data[left] <= data[loc] and left != loc:
        left += 1

    if loc == left:
        return data

    if data[left] > data[loc]:
        temp = data[loc]
        data[loc] = data[left]
        data[left] = temp
        loc = left
    
array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

lower = []
upper = []

top = 0
if len(array) > 1:
    top = top + 1
    lower[0] = 0
    upper[0] = len(array) - 1

while top != 0:
    beg = lower[top]
    end = upper[top]
    top -= 1

    quick(array, len(array), beg, end, loc)
    if beg < loc - 1
    

