#dfs
def dfs(node):
  count = 0

  value,left,right = tree[node]

  left_max = float('inf')
  right_max = float('inf')

  if left != -1:
    left_max = dfs(left)
  
  if right != -1:
    right_max = dfs(right)

  max_descent = max(left_max,right_max)

  if (value > max_descent):
    count += 1

  return max(value,max_descent)


n = int(input())
tree = []

for _ in range(n):
  value,left,right = map(int,input().split())
  tree.append((value,left,right))

count =0 
dfs(0)
print(count)
