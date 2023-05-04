def solution(rank, attendance):
    my_list = []
    for i in range(len(rank)):
        if attendance[i]==True:
            my_list.append(rank[i])
    my_list = sorted(my_list)
    return 10000*rank.index(my_list[0])+100*rank.index(my_list[1])+rank.index(my_list[2])

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))

"""
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
"""