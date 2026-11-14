class Solution(object):
    def addSpaces(self, s, spaces):
        res = []
        j = 0
        i = 0
        n = len(s)
        m = len(spaces)
        while i < n:
            if j < m and i == spaces[j]:
                res.append(" ")
                j += 1
            res.append(s[i])
            i += 1
        return "".join(res)

