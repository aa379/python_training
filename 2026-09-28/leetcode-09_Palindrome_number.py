class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
if __name__=="__main__":
    solver=Solution()
    data=121
    ans=solver.isPalindrome(data)
    print(ans)