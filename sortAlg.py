foo = [2, 7, 3, 1, 7, 4]

def selection_sort(nums):
    for i in range(len(nums)-1):
        k = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
    return nums
# print(selection_sort(foo))

def bubble_sort(nums):
    for i in range(len(nums), 0, -1):
        flag = False
        for j in range(i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag: break
    return nums
# print(bubble_sort(foo))

def insertion_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i-1
        while j > -1 and nums[j] > tmp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp
    return nums
# print(insertion_sort(foo))

def quick_sort(nums, left, right):
    if left >= right: return
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]: j -= 1
        while i < j and nums[i] <= nums[left]: i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]
    quick_sort(nums, left, i-1)
    quick_sort(nums, i+1, right)
# quick_sort(foo, 0, len(foo)-1)
# print(foo)

def merge(l, r):
    res = list()
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    if i < len(l): res += l[i:]
    if j < len(r): res += r[j:]
    return res

def merge_sort(nums):
    if len(nums) <= 1: return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)
# print(merge_sort(foo))

def bucket_sort(nums):
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]
    for n in nums:
        i = n // k
        buckets[i].append(n)
    for bkt in buckets:
        bkt.sort()
    i = 0
    for bkt in buckets:
        for n in bkt:
            nums[i] = n
            i += 1
    return nums
# print(bucket_sort(foo))
