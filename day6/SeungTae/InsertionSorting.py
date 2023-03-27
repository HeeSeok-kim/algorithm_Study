"""
삽입정렬1
삽입정렬은 최악, 평균 모두 시간복잡도가 O(N^2)이며 최적화가 이루어졌을 경우 이미 정렬이 되어 있는 배열에서 O(N)의 시간 복잡도를 가진다.
Constarints에서 주어진 배열의 개수가 n=10^3 이므로, 삽입정렬을 사용하여 문제를 풀 수 있다.

오름차순의 정렬을 만드는 문제이며,
일반적인  문제와 다른 점은 뒤에서부터 비교를 시작한다는 점이다.
"""

def insertionSort(n, arr):
    for end in range(n-1, 0, -1):
        key = arr[end]
        before = end - 1
        while(before>=0 and arr[before]>key):
            arr[before+1], arr[before] = arr[before], arr[before+1]
            print(arr)
            before -= 1

# insertionSort(5, [1,5,6,8,2])