class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        lastIndex = {}
        for i in range(n):
            lastIndex[s[i]] = i

        taken = set()
        result = []

        for i in range(n):
            ch = s[i]

            if ch in taken:
                continue

            while result and result[-1] > ch and lastIndex[result[-1]] > i :
                taken.remove(result.pop())

            result.append(ch)
            taken.add(ch)

        return "".join(result)
