class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        """
        # First code I made w str method
        num = str(x)
        
        tail = len(num)//2
        head = tail
        
        if len(num) % 2 == 0:
            head = head - 1
            
        while num[head] == num[tail]:
            head = head - 1
            tail = tail + 1
            
            if head < 0:
                return True
            
        return False
        """
        # Method w/out casting int as str
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        left = x
        right = 0
        
        while right < left:
            right = right * 10 + (left % (10))
            left = left//10

        return right == left or right//10 == left
       
