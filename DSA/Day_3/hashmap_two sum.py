def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return[seen[diff], i]
        seen[num] = i

print(two_sum([1, 2, 4, 5, 6], 9))

# time complexity : O(n)
# space complexity : O(n)