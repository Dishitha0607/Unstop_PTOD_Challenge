def max_chocolates(grid, n, m):
    dp = [[[-1]*m for _ in range(m)] for _ in range(n)]

    for c1 in range(m):
        for c2 in range(m):
            
            if c1==c2:
                dp[n-1][c1][c2] = grid[n-1][c1]
            else:
                dp[n-1][c1][c2] = grid[n-1][c1] + grid[n-1][c2]
    
    for row in range(n-2,-1,-1):
        for c1 in range(m):
            for c2 in range(m):
                
                if c1==c2:
                    current = grid[row][c1]
                else:
                    current = grid[row][c1] + grid[row][c2]
                best=0

                for d1 in [-1,0,1]:
                    for d2 in [-1,0,1]:
                        
                        nc1 = c1+d1
                        nc2 = c2 + d2

                        if 0<=nc1<m and 0<=nc2<m:
                            best = max(best,dp[row+1][nc1][nc2])
                dp[row][c1][c2] = current+best
    return dp[0][0][m-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m
    
    # Call user logic function and print the output
    result = max_chocolates(grid, n, m)
    print(result)

if __name__ == "__main__":
    main()
