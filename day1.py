from itertools import combinations
def countValidCombos(N, K, L, R, deviceTypes, prices):
    count = 0

    for combo in combinations(prices , K):
        total = sum(combo)

        if L <= total <= R:
            count += 1
    return count

if __name__ == "__main__":
    N, K, L, R = map(int, input().split())
    deviceTypes = []
    prices = []
    for _ in range(N):
        line = input().split()
        deviceTypes.append(line[0])
        prices.append(int(line[1]))
    
    # Call the user logic function and print the result
    result = countValidCombos(N, K, L, R, deviceTypes, prices)
    print(result)
