from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n+1)]
    maxNum = 10**8
    dist = [[maxNum for _ in range(n+1)] for _ in range(n+1)]
    fares_len = len(fares)
    for i in range(fares_len):
        x, y, w = fares[i]
        adj[x].append((y, w))
        adj[y].append((x, w))

    def dijkstra(start):
        heap = []
        heappush(heap, [0, start])
        dist[start][start] = 0
        while heap:
            curW, curV = heappop(heap)
            for nextV, nextW in adj[curV]:
                nextW += curW
                if dist[start][nextV] > nextW:
                    dist[start][nextV] = nextW
                    heappush(heap, [nextW, nextV])

    for i in range(1, n+1):
        dijkstra(i)
    route = dist[s][a]+dist[s][b]
    for i in range(1, n+1):
        if i != s:
            route = min(route, dist[s][i] + dist[i][a] + dist[i][b])
    answer = route
    return answer

if __name__ == '__main__':
    n_l = [6, 7, 6]
    s_l = [4, 3, 4]
    a_l = [6, 4, 5]
    b_l = [2, 1, 6]
    fares_list = [[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
                  [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
                  [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]
    for i in range(3):
        print(solution(n_l[i], s_l[i], a_l[i], b_l[i], fares_list[i]))
