def diagonalDifference(arr):
    leftCount = 0
    rightCount = len(arr[0])-1
    leftSum = 0
    rightSum = 0

    for i in range(0,len(arr)):
        leftSum += arr[i][leftCount]
        rightSum += arr[i][rightCount]
        leftCount += 1
        rightCount -= 1

    return abs(leftSum - rightSum)


arr = [[1,2,3],[4,5,6],[9,8,9]]

print(diagonalDifference(arr))