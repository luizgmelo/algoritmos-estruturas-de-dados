def binary_search(nums, target, left=0, right=None):
    steps = 0
    if right is None:
        right = len(nums)

    while left < right:
        steps += 1
        mid = int((right+left)/2)
        if nums[mid] == target:
            print("steps:", steps)
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid

    return -1

if __name__ == "__main__":
    binary_search([1,2,3,4,5], 5)
    binary_search([1,2,3,4,5,6,7,8,9,10], 5)
    binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 5)


