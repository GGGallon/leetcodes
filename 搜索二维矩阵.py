# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
#     每行中的整数从左到右按非严格递增顺序排列。
#     每行的第一个整数大于前一行的最后一个整数。
#
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

def searchMatrix(matrix, target) -> bool:
    height = len(matrix)
    width = len(matrix[0])
    total = width * height
    left = 0
    right = total - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid // width][mid % width] == target:
            return True
        if matrix[mid // width][mid % width] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


print(searchMatrix([[1,1]], 2))
