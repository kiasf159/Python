def selectionSort(x):
    length = len(x)
    for i in range(length - 1):
        indexMin = i
        for j in range(i+1, length):
            if x[indexMin] > x[j]:
                indexMin = j
        x[i], x[indexMin] = x[indexMin], x[i] # only one change in 1 pass
    return x

array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
selectionSort(array)
print(array)
