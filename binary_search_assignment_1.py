def condition(mid):
    if nums[mid] == target:
        if mid > 0 and nums[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif nums[mid] < target:
        return 'left'
    else:
        return 'right'   

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

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1



def count_rotations_generic(nums):
    def condition(mid, hi):
        if mid > 0 and nums[mid] < nums[mid-1]:
            return 'found'
        elif nums[mid] < nums[hi]:
            return 'left'
        else:
            return 'right'
        
    return binary_search(0, len(nums)-1, condition)

def find_element(nums, query):
    def condition2(mid):
        if nums[mid] == query:
            if mid > 0 and nums[mid-1] == query:
                return 'left'
            else:    
               return 'found'
        elif nums[mid] > query:
            return 'left'
        else:
            return 'right'

    mid = count_rotations_binary(nums)

    if query == nums[mid]:
        return mid
    elif query > nums[mid] and query <= nums[-1]:
        return binary_search(mid, len(nums)-1, condition2)
    else:
        return binary_search(0, mid-1, condition2)

##
##print(count_rotations_linear([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
##print(count_rotations_binary([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
##print(count_rotations_generic([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
##print(count_rotations_generic([5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]))
print(find_element([5, 6, 9, 0, 2, 3, 4], 2))
print(count_rotations_binary([1,3]))
print(find_element([1,3], 3))
##print(binary_search(0, len([1,3]), 3))
