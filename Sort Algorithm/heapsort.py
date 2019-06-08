def heapSort(x):
    length = len(x)
    for i in range(length, -1, -1):
        heapify(x, length, i)
    for i in range(length -1, 0, -1):
        x[i], x[0] = x[0], x[i]
        heapify(x, i, 0)

def heapify(array, size, i):
    largest = i
    L = 2*i + 1
    R = 2*i + 2
    if L < size and array[i] < array[L]:
        largest = L
    if R < size and array[largest] < array[R]:
        largest = R
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, size, largest)


array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
heapSort(array)
print(array)
