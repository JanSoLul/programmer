from math import ceil

def solution(s):
    s_len = len(s)

    def split_string(n):
        splits = []
        for i in range(ceil(s_len/n)):
            end = (i+1) * n
            if end > s_len:
                end = s_len
            splits.append(s[i*n : end])
        new_string = ''
        total_repeat_count = 0
        for i in range(len(splits)):
            index = i+total_repeat_count
            if index >= len(splits):
                break
            repeat_count = 0
            for j in range(index+1, len(splits)):
                if splits[index] != splits[j]:
                    break
                repeat_count += 1
            if repeat_count > 0:
                total_repeat_count += repeat_count
                new_string += str(repeat_count+1) + splits[index]
            else:
                new_string += splits[index]
        return len(new_string)

    min_len = s_len
    for i in range(1, s_len//2+1):
        min_len = min(min_len, split_string(i))

    answer = min_len
    return answer

if __name__ == '__main__':
    s_l = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    for i in range(len(s_l)):
        print(solution(s_l[i]))