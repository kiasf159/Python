def radixSort(x, base=10):
    size = len(x)
    maxval = max(x)
    exp = 1
    while exp <= maxval:
        output = [0] * size
        count = [0] * base
        for i in range(size):
            count[(x[i] // exp) % base] += 1
        for i in range(1,base):
            count[i] += count[i - 1]
        for i in range(size - 1, -1, -1):
        	j = (x[i] // exp) % base
        	output[count[j] - 1] = x[i]
        	count[j] -= 1
        for i in range(size):
            x[i] = output[i]
        exp = exp * base

array = [13, 48, 23, 38, 9, 87, 55, 94, 72, 21, 46, 90, 31, 50, 77, 36, 64, 7, 81, 17, 29, 68, 99, 16, 2, 83, 20]
radixSort(array)
print(array)
