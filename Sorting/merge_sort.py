from random import shuffle

def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if (start < end):
        mid = (end + start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)
    return arr

def merge(arr, start, mid, end):
    helper = arr[:]
    i, j, k = start, mid+1, start
    while (i <= mid and j <= end):
        if helper[i] <= helper[j]:
            arr[k] = helper[i]
            i += 1
        else:
            arr[k] = helper[j]
            j += 1
        k += 1
    
    while (i <= mid):
        arr[k] = helper[i]
        i += 1
        k += 1

    while (j <= end):
        arr[k] = helper[j]
        j += 1
        k += 1

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
