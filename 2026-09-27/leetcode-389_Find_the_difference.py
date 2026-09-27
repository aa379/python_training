class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff=sum(ord(i) for i in t)-sum(ord(j) for j in s)
        return chr(diff)
if __name__=="__main__":
    solver=Solution()
    data="abcde"
    data1="abcd"
    ans=solver.findTheDifference(data,data1)
    print(ans)