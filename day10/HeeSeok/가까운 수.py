def solution(array, n):
    array.sort()
    answer = array[0]
    min_num = abs(n - array[0])
    for i in range(1,len(array)):
        num = abs(n-array[i])
        if min_num > num:
            min_num = num
            answer = array[i]

    return answer

print(solution([3, 10, 28],20))
