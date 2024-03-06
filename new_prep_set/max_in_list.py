# climbing stairs
def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # Create a list to store the number of ways to reach each step
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    # Calculate the number of ways to reach each step
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

# Test the function with different values of n
n = 3
print(f"Number of ways to climb {n} steps: {climb_stairs(n)}")

n = 4
print(f"Number of ways to climb {n} steps: {climb_stairs(n)}")

n = 5
print(f"Number of ways to climb {n} steps: {climb_stairs(n)}")

