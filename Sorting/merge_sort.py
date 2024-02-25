from random import shuffle

def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if (end - start > 1):
        mid = (end + start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)
    return arr

def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i, j = 0, 0
    for k in range(start, end):
        if i >= len(left):
            arr[k] = right[j]
            j += 1
        elif j >= len(right):
            arr[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

if __name__ == "__main__":
    order = list(range(10))
    reverse = list(range(9, -1, -1))
    random = list(range(10))
    shuffle(random)
    merge_sort(order)
    merge_sort(reverse)
    merge_sort(random)
    print('order', order)
    print('reverse', reverse)
    print('random', random)
