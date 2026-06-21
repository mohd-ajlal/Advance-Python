def square_items_with_tuples(lst: list[int]) -> list[tuple[int, int]]:
    return [(x, x * x) for x in lst]

out = square_items_with_tuples([1, 2, 3, 4])
print(out)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16)]