def solution(orders, course):
    answer = []
    completeCourse = [[[], 0] for _ in range(course[-1]+1)] # 첫번째 index는 완성된 course, 두번째 index는 주문한 횟수
    def addAnswer():
        countCourse = 0
        finishedCourse = []
        for i in range(check_len):
            if check[i]:
                finishedCourse.append(checkAlpha[i])
        setFinishedCourse = set(finishedCourse)
        for i in range(len(orders)):
            if setFinishedCourse.issubset(orders[i]):
                countCourse += 1
        if countCourse >= 2:
            return [finishedCourse, countCourse]
        else:
            return []

    # backtracking 메소드
    def backtracking(start, count):
        if count > max_len:
            return
        ret = addAnswer()
        if ret != [] or count == 0:
            if count in course:
                if ret[1] >= completeCourse[count][1]:
                    add_answer = ''
                    for i in ret[0]:
                        add_answer += i
                    print(add_answer)
                    if ret[1] == completeCourse[count][1]:
                        completeCourse[count][0].append(add_answer)
                    else:
                        completeCourse[count][0] = []
                        completeCourse[count][0].append(add_answer)
                        completeCourse[count][1] = ret[1]


            for i in range(start, check_len):
                check[i] = True
                count += 1
                backtracking(i + 1, count)
                count -= 1
                check[i] = False

    orders_len = [len(orders[i]) for i in range(len(orders))]  # 각 order의 메뉴 개수
    for i in range(len(orders)):
        orders[i] = set(orders[i])
    max_len = max(orders_len)  # 가장 긴 order
    checkAlpha = []
    for i in range(len(orders)):
        for j in orders[i]:
            if not j in checkAlpha:
                checkAlpha.append(j)
    checkAlpha.sort()
    check = [False for _ in range(len(checkAlpha))]
    check_len = len(check)
    backtracking(0, 0)
    print(completeCourse)
    for i in range(course[-1]+1):
        if i in course:
            if len(completeCourse[i][0]) == 1:
                answer.append(completeCourse[i][0][0])
            else:
                for j in completeCourse[i][0]:
                    answer.append(j)
    answer.sort()
    return answer

if __name__ == "__main__":
    orders = list(map(str, input().split()))
    course = list(map(int, input().split()))
    print(solution(orders, course))