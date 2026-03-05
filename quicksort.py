#!/usr/bin/env python3
"""快速排序算法"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 测试
if __name__ == "__main__":
    nums = [3, 6, 8, 10, 1, 2, 1]
    print("原始数组:", nums)
    print("排序后:", quicksort(nums))
