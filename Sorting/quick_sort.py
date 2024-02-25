from random import shuffle

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        mid = (start+end)//2
        pivot = arr[mid]
        index = partition(arr, start, end, pivot)
        quick_sort(arr, start, index-1)
        quick_sort(arr, index, end)
    return arr

def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

if __name__ == "__main__":
    order = list(range(10))
    reverse = list(range(9, -1, -1))
    random = list(range(10))
    shuffle(random)
    quick_sort(order)
    quick_sort(reverse)
    quick_sort(random)
    print('order', order)
    print('reverse', reverse)
    print('random', random)


