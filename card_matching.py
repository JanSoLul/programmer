from collections import deque
from copy import deepcopy
from itertools import permutations


def bfs(board, start_x, start_y, end_x, end_y):
    check_l = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([(start_x, start_y, 0)])
    visited = {(start_x, start_y)}

    while queue:
        x, y, count = queue.popleft()

        if x == end_x and y == end_y:
            return count

        for add_x, add_y in check_l:
            tmp_x = x + add_x
            tmp_y = y + add_y
            if 0 <= tmp_x < 4 and 0 <= tmp_y < 4 and (tmp_x, tmp_y) not in visited:  # 방향키
                queue.append((tmp_x, tmp_y, count + 1))
                visited.add((tmp_x, tmp_y))

            while 0 <= tmp_x + add_x < 4 and 0 <= tmp_y + add_y < 4:  # 컨트롤 + 방향키
                tmp_x += add_x
                tmp_y += add_y
                if board[tmp_x][tmp_y] > 0:
                    break

            if (tmp_x, tmp_y) not in visited:
                queue.append((tmp_x, tmp_y, count + 1))
                visited.add((tmp_x, tmp_y))


def solution(board, r, c):
    answer = 10 ** 10
    card = {n: [] for n in range(1, 7)}

    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                card[board[i][j]].append((i, j))

    for per in permutations(filter(lambda v: v, card.values())):
        start_x, start_y = r, c
        copy_board = deepcopy(board)
        tmp = 0

        for check in per:
            tmp1 = bfs(copy_board, start_x, start_y, check[0][0], check[0][1]) + bfs(copy_board, check[0][0], check[0][1], check[1][0], check[1][1])
            tmp2 = bfs(copy_board, start_x, start_y, check[1][0], check[1][1]) + bfs(copy_board, check[1][0], check[1][1], check[0][0], check[0][1])

            if tmp1 > tmp2:  # 서로 다른 짝 카드 위치에서 시작할떄 최소인 경우를 선택
                start_x, start_y = check[0][0], check[0][1]
            else:
                start_x, start_y = check[1][0], check[1][1]
            tmp += min(tmp1, tmp2) + 2  # 둘중 이동횟수가 적은 것과 카드 뒤집는 횟수 더해줌

            copy_board[check[0][0]][check[0][1]] = 0
            copy_board[check[1][0]][check[1][1]] = 0
        answer = min(answer, tmp)

    return answer


if __name__ == '__main__':
    board_l = [[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], [[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]]]
    r_l = [1, 0, 0]
    c_l = [0, 1, 0]
    for i in range(3):
        print(solution(board_l[i], r_l[i], c_l[i]))