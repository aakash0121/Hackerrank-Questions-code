# URL of the problem : https://www.geeksforgeeks.org/ugly-numbers/

def ugly_func(n):
    ugly = [None] * n
    ugly[0] = 1

    i2, i3, i5 = 0, 0, 0
    for i in range(1, n):
        next_multiple_2 = ugly[i2]*2
        next_multiple_3 = ugly[i3]*3
        next_multiple_5 = ugly[i5]*5

        next_ugly_number = min(next_multiple_2, next_multiple_3, next_multiple_5)
        ugly[i] = next_ugly_number

        if next_ugly_number == next_multiple_2:
            i2 += 1
        if next_ugly_number == next_multiple_3:
            i3 += 1
        if next_ugly_number == next_multiple_5:
            i5 += 1
    return ugly[n-1]

n = int(input("enter the number: "))
result = ugly_func(n)
print(result)