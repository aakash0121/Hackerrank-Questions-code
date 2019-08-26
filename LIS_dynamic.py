
def LIS(arr):
    lis = [1]*len(arr)

    for i in range(1, len(arr)):
        m = []
        m.append(0)
        for j in range(i-1, -1, -1):
            if arr[j] <= arr[i]:
                m.append(lis[j])
        lis[i] = max(m) + 1
    
    m = max(lis)
    return m, lis

if __name__ == "__main__":
    print(LIS([50,9,10,7,40,80]))
