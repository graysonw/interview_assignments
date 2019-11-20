# Edge cases:
# 1) len(temperatures> < N
# 2) temperatures are negative (particularly after initial 0..N sum where we are using the -= operator
# 3) All numbers are the same
# 4) Multiple windows with same maximum temperature


def warmest_days(temperatures, N):
    if not temperatures:
        return None

    # If we want N > the actual size of the array, just return the whole array
    if len(temperatures) <= N:
        return 0

    try:
        # Use sliding window algorithm with a window of size N
        # If there are multiple windows with the same maximum average temperature, just return the first one
        print(temperatures[0:N])
        maximum_sum = sum(temperatures[0:N])
        running_sum = maximum_sum
        maximum_sum_index = 0

        for i in range(1, len(temperatures) - N + 1):
            running_sum -= temperatures[i - 1]
            running_sum += temperatures[i + N - 1]
            if running_sum > maximum_sum:
                maximum_sum = running_sum
                maximum_sum_index = i
        return maximum_sum_index
    except TypeError:
        print("Error: non-numeric values found.\n")
        return None


if __name__ == "__main__":

    # Negative numbers
    N = 3
    temps = [-100, 50, 30, -200, 10, -40, -75]
    offset = warmest_days(temps, N)
    print("Array index/offset of start of " + str(N) + " warmest days: " + str(offset) +
          ", with temps:" + str(temps[offset:offset + N]))

    # Floats
    N = 2
    temps = [15.1, 33.5, -85.7, 42.6, 25.6]
    offset = warmest_days(temps, N)
    print("Array index/offset of start of " + str(N) + " warmest days: " + str(offset) +
          ", with temps:" + str(temps[offset:offset + N]))

    # N > len(temps)
    N = 7
    temps = [15.1, 33.5, -85.7, 42.6, 25.6]
    offset = warmest_days(temps, N)
    print("Array index/offset of start of " + str(N) + " warmest days: " + str(offset) +
          ", with temps:" + str(temps[offset:offset + N]))

    # temps is empty
    N = 7
    temps = []
    offset = warmest_days(temps, N)
    if offset:
        print("Array index/offset of start of " + str(N) + " warmest days: " + str(offset) +
              ", with temps:" + str(temps[offset:offset + N]))

    # Non-numeric values
    N = 3
    temps = [15.1, 33.5, -85.7, "thirty-three", 42.6, 25.6]
    offset = warmest_days(temps, N)
    if offset:
        print(offset)

    # Max at end
    N = 3
    temps = [15.1, 33.5, -85.7, 42.6, 25.6, 100]
    offset = warmest_days(temps, N)
    print("Array index/offset of start of " + str(N) + " warmest days: " + str(offset) +
          ", with temps:" + str(temps[offset:offset + N]))