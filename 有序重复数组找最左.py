# 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
def fun(nums, target):
    left = 0
    right = len(nums) - 1
    if len(nums) == 0:
        return [-1, -1]
    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            mid1 = mid2 = mid
            while mid1 != 0 and nums[mid1 - 1] == target:
                mid1 -= 1
            while mid2 != len(nums) - 1 and nums[mid2 + 1] == target:
                mid2 += 1
            return [mid1, mid2]
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return [-1, -1]


data = [1, 4]
print(fun(data, 4))
