def solution(n):
    factorial = 1
    answer = 1      # answer이 몇번 째 factorial인지 나타내는 구조. 예) 3!이면 answer=3
    while True:
        if(factorial > n):
            return answer-1
        elif(factorial == n): return answer
        answer += 1
        factorial *= answer
    return answer

print(solution(3628800))

"""
<팩토리얼 함수를 임포트해서 풀이하는 방법>
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
    
<if문을 사용하지 않는 방법>
def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:       # factorial이 n이하인 동안
        answer += 1
        factorial = factorial * answer
    answer -= 1 #factorial이 n을 초과한다면 answer-1을 리턴 (answer이 한 번 더 증가했다는 이야기이므로)
    return answer
    
<간결한 풀이>
def solution(n):
    cal = 1
    fact = 1

    while True :
        cal *= fact
        if cal > n :
            return fact - 1
        fact += 1
"""