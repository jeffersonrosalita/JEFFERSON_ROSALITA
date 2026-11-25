def filter_and_deduplicate(full_name: str) -> list[str]:
    """Keep only alphabetic letters (excluding symbols/spaces) and discard duplicates."""
    unsorted_letters: list[str] = []
    seen: set[str] = set()

    for ch in full_name:
        # Exclude symbols, numbers, spaces, and punctuation
        if ch.isalpha():
            letter = ch.upper()
            if letter not in seen:
                seen.add(letter)
                unsorted_letters.append(letter)

    return unsorted_letters


def bubble_sort(arr: list[str]) -> list[str]:
    """Sort a list of letters in ascending alphabetical order using Bubble Sort."""
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break

    return sorted_arr


def main() -> None:
    full_name = "ROSALITA"

    unsorted_array = filter_and_deduplicate(full_name)
    sorted_array = bubble_sort(unsorted_array)

    print(f"Input Name:     {full_name}")
    print(f"Unsorted Array: {unsorted_array}")
    print(f"Sorted Array:   {sorted_array}")


if __name__ == "__main__":
    main()