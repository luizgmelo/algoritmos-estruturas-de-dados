from binary_search import binary_search

def exponential_search(nums, target):
    length = len(nums)

    if length == 0:
        return -1

    if nums[0] == target:
        return 0

    right = 1
    while right < length and nums[right] < target:
        right *= 2

    if right > length:
        right = length-1

    if nums[right] == target:
        return right

    return binary_search(nums, target, right//2, min(right,length-1))


if __name__ == "__main__":
    exponential_search([], 5)
    exponential_search([1,2,3,4,5], 6)
    exponential_search([1,2,3,4,5,6,7,8,9,10], 6)
    exponential_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 6)

