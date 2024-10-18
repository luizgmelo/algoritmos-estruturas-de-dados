from random import shuffle

def bubble_sort(arr):
    length = len(arr)
    for _ in range(length - 1):
        is_order = True
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                is_order = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if is_order:
            break

        length -= 1

    return arr

if __name__ == "__main__":
    order = list(range(10))
    reverse = list(range(9, -1, -1))
    random = list(range(10))
    shuffle(random)
    bubble_sort(order)
    bubble_sort(reverse)
    bubble_sort(random)
    print('order', order)
    print('reverse', reverse)
    print('random', random)


