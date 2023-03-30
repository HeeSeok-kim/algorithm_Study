def solution(array, commands):
    answer = []
    origin = array
    for i in range(len(commands)):
        array = origin # 반드시 원형으로 초기화 해야함
        start = commands[i][0]-1    #-1의 이유는 index가 아니라 '몇 번째'의 서수 개념이기 때문
        end = commands[i][1]-1
        index = commands[i][2]-1
        array = array[start:(end+1)]
        array.sort() #슬라이싱에서 마지막요소는 포함하지 않는다. 따라서 포함시키려면 end+1
        num = array[index]
        answer.append(num)
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])


"""
<더 좋은 방법 - 파이썬은 for a in A 를 사용할 수 있다. A 배열의 요소를 a가 순회한다는 뜻이다.>
def solution(array, commands):
    answer = []
    for com in commands: ##이 부분이 핵심
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer
"""
