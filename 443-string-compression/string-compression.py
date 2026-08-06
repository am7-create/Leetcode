class Solution(object):
    def compress(self, chars):
        i = 0
        j = 0
        n = len(chars)

        while i < n :
            current = chars[i]
            count = 0

            while i < n and chars[i] == current:
                i += 1
                count += 1

            chars[j] = current
            j += 1

            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1

        return j