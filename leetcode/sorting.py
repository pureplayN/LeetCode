

def insertion_sort(nums):
    if not nums_need_sort(nums):
        return

    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j = j - 1


def quick_sort(nums):
    if not nums_need_sort(nums):
        return

    quick_sort_impl(nums, 0, len(nums) - 1)


def quick_sort_impl(nums, front, end):
    if front < end:
        mid = partition(nums, front, end)
        quick_sort_impl(nums, front, mid - 1)
        quick_sort_impl(nums, mid + 1, end)


def partition(nums, front, end):
    mid_item = nums[end]
    lt_end = front - 1
    for i in range(front, end):
        if nums[i] <= mid_item:
            lt_end += 1
            if lt_end != i:
                nums[i], nums[lt_end] = nums[lt_end], nums[i]
    nums[lt_end + 1], nums[end] = nums[end], nums[lt_end]
    return lt_end + 1


def nums_need_sort(nums):
    if not nums:
        return False
    if not isinstance(nums, list):
        raise TypeError('nums must be a list!')
    else:
        return len(nums) > 1
