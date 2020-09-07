class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations, prefix = [], ""
        if not digits:
            return combinations
        self.doCombinations(prefix, combinations, digits)
        return combinations

    def doCombinations(self, prefix: str, combinations: List[str], digits: str):
        if len(prefix) == len(digits):
            combinations.append(prefix)
            return
        for i in self.keys[int(digits[len(prefix)])]:
            prefix += i
            self.doCombinations(prefix, combinations, digits)
            prefix = prefix[:-1]