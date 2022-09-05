class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 1:
            return strs[0]
        
        pre = ""
        
        cap = min([len(string) for string in strs])
        
        i = 0
        
        while i < cap and all([strs[0][i] == string[i] for string in strs[1:]]):
            pre = pre + strs[0][i]
            i+=1
            
        return pre
