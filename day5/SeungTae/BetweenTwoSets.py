"""
<문제접근>
해당 문제는 한 배열의 정수요소들의 공배수인 동시에 다른 배열의 정수요소들의 공약수인 정수의 개수를 구하는 문제이다.
예를 들어
2 6     //배열 a
24 36   //배열 b
이 있다면 6, 12가 각각 그 공통 인자가 된다.
6과 12는 2와 6의 공배수이며, 동시에 24, 36의 공약수이다.

<제약>
각각의 배열의 개수 n, m은 1과 10 사이이며,
배열 안의 요소들은 100을 넘지 않는 값이다.

<해답 로직 설계1>
공통 인자를 담은 리스트 객체를 생성한다. //tmpList = list()
배열 a에서는 각 요소의 최소 공배수를 찾는다.
최소 공배수가 나오면 해당 변수 값을 다음 로직으로 넘긴다.
배열 b에서는 각 요소의 최대 공약수를 찾는다.

<⭐tip>
최소 공배수를 구하는 함수와 최대 공약수를 구하는 함수를 따로 설계하자.

<해답 로직 설계2>
배열 a의 최소공배수를 구하기 위한 함수와
배열 b의 최대공약수를 구하기 위한 함수를 따로 만든다.
a의 최소공배수 * 1, 2, 3, ...이 리스트 b에 존재하는 경우에만
count를 +1한다. a의 공배수가 b의 최대공약수보다 크면 break로 루프를 탈출한다.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getGcd(x, y): #최대공약수 구하는 함수 (⭐유클리드 호제법 이용)
    if(y>x):
        x, y = y, x
    while y :   #y가 0이 아니면
        x, y = y, x % y # x와 y의 값을 다시 y, x를 y로 나눈 나머지값과 대체한다.
    return x    #⭐위의 과정을 반복했을 때 y(즉, x를 y로 나눈 나머지)가 0이 되면 x를 반환한다.
def getListGcd(numList): #최대공약수 구하는 함수 (⭐유클리드 호제법 이용)
    gcd_nums = None  #해당 리스트의 GCD 최대공약수는 일단 None으로 둔다.
    for i in range(len(numList)):   #리스트의 크기만큼 i값이 순회
        if i == 0:  # i가 0이면
            gcd_nums = numList[i]    #gcd_nums에 numList의 첫 번째 요소를 담는다.
        else:
            gcd_nums = getGcd(gcd_nums, numList[i])   #i가 1이 아닐때 이전 gcd_nums값과 numList[i]요소의 gcd를 구해 저장
    return gcd_nums # 그 gcd_nums (인자로 들어온 numList의 공통 최대공약수)를 반환한다.

def getLcm(x, y):   #최소공약수 구하는 함수
    # 최소공배수 = 두 수의 곱 / 최대공약수
    return x * y // getGcd(x, y)

def getListLcm(numList):    #numList의 최소공약수를 구하는 함수
    lcm_nums = None
    for i in range(len(numList)):
        if i == 0:
            lcm_nums = numList[i]
        else:
            lcm_nums = getLcm(lcm_nums, numList[i])
    return lcm_nums

def getTotalX(a, b):
# Write your code here
    lcm_a = getListLcm(a)
    gcd_b = getListGcd(b)

    # a의 공배수들 중 min_b이하
    a_cms = []
    i = 1
    while True:
        temp = lcm_a * i    #temp는 a의 최소공배수 * i
        if temp > gcd_b:    #만약 temp가 gcd_b보다 크면 루프문 탈출 (a의 공배수가 b의 최대공약수보다 크면 안되므로)
            break

        a_cms.append(temp)  #a_cms 리스트에 temp를 추가
        i += 1

    count = 0
    for temp in a_cms:
        is_factor = True
        for bb in b:
            if bb % temp != 0:
                is_factor = False
                break
        if is_factor:
            count += 1

    return count


a = [2, 3]
b = [2, 4]
getTotalX(a, b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
