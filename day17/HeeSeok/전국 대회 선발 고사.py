def solution(rank, attendance):
    data = {};
    for i in range(len(rank)):
        if(attendance[i]):
            data[rank[i]] = i
    arr = sorted(data.keys())

    return 10000 * data[arr[0]] + 100 * data[arr[1]] + data[arr[2]]