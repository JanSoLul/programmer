def check_open(check_map, key, M, ud_move, lr_move):
    count = 0
    for i in range(M):
        for j in range(M):
            if check_map[i+ud_move][j+lr_move] == -1:
                continue
            if key[i][j] == 0:
                if check_map[i+ud_move][j+lr_move] == 0:
                    return -1
                continue
            else:
                if check_map[i+ud_move][j+lr_move] == 0:
                    count += 1
                if check_map[i+ud_move][j+lr_move] == 1:
                    return -1
    return count

def solution(key, lock):
    M = len(key)
    N = len(lock)
    blank_count = 0
    map_size = N + 2 * (M - 1)
    check_map = [[-1 for _ in range(map_size)] for _ in range(map_size)]
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                blank_count += 1
            check_map[M+i-1][M+j-1] = lock[i][j]

    check_count = M + N - 1
    for _ in range(4): # 4방향 회전
        for i in range(check_count):
            for j in range(check_count):
                save_count = check_open(check_map, key, M, i, j)
                if save_count == blank_count:
                    return True
        key = list(zip(*reversed(key)))
    return False

if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

