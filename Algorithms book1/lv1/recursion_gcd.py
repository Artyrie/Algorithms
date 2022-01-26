def recursion_gcd(n1, n2):
    if (n2 == 0):
        return n1
    else:
        return recursion_gcd(n2, n1 % n2)

print(recursion_gcd(13, 39))