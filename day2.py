## Problem Statement
# A building has N rooms, each with a smart air conditioner that can operate in three modes:

# 0 = Off

# 1 = Eco mode (uses 1 unit of energy/hour)

# 2 = Cool mode (uses 2 units of energy/hour)

# The building is active for T hours in a day. For each room, the building manager provides:

# A list of cooling requirement intervals. Each interval means the AC must be on (mode 1 or 2) during that time (inclusive).

# A maximum energy limit Eᵢ for the AC in that room for the whole day.

# You need to generate a valid hourly schedule (list of length T with values 0, 1, or 2) for each room such that:

# All required intervals K are covered (AC must not be in mode 0 during those hours).

# The total energy consumption does not exceed Eᵢ for each room.

# Try to use Cool mode (mode 2) as less frequently as possible (Eco mode is preferred if both satisfy condition 1 and 2).

# If it's not possible to fulfill these conditions for any room, output "NOT POSSIBLE" for that room.

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
