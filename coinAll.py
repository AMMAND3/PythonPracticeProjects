# 'getWays' & anotherWay function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def minNumberOfCoinsNeeded(coins: list, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

def getWays(n, c):
    # DYNAMIC PROGRAMMING
    # Time: O(n*m)
    # Memory: O(n*m)
    
    dp = [[0] * (len(c) + 1) for i in range(n + 1)]
    dp[0] = [1] * (len(c) + 1)
    for a in range(1, n + 1):
        for i in range(len(c) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - c[i] >= 0:
                dp[a][i] += dp[a - c[i]][i]
    return dp[n][0]

def anotherWay(n, c):
        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(len(c) - 1, -1, -1):
            nextDP = [0] * (n + 1)
            nextDP[0] = 1

            for a in range(1, n + 1):
                nextDP[a] = dp[a]
                if a - c[i] >= 0:
                    nextDP[a] += nextDP[a - c[i]]
            dp = nextDP
        return dp[n]
    
    
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    print(str(ways) + '\n')
