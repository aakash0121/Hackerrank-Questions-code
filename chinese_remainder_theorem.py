from functools import reduce

n = list(map(int, input().split()))
rem = list(map(int, input().split()))

pro = reduce((lambda x, y : x*y), n)
pp = [pro//i for i in n]

#print(n, rem, pro, pp)

def find_inv(num_pp, num_n):
    i = 1
    while True:
        if (num_pp*i)%num_n == 1:
            return i
        else:
            i += 1

inv = [find_inv(i,j) for i,j in zip(pp, n)]
#print(inv)
sum = 0
for i in range(len(n)):
    sum += (rem[i]*pp[i]*inv[i])
    #print(sum)
print(sum%pro)