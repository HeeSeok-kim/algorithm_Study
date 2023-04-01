# k번째 던진 사람의 번호를 알아맞히는 문제.
# k번째 던진 사람의 인덱스 = (2(k-1))%len(numbers)    //한 사람씩 건너 뛰므로
# k번째 던진 사람의 번호 = k인덱스+1
def solution(numbers, k):
    indexK = (2*(k-1))%len(numbers)
    return indexK+1
    #print(indexK+1)

solution([1, 2, 3, 4, 5, 6], 5)