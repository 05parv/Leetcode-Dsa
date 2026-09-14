from collections import defaultdict, deque

class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parent = defaultdict(list)
        queue = deque([beginWord])
        distance = {beginWord: 0}
        found = False

        while queue and not found:
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word not in wordSet:
                            continue

                        if new_word not in distance:
                            distance[new_word] = distance[word] + 1
                            queue.append(new_word)
                            parent[new_word].append(word)

                        elif distance[new_word] == distance[word] + 1:
                            parent[new_word].append(word)

                        if new_word == endWord:
                            found = True

        if endWord not in distance:
            return []

        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for p in parent[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)

        return result