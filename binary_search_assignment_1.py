def count_rotations_linear(nums):
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position

        position += 1

    return 0

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1 

    while lo <= hi:
        mid = (lo + hi) // 2
        #print(mid , lo , hi)

        if mid > 0 and nums[mid] < nums[mid-1]:
            return mid
        elif nums[mid] < nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 0
        



print(count_rotations_linear([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
print(count_rotations_binary([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
