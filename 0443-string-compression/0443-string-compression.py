class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        index = 0
        i = 0

        while i < n:
            ch = chars[i]
            count = 0

            while i < n and chars[i] == ch:
                count += 1
                i += 1

            chars[index] = ch
            index += 1

            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1
        return index