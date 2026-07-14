class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checklist = defaultdict(list)

        for word in strs:
            sorted_label = ''.join(sorted(word))

            checklist[sorted_label].append(word)

        return list(checklist.values())