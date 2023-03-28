"""
문제 : 계수정렬 _1
제약 조건
100 <n <= 10^6      #계수정렬은 최악의 경우에도 시간복잡도가 O(배열개수N+최대값K)
0 <= arr[i] < 100   #배열 각 요소 값들은 양의 정수이어야 하며, 이 요소값들은 인덱스화하여 각 중복된 요소개수를 센다.

계수정렬은 요소의 범위가 양의 정수이고, 데이터의 크기 범위가 제한된 경우 사용가능.

해당 문제는 계수 정렬의 이용조건에 딱 알맞다.
"""

def countingSort(arr):
    # 1. 계수정렬 배열 count를 만든다. 인덱스는 0부터 max(arr)+1까지 이다. 또한 각 값을 0으로 초기화한다.
    count = [0]*(max(arr)+1)

    # 2. 배열 arr의 각 요소를 순회하며 i 값이 발견될 때 count[i]값의 배열도 증감연산자 ++의 적용을 받게한다.
    for i in arr :
        if i>=0 :
            count[i] += 1

    # 3. 배열 count를 순회하며 각 count[k]값을 print로 출력한다.
    for k in range(len(count)):
        print(str(count[k]) , end=" ")

test = [1, 3, 4, 2, 1, 1, 4]
countingSort(test)