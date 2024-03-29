# 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
def fun(nums, target):
    index = 1024
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] >= target:
            if index > mid:
                index = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return index


data = [5,7,7,8,8,10]
print(fun(data, 8))
