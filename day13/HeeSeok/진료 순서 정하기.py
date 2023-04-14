def solution(emergency):
    answer = []
    data = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(data.index(i)+1)

    return answer