def climbingStairs(n: int) -> int:
    predefined = [0, 1, 2]
    memo = predefined + [-1] * (n - len(predefined) + 1)

    def climb(n: int) -> int:
        if n < 2:
            return n
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

    return climb(n)
