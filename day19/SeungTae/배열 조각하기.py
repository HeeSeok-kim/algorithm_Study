def solution(arr, query):
    for i in range(len(query)):
        num = query[i]
        if i % 2 == 0:
            arr = arr[:num+1]
        if i % 2 != 0:
            arr = arr[num:]
    return arr