def solution(bin1, bin2):
    a = int(bin1, 2) + int(bin2, 2)
    print(a)
    return bin(a)[2:]