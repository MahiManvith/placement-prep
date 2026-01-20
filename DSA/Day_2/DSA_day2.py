arr_nums = [1, 4, 7, 10, 13]
current_nums = 0
new_nums = []

for i in arr_nums:
    current_nums += i
    new_nums.append(current_nums)

print("Sum of  Array_Num :", new_nums)

#time complexity = O(n)