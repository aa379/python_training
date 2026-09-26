class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in a:
                return[a[diff],i]
            a[num]=i
        return []
if __name__=="__main__":
    solver=Solution()
    data=[2,7,11,15]
    target=9
    ans=solver.twoSum(data,target)
    print(ans)