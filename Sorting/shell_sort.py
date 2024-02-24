from random import shuffle

def shell_sort(arr):
    length = len(arr)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            key = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > key:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = key
        gap //= 2
    return arr

if __name__ == "__main__":
    order = list(range(10))
    reverse = list(range(9, -1, -1))
    random = list(range(10))
    shuffle(random)
    shell_sort(order)
    shell_sort(reverse)
    shell_sort(random)
    print('order', order)
    print('reverse', reverse)
    print('random', random)

