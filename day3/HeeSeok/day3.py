def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    else:
        while x1 <= x2:
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2:
                return "YES"
        return "NO"

print(kangaroo(0,3,4,2))
print(kangaroo(0,2,5,3))
print(kangaroo(28,8,96,2))

