def solution(sales, links):
    sales_len = len(sales)
    links_len = len(links)
    team = [[] for _ in range(sales_len+1)]
    for i in range(links_len):
        team[links[i][0]].append(links[i][1])
    dp = [[0, 0] for _ in range(sales_len+1)]

    def dfs(n):
        is_leaf_node = True # 이 사람이 말단 직원인지 확인하는 변수
        team_len = len(team[n])
        for i in range(team_len):
            next = team[n][i]
            is_leaf_node = False
            dfs(next)

        if is_leaf_node:
            dp[n][0] = 0
            dp[n][1] = sales[n-1]
            return

        sum = 0
        min_sales = 10 ** 10
        is_attend = True
        for i in range(team_len):
            employee = team[n][i]
            sum += min(dp[employee][0], dp[employee][1])
            if dp[employee][0] >= dp[employee][1]:
                is_attend = False
            min_sales = min(min_sales, dp[employee][1] - dp[employee][0])
        dp[n][1] = sales[n-1] + sum
        if not is_attend:
            dp[n][0] = sum
        else:
            dp[n][0] = sum + min_sales

    dfs(1)
    answer = min(dp[1][0], dp[1][1])
    return answer

if __name__ == '__main__':
    sales_l = [[14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [5, 6, 5, 3, 4], [5, 6, 5, 1, 4], [10, 10, 1, 1]]
    links_l = [[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],
               [[2, 3], [1, 4], [2, 5], [1, 2]],
               [[2, 3], [1, 4], [2, 5], [1, 2]],
               [[3, 2], [4, 3], [1, 4]]]
    for i in range(4):
        print(solution(sales_l[i], links_l[i]))