def solution(spell, dic):
    answer = 0
    count =0;
    for i in dic:
        for j in spell:
            if(j in i):
                count +=1
        if(count == len(spell)):
            return 1
        else:
            count = 0;

    return 2