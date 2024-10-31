def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if sum_ascii(L[i]) <= sum_ascii(R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def sum_ascii(s):
    letters = ''.join(c for c in s if c.isalpha())  # Keeps only letters
    return sum(ord(c) for c in letters)

# To read the dataset file, sort it, and write to output
def sort_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Timing the merge sort
    import time
    start_time = time.time()
    merge_sort(lines, 0, len(lines) - 1)
    end_time = time.time()

    # Write sorted lines to the output file
    with open(output_file, 'w') as f:
        for line in lines:
            f.write(f"{line}\n")

    # Print the time taken
    print(f"Time taken to sort {input_file} using Merge Sort: {end_time - start_time} seconds")

if __name__ == "__main__":
    import sys
    sort_file(sys.argv[1], sys.argv[2])
