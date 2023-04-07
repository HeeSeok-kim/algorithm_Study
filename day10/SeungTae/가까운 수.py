# 절대값 차이가 가장 작은 array배열의 요소를 리턴하는 것이 목적이다.
def solution(array, n):
    list = []
    for i in array:
        list.append(abs(n-i))   #(n-i) 차이의 절대값들을 리스트 list에 저장.
        if(n-i>=0): # n이 i보다 크면
            answer = n-min(list)    #n에서 절대값 차이의 최소값을 뺀 값이 가장 가까운 값
        else: # n-i<0  #n이 i보다 작으면
            answer = n+min(list)    #n에서 절대값 차이의 최소값을 더한 값이 가장 가까운 값
    return answer
"""
단 위의 코드는 solution([10, 20],15)일 경우 10이 아닌 20을 반환하기도 하는 등, 차이가 같을 때 항상 더 작은 수를 반환하지 못한다.
왜냐하면 list에 5,5가 담김.
"""
# 아래의 메서드는 아예 배열의 크기 순으로 n의 위치를 찾아 insert로 집어넣고 n 좌우의 값 비교를 통해 절대값 차이가 같거나 작으면 왼쪽것을 반환하고 우측 절대값차이가 더 작으면 우측 요소를 반환한다.
def solution2(array, n):
    for i in range(len(array)):
        if(max(array)<n): return max(array) #n이 가장 클 경우 max(array)반환
        if(array[i]<=n and n<array[i + 1]):
            array.insert(i + 1, n)
            if(abs(array[i] - n)<=abs(array[i + 2] - n)):
                return array[i]
            else: # 우측 절대값차이가 좌측 절대값차이보다 적으면
                return array[i + 2]
"""
하지만 이 경우에도 런타임 에러 발생... 이유가 뭘까?
"""
def solution3(array, n):
    array.sort() #array가 정렬되어 있지 않을 경우를 대비해 sort()를 추가해보았다. 그래도 테스트케이스 2개가 실패한다. (테스트케이스 17, 18)
    for i in range(len(array)):
        if(max(array)<n): return max(array) #n이 가장 클 경우 max(array)반환
        if(n<min(array)): return min(array) #n이 가장 적을 경우 min(array)반환 ⭐⭐⭐ 이걸 빼먹었네.
        if(array[i]<=n and n<array[i + 1]): #n이 중간에 위치하는 자리를 찾는다.
            if(abs(array[i] - n)<=abs(array[i + 1] - n)):
                return array[i]
            else: # 우측 절대값차이가 좌측 절대값차이보다 적으면
                return array[i + 1]

# 위의 코드에서 ⭐⭐⭐ 부분을 빼먹어서 실패한 것이었다. 추후에 다시 추가해주니 정답이 되었다!
def solution4(array, n):
    array.sort()        # 배열을 정렬한다.
    temp = []           # temp 리스트를 선언한다.

    for i in array :
        temp.append( abs(n-i) ) # temp에는 n-배열 요소들의 절대값을 저장한다.

    return array[temp.index(min(temp))] # temp에서 최소값의 인덱스를 찾아 array에 적용한다.
"""
예를 들어 array가 [3, 10, 28]이고 n이 20이라면, 
temp는 [17, 10, 8]이 됩니다. 여기서 temp에서 가장 작은 값은 8이므로, 
temp.index(min(temp))는 2가 됩니다. 따라서 array[2]의 값인 28이 반환됩니다.
"""


k = solution4([10, 20], 15)
print(k)
print((solution4([3,10,28],20)))
print((solution4([10,11,12],13)))