# Kadane's Algorithm

def find_max_subarray(arr):
    current_sum = global_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        if current_sum >= global_sum:
            global_sum = current_sum
    
    return global_sum

arr = input("enter the array: ")
arr = arr.split(" ")
arr = list(map(int, arr))
print(find_max_subarray(arr))