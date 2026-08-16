class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        max_right = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_right

            if temp > max_right:
                max_right = temp

        return arr