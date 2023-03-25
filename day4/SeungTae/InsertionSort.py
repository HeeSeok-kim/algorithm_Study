# 제약에 따르면 최대값이 10의 3승이므로 이중 for문 사용이 가능하다. O(n^2)
# i는 for문에 사용될 인덱스 값으로 계속 ++증가.
# 현재 i인덱스 요소가 올바른 위치에 있는 경우 (변경사항 없는 경우) 프린트
# 현재 i인덱스 요소가 다음 요소보다 큰 경우 다음 요소의 위치를 바꾸고 이전 인덱스 모두 체크
# n은 배열의 길이이다.
def insertionSort2(n, arr):
    for i in range(n-1):
        tmp = 0
        if arr[i] < arr[i + 1]:
           print(arr)
           i= i + 1
        elif arr[i] > arr[i + 1]:
            tmp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = tmp
            print(arr)
            i= i + 1


ar1 = [3, 1, 7, -100, 4, 9]

insertionSort2(3, ar1)

