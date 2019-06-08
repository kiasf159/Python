def quickSort(x, left, right):
    low = left
    high = right
    pivot = x[(left + right) / 2]
    while low < high:
        while x[low] < pivot:
            low = low + 1
        while x[high] > pivot:
            high = high - 1
        x[low], x[high] = x[high], x[low]
    low = low + 1
    high = high - 1
    if(left < high):
        quickSort(x, left, high)
    if(low < right):
        quickSort(x, low, right)


array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 20, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 50]
quickSort(array, 0, len(array) - 1)
print(array)
