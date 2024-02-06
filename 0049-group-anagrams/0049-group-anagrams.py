class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_groups = {}
        for word in strs:
            key =tuple(sorted(word))
            if key in my_groups:
                my_groups[key].append(word)
            else:
                my_groups[key] = [word]
        result = list(my_groups.values())
        return result