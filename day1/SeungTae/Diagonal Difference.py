arr1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, -10]]

'''

def diag(arr):
       i=0
       j=0
       sum1=0
       i2=-1
       j2=-1
       sum2=0
              for i in arr:
                     for j in arr:
                           k = arr[i][j]
                           i = i+1
                           j = j+1
                           sum1 = sum1 + k
                           if arr[i][j]<-100 : return
                           if arr[i][j]>100 : return
              for i2 in arr: 
                    for j2 in arr:
                            k = arr[i2][j2] 
                            i2 = i2-1
                            j2 = j2-1
                            sum2 = sum2 + k 
       return sum1+sum2
               '''
def diag(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                sum1 += arr[i][j]
            if i + j == len(arr) - 1:
                sum2 += arr[i][j]
            if arr[i][j] < -100 or arr[i][j] > 100:
                return None
    return abs(sum1 + sum2)

k = diag(arr1)
print(k)