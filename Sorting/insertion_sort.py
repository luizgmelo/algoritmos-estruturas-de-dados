from random import shuffle

def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

if __name__ == "__main__":
    order = list(range(10))
    reverse = list(range(9, -1, -1))
    random = list(range(10))
    shuffle(random)
    insertion_sort(order)
    insertion_sort(reverse)
    insertion_sort(random)
    print('order', order)
    print('reverse', reverse)
    print('random', random)
