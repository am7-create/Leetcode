class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"

        for i in range(1,n):

            current = res[0]
            count = 1
            newdata = ""
            for c in res[1:]:
                if c == current:
                    count +=1
                else:
                    newdata = newdata + str(count) + current
                    current = c
                    count = 1
                    
            res = newdata + str(count) + current
        return res

        