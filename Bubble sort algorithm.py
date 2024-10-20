def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm."""

    n = len(arr)

    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [64, 37, 26, 12, 24, 11, 91]
print("Sorted array:", bubble_sort(arr))