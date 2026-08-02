class Solution(object):
    def solve(self, index, total, subset, candidates,target, result):

        if total == target:
            result.append(subset[:])
            return

        if total > target:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue

            if total + candidates[i] > target:
                break

            subset.append(candidates[i])

            self.solve(
                i+1, 
                total+candidates[i], 
                subset, 
                candidates, 
                target, 
                result
            )

            subset.pop()


    def combinationSum2(self, candidates, target):
        result = []

        candidates.sort()

        self.solve(0, 0, [], candidates, target, result)

        return result
       