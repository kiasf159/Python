def bubbleSort(x):
    length = len(x)
    for i in range(length - 1):
        for j in range(length - i - 1): # it's the same as the out-range
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]


array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
bubbleSort(array)
print(array)
