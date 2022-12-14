def solution(m, n):
    dp = [[0 for i in range( n +1)] for j in range( m +1)]
    for i in range( m +1):
        dp[i][1] = 1            # 如果只有一个盘子则只有一种放置方案
    for j in range(1, n+ 1):
        dp[0][j] = 1  # 如果没有苹果则只有一种放置方案
        dp[1][j] = 1  # 如果只有一个苹果也相当于只有一种方案
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            if i < j:  # 如果苹果数量少，则盘子一定会空，所以去除那些空的盘子其实不影响方案数
                dp[i][j] = dp[i][i]
            else:  # 如果苹果数量多，则考虑是否要装够j个盘子，如果不装够则有dp[i][j-1]，如果装够则相当于从所有盘子同时去掉一个苹果无影响，则有dp[i-j][j]
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

    return dp[m][n]


while True:
    try:
        m, n = map(int, input().split())
        print(solution(m, n))
    except:
        break
