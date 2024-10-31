def partition(arr, low, high):
    # Choose the pivot
    pivot = arr[high]
    
    i = low - 1  # Index of smaller element
    
    # Traverse arr[low..high] and move all smaller
    # elements on the left side. Elements from low to i are smaller after every iteration
    for j in range(low, high):
        if sum_ascii(arr[j]) < sum_ascii(pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Move pivot after smaller elements and return its position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The QuickSort function implementation
def quick_sort(arr, low, high):
    if low < high:
        # p is the partition return index of pivot
        p = partition(arr, low, high)

        # Recursion calls for elements before and after the partition
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def sum_ascii(s):
    letters = ''.join(c for c in s if c.isalpha())  # Keeps only letters
    return sum(ord(c) for c in letters)

def sort_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Timing the quick sort
    import time
    start_time = time.time()
    quick_sort(lines, 0, len(lines) - 1)
    end_time = time.time()

    # Write sorted lines to the output file
    with open(output_file, 'w') as f:
        for line in lines:
            f.write(f"{line}\n")

    # Print the time taken
    print(f"Time taken to sort {input_file} using Quick Sort: {end_time - start_time} seconds")

# Function to print an array (optional for testing purposes)
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    import sys
    sort_file(sys.argv[1], sys.argv[2])
