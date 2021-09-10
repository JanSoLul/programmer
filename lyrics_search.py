class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            current_node.count += 1
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0
        return current_node.count

def solution(words, queries):
    answer = []
    trie = [Trie() for _ in range(10001)]
    reverse_trie = [Trie() for _ in range(10001)]
    for word in words:
        word_len = len(word)
        trie[word_len].insert(word)
        reverse_trie[word_len].insert(''.join(reversed(word)))
    for query in queries:
        check = ''
        tmp = 0
        query_len = len(query)
        if query[0] == '?':
            for i in range(-1, -query_len-1, -1):
                if query[i] != '?':
                    check += query[i]
            tmp = reverse_trie[query_len].starts_with(check)
        else:
            for i in range(query_len):
                if query[i] != '?':
                    check += query[i]
            tmp = trie[query_len].starts_with(check)
        answer.append(tmp)

    return answer

if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))