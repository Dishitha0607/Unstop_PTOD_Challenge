n = int(input())
nums = list(map(int,input().split()))

freq={}

for num in nums:
  freq[num] = freq.get(num,0) + 1

max_freq = max(freq.values())
res = min(num for num,count in freq.items() if count==max_freq)
print(res)
