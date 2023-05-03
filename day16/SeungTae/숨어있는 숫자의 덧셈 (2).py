def solution(my_string):
    num_str = ''  # 자연수를 저장할 문자열 변수 초기화
    num_sum = 0  # 자연수의 합을 저장할 변수 초기화

    for ch in my_string:  # 문자열의 각 문자를 반복
        if ch.isdigit():  # 문자가 숫자인 경우
            num_str += ch  # 숫자를 num_str 변수에 추가
        else:
            if num_str:  # 이전에 숫자가 있었다면
                num_sum += int(num_str)  # 숫자를 정수로 변환하여 합산
                num_str = ''  # 숫자를 저장하는 변수 초기화
    if num_str:  # 마지막으로 처리되지 않은 숫자가 있다면
        num_sum += int(num_str)  # 숫자를 합산
    return num_sum  # 자연수의 합을 반환
