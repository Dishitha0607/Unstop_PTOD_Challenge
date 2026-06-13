def can_partition_k_subsets(arr, k):
    total = sum(arr)

    if total%k != 0:
        return False

    target = total//k

    arr.sort(reverse = True)
    n=len(arr)
    used = [False]*n 

    def backtracking(start,curr_sum,subset_formed):
        if subset_formed == (k-1):
            return True

        if curr_sum == target:
            return backtracking(0,0,subset_formed+1)

        for i in range(start,n):
            if used[i]:
                continue

            if curr_sum+arr[i] > target:
                continue
            used[i] = True

            if backtracking(i+1 , curr_sum+arr[i] , subset_formed):
                return True
            used[i] = False
        return False
    return backtracking(0,0,0)  

import sys
input = sys.stdin.read

data = input().strip().split()

arr = list(map(int, data[:-1]))  # All inputs except the last one are part of the array
k = int(data[-1])  # The last input is the integer k

result = can_partition_k_subsets(arr, k)
print("true" if result else "false")