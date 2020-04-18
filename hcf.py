def gcd( a, b):
    while a and b :
        print(a and b)
        if (a >= b):
            a %= b
        else:
            b %= a
    return a + b;
print(gcd(3,7))