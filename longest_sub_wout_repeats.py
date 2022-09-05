class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [0] * 128
        
        strt = 0
        end = 0
        res = 0
        
        while end < len(s):
            chars[ord(s[end])] += 1
            
            while chars[ord(s[end])] > 1:
                chars[ord(s[strt])] -= 1
                strt +=1
                
            res = max(res, end - strt + 1)
            
            end += 1
            
        return res
  
