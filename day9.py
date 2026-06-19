import heapq

def chronoShortestPath(n, S, adj, start, end):
    # Decode cost for each node (1-indexed)
    node_cost = [0] * (n + 1)

    for i in range(1, n + 1):
        node_cost[i] = sum(ord(ch) - ord('a') + 1 for ch in S[i - 1])

    INF = float('inf')
    dist = [INF] * (n + 1)

    dist[start] = node_cost[start]

    pq = [(dist[start], start)]

    while pq:
        curr_cost, u = heapq.heappop(pq)

        if curr_cost > dist[u]:
            continue

        if u == end:
            return curr_cost

        for v, t in adj[u]:
            new_cost = curr_cost + t + node_cost[v]

            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return -1

import sys
input = sys.stdin.read
data = input().strip().split()

idx = 0

# First line contains N and M
N = int(data[idx])
M = int(data[idx + 1])
idx += 2

# Next N lines contain ChronoString of each node
S = []
for _ in range(N):
    S.append(data[idx])
    idx += 1

# Next M lines contain edges with traversal time
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u = int(data[idx])
    v = int(data[idx + 1])
    T = int(data[idx + 2])
    adj[u].append([v, T])
    adj[v].append([u, T])
    idx += 3

# Last line contains start and end nodes
start = int(data[idx])
end = int(data[idx + 1])

# Call user logic function and print the output
result = chronoShortestPath(N, S, adj, start, end)
print(result)
