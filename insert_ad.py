def solution(play_time, adv_time, logs):
    def to_sec(t):
        hours, minutes, seconds = t.split(':')
        return int(hours)*3600 + int(minutes)*60 + int(seconds)
    play_time_sec = to_sec(play_time)+1
    total_view = [0 for _ in range(play_time_sec)]
    adv_time_sec = to_sec(adv_time)
    for i in logs:
        start, end = i.split("-")
        start_sec = to_sec(start)
        end_sec = to_sec(end)
        total_view[start_sec] += 1
        total_view[end_sec] -= 1
    for _ in range(2):
        for i in range(1, play_time_sec):
            total_view[i] += total_view[i-1]
    answer = ''
    max_view = 0
    save_time = 0
    for i in range(adv_time_sec-1, play_time_sec-1):
        if i >= adv_time_sec:
            tmp = total_view[i] - total_view[i-adv_time_sec]
            if tmp > max_view:
                save_time = i - adv_time_sec + 1
                max_view = tmp
        else:
            if total_view[i] > max_view:
                max_view = total_view[i]
                save_time = i - adv_time_sec + 1
    ret_hour = save_time // 3600
    ret_minute = (save_time % 3600) // 60
    ret_second = (save_time % 3600) % 60
    answer = '{:02d}:{:02d}:{:02d}'.format(ret_hour, ret_minute, ret_second)
    return answer

if __name__ == '__main__':
    play_time = "50:00:00"
    adv_time = "50:00:00"
    logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    print(solution(play_time, adv_time, logs))
