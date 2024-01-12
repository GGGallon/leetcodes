# 与搜索旋转排序数组.py相比，数组会出现重复数字


def fun(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue
        if nums[left] <= nums[mid]:  # 左边有序
            if nums[left] <= target < nums[mid]:  # 说明前半段有序且目标值在前半段-->可对前半段二分查找
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] <= nums[right]:  # 右边有序
            if nums[mid] < target <= nums[right]:  # 说明后半段有序且目标值在后半段-->可对后半段二分查找
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(fun([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13))
