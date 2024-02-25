from random import shuffle

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)
    return arr


def partition(arr, start, end):
    pivot = arr[end]
    i = start

    for j in range(start, end):
        if (arr[j] <= pivot):
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]

    return i

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


