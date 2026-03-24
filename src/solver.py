def solve_d01kp_dp(item_sets, max_weight):
    dp = [0] * (max_weight + 1)
    select_info = [[] for _ in range(max_weight + 1)]

    for s in item_sets:
        w1, v1, w2, v2, w3, v3 = s
        for w in range(max_weight, -1, -1):
            options = [(0, 0, 0),
                       (w1, v1, 1),
                       (w2, v2, 2),
                       (w3, v3, 3)]
            for tw, tv, idx in options:
                if w >= tw and dp[w - tw] + tv > dp[w]:
                    dp[w] = dp[w - tw] + tv
                    select_info[w] = select_info[w - tw] + [(idx, s)]
    return dp[max_weight], select_info[max_weight]