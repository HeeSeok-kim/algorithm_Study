def insertionSort2(n, arr):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                swap = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = swap
            else:
                break
        print(' '.join(str(e) for e in arr))


insertionSort2(6,[1, 4, 3, 5, 6, 2])