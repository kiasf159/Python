def shellSort(x):
    length = len(x)
    gap = length / 2
    while gap >= 1:
        for i in range(length - gap):
            if x[i] > x[i + gap]:
                x[i], x[i + gap] = x[i + gap], x[i]
        gap = gap - 1  # it's important to set the gap


array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
shellSort(array)
print(array)
