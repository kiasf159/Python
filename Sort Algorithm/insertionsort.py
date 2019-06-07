def insertionSort(x):
    for i in range(1, len(x)):
		j = i - 1
		key = x[i]
        # for j in range(i - 1, 0):
        #    if [j + 1] > key:
        #        x[j + 1] = x[j]

		while x[j] > key and j >= 0:
			x[j+1]  = x[j]
			j = j - 1
		x[j+1] = key

array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
insertionSort(array)
print(array)
