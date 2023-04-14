def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        answer.append(len(emergency))
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if(emergency[i]>emergency[j]):
                answer[i] -= 1
    return answer


solution([3, 76, 24])