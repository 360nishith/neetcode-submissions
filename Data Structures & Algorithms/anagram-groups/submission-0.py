class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap={}

        for word in strs:
            key="".join(sorted(word))

            if key not in anagrammap:
                anagrammap[key]=[]
            anagrammap[key].append(word)

        return list(anagrammap.values())