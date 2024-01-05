def selection_sort(arr):

    for k in range(len(arr)):

        min_index = k   # --> elemento más pequeño

        for j in range(k + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[k], arr[min_index] = arr[min_index], arr[k]

nums = [64, 25, 12, 22, 11]

selection_sort(nums)

print(nums)#  11, 12, 22, 25, 64
