class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longPalin = ''
        for i in range(len(s)):
            head = i
            tail = i
            
            while head >= 0 and tail < len(s) and s[head] == s[tail]:
                if tail - head + 1 > len(longPalin):
                    longPalin = s[head:tail+1]
                    
                head = head - 1
                tail = tail + 1
                

                    
            if i < len(s) - 1:
                head = i
                tail = i + 1

                while head >= 0 and tail < len(s) and s[head] == s[tail]:
                    if tail - head + 1 > len(longPalin):
                        longPalin = s[head:tail+1]
                        
                    head = head - 1
                    tail = tail + 1

                        
        return longPalin
      
