
class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = 0
        original =x
        while x>10:
            right = x%10
            x=x/10
            nums += right

        if original== nums:
            return True
        else:
            return False
    isPalindrome(121)    