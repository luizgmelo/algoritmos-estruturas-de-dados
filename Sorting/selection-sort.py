from random import shuffle

def selection_sort(arr):
    length = len(arr)
    for i in range(0, length):
        min_index = i 
        for j in range(i + 1, length):
            if (arr[min_index] > arr[j]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    array = list(range(10))
    shuffle(array)
    print(array)
    selection_sort(array)
    print(array)
