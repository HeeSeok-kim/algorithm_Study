def getTotalX(a, b):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    lcm_a = a[0]
    gcd_b = b[0]

    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])

    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])

    count = 0
    multiple_of_lcm = lcm_a
    while multiple_of_lcm <= gcd_b:
        if gcd_b % multiple_of_lcm == 0:
            count += 1
        multiple_of_lcm += lcm_a

    return count



getTotalX([2, 4],[16, 32, 96])