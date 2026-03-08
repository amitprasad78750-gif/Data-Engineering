
class palindrome:
    def findPalindrome(self,nums):

        if nums < 0:
            return "Not Plaindrome"
        originalNo = nums
        oppNums = 0
        while nums > 0:
            oppNums = oppNums * 10 + nums % 10
            print(oppNums)

            nums = nums //10

        if originalNo == oppNums:
            return "Palindrome"

output= palindrome().findPalindrome(121)
print(output)