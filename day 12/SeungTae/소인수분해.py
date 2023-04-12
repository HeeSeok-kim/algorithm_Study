"""
while i * i <= n: 이 조건은 왜 붙이는거야?
이 조건은 n의 약수 중 가장 큰 값은 n의 제곱근을 넘을 수 없다는 점을 이용하기 위해 추가한 것입니다.
만약 i가 n의 제곱근보다 큰 경우에는 n을 나눌 수 있는 값이 더 이상 존재하지 않으므로 반복문을 종료하게 됩니다.
따라서 반복문을 최소한으로 실행하여 시간 복잡도를 줄일 수 있습니다.
"""
def solution(n):
    i = 2           # 소수는 2부터 시작한다.
    factors = set() # 중복된 값은 제거해야하므로 리스트가 아닌 set을 사용한다.
    while i * i <= n:   # i가 n의 제곱근보다 큰 경우에는 n을 나눌 수 있는
        if n % i:
            i += 1
        else:
            n //= i     # n은 i로 나눈 정수몫
            factors.add(i) # set factors에 저장
    if n > 1:   # n이 1보다 크면 소인수 분해 구성원이기 때문에 추가
        factors.add(n)
    return sorted(list(factors))

