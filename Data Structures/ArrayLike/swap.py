def swap_items(arr: list, index1: int, index2: int) -> list:
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr

arr = [10, 20, 30, 40]

result = swap_items(arr, 1, 3)

print(result)