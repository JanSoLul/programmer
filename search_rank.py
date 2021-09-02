def solution(info, query):
    def make_key(tmp_key, index, cur_info):
        if index == 4:
            if tmp_key == '':
                tmp_key = '-'
            if tmp_key in db:
                db[tmp_key].append(int(cur_info[-1]))
            else:
                db[tmp_key] = [int(cur_info[-1])]
            return
        next_key = tmp_key
        next_key += cur_info[index]
        make_key(next_key, index+1, cur_info)
        next_key = tmp_key
        make_key(next_key, index+1, cur_info)

    answer = []
    info_len = len(info)
    for i in range(info_len):
        info[i] = info[i].split()
    for i in range(len(query)):
        query[i] = query[i].split()
    for i in range(info_len):
        info[i][4] = int(info[i][4])
    db = dict()
    for i in info:
        make_key('', 0, i)
    for val in db.values():
        val.sort()
    for i in range(len(query)):
        query_key = ''
        for j in range(4):
            if query[i][j*2] != '-':
                query_key += query[i][j*2]
        if query_key == '':
            query_key = '-'
        if query_key in db:
            target_list = db[query_key]
            target = int(query[i][-1])
            left = 0
            right = len(target_list)-1
            while left <= right:
                mid = (left + right) // 2
                if target_list[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            answer.append(len(target_list)-left)
        else:
            answer.append(0)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))
