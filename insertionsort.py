import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and sum_ascii(arr[j]) > sum_ascii(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sum_ascii(s):
    letters = ''.join(c for c in s if c.isalpha())  # Keeps only letters
    return sum(ord(c) for c in letters)

def sort_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    start_time = time.time()
    sorted_lines = insertion_sort(lines)
    end_time = time.time()

    # Write sorted lines to the output file
    with open(output_file, 'w') as f:
        for line in sorted_lines:
            f.write(f"{line}\n")

    # Print the time taken
    print(f"Time taken to sort {input_file}: {end_time - start_time} seconds")

if __name__ == "__main__":
    import sys
    sort_file(sys.argv[1], sys.argv[2])
