def solution(info, query):
    answer = []
    info_len = len(info)
    for i in range(info_len):
        info[i] = list(map(str, info[i].split()))
    for i in range(len(query)):
        query[i] = list(map(str, query[i].split()))
    for i in range(info_len):
        info[i][4] = int(info[i][4])
    info.sort(key=lambda x : x[4])
    for i in range(len(query)):
        query[i] = [query[i][0], query[i][2], query[i][4], query[i][6], int(query[i][7])]
        target = query[i][-1]
        left = 0
        right = info_len-1
        while left <= right:
            mid = (left + right) // 2
            if info[mid][4] >= target:
                right = mid - 1
            else:
                left = mid + 1
        count = 0
        for j in range(left, info_len):
            for k in range(4):
                if not (query[i][k] == '-' or query[i][k] == info[j][k]):
                    break
                if k == 3:
                    count += 1
        answer.append(count)
    return answer