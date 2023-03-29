def countingSort(arr):
    countList = [0 for i in range(100)]

    for i in range(len(arr)):
        countList[arr[i]] += 1

    print(countList)

data = countingSort([5,5,1,1,2,3])