class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        i = 0
        while i <= n - m:
            if haystack[i:i + m] == needle:
                return i
            i += 1
        return -1

