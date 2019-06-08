def mergeSort(x, left, right):
    if(left >= right):
        return
    middle = (left + right - 1) / 2
    mergeSort(x, left, middle)
    mergeSort(x, middle + 1, right)
    n1 = middle + 1 - left
    n2 = right - middle
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = x[left + i]
    for j in range(0, n2):
        R[j] = x[middle + 1 + j]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            x[k] = L[i]
            i = i + 1
            k = k + 1
        else:
            x[k] = R[j]
            j = j + 1
            k = k + 1
    while i < n1:
        x[k] = L[i]
        i = i + 1
        k = k + 1
    while j < n2:
        x[k] = R[j]
        j = j + 1
        k = k + 1

array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
mergeSort(array, 0, len(array) - 1)
print(array)
