def prepare_name_array(full_name: str) -> list[str]:
    """Exclude symbols/non-letters, discard duplicate letters, and build the unsorted array."""
    unsorted: list[str] = []
    seen: set[str] = set()

    for ch in full_name:
        if ch.isalpha():
            letter = ch.upper()
            if letter not in seen:
                seen.add(letter)
                unsorted.append(letter)

    return unsorted


def bubble_sort(arr: list[str]) -> list[str]:
    """Repeatedly compare adjacent elements and swap if out of order."""
    data = arr.copy()
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(arr: list[str]) -> list[str]:
    """Repeatedly find the smallest element from the unsorted portion and place it next."""
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def insertion_sort(arr: list[str]) -> list[str]:
    """Build a sorted subarray one element at a time by shifting larger items right."""
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def merge_sort(arr: list[str]) -> list[str]:
    """Divide and conquer: split into halves, sort recursively, and merge."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged: list[str] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: list[str]) -> list[str]:
    """Divide and conquer: partition elements around a pivot and sort halves recursively."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def timsort(arr: list[str]) -> list[str]:
    """Hybrid of Insertion Sort on runs and Merge Sort to combine sorted runs."""
    min_run = 4
    data = arr.copy()
    n = len(data)

    # Sort small runs with Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        for i in range(start + 1, end):
            key = data[i]
            j = i - 1
            while j >= start and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

    # Merge sorted runs (like Merge Sort)
    size = min_run
    while size < n:
        for left_start in range(0, n, 2 * size):
            mid = min(n, left_start + size)
            right_end = min(n, left_start + 2 * size)
            if mid < right_end:
                left = data[left_start:mid]
                right = data[mid:right_end]
                i = j = 0
                k = left_start
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        data[k] = left[i]
                        i += 1
                    else:
                        data[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    data[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    data[k] = right[j]
                    j += 1
                    k += 1
        size *= 2

    return data


def main() -> None:
    full_name = "ROSALITA,JEFFERSON O."
    unsorted_array = prepare_name_array(full_name)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Timsort": timsort,
    }

    print(f"Input Name:     {full_name}")
    print(f"Unsorted Array: {unsorted_array}\n")

    for name, fn in algorithms.items():
        sorted_array = fn(unsorted_array)
        print(f"{name}:")
        print(f"  Unsorted: {unsorted_array}")
        print(f"  Sorted:   {sorted_array}")


if __name__ == "__main__":
    main()