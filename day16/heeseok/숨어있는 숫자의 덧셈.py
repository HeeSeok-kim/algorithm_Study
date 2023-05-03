import re

def solution(my_string):
    numbers = list(map(int,re.findall('[0-9]+', my_string)))

    return sum(numbers)