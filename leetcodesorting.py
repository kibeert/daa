import time

start_time =time.time()
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively apply merge_sort on both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage:
arr = [20, 27, 43, 4, 79, 8, 15]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
end_time = time.time()
elapsed_time =end_time - start_time
print("Elapsed time:{} seconds".format(elapsed_time))
