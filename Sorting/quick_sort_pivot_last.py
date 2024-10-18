def partition(arr, left, right):
    pivot = arr[right]
    i = left-1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)


random = [9, 2, 4, 5, 8, 1, 6, 7, 10, 3]
reverse = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
duplicated = [2, 2, 2, 2, 1, 1, 1, 3, 3, 3]
sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before: ")
print(random)
print(reverse)
print(duplicated)
print(sorted)

quick_sort(random, 0, len(random)-1)
quick_sort(reverse, 0, len(random)-1)
quick_sort(duplicated, 0, len(random)-1)
quick_sort(sorted, 0, len(random)-1)

print("After:")
print(random)
print(reverse)
print(duplicated)
print(sorted)

