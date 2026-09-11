class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        mini = float('inf')

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                dist = min(dist, n - dist)
                mini = min(mini, dist)

        if mini == float('inf'):
            return -1

        return mini