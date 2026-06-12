def user_logic(N, T, room_data):
    result = []

    for K,E,intervals in room_data:
        schedule = [0]*T

        for L,R in intervals:
            for hour in range(L-1,R):
                schedule[hour] = 1
        energy_used = sum(schedule)

        if energy_used <= E:
            result.append(schedule)
        else:
            result.append("NOT POSSIBLE")
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    N = int(data[index])
    index += 1
    T = int(data[index])
    index += 1

    room_data = []
    for _ in range(N):
        K = int(data[index])
        index += 1
        E = int(data[index])
        index += 1
        intervals = []
        for _ in range(K):
            L = int(data[index])
            index += 1
            R = int(data[index])
            index += 1
            intervals.append((L, R))
        room_data.append((K, E, intervals))
    
    # Call user logic function
    results = user_logic(N, T, room_data)
    
    # Print the output as per the problem statement
    for result in results:
        if isinstance(result, str):
            print(result)
        else:
            print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
