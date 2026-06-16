class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range (len(strs[0])):
            char = strs[0][i]

            for j in strs:
                if i>=len(j) or j[i] != char:
                    return strs[0][:i]
        
        return strs[0]