# class Solution(object):
#     def threeSum(self, nums):
#         # 三数之和转换为两数之和
#         n = len(nums)
#         nums.sort()
#         ans = []

#         if not nums:
#             return None

#         for i, each in enumerate(nums):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             target = 0 - each

#             left = i + 1
#             right = n - 1

#             while left < right:
#                 sum = nums[left] + nums[right]
#                 if sum == target :
#                     ans.append([each, nums[left], nums[right]])
#                     left += 1
#                     right -= 1
#                     # 去重
#                     while left < right and  nums[left] == nums[left-1]:
#                         left += 1
#                     while left  < right and  nums[right] == nums[right+1]:
#                         right -= 1
#                 elif sum < target:
#                     left += 1
#                 else:
#                     right -=1 
            
#         return ans
                    
                    
                    
# if __name__ == '__main__':
#     s = Solution()
#     nums = [1,2,0,1,0,0,0,0]

#     print(s.threeSum(nums))

for each in range(1,9):
    print(each)