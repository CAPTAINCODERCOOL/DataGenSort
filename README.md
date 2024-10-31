DataGenSort
Overview
DataGenSort is a Python-based tool designed to facilitate dataset generation and sorting algorithm testing. It combines random words from an input list to create unique datasets of customizable sizes. These datasets can then be sorted using various algorithms, including Insertion Sort, Merge Sort, and Quick Sort, based on the ASCII value sum of the characters in each line. DataGenSort enables users to analyze sorting efficiency and compare algorithm performance across datasets of different sizes.

Features
Dataset Generation: Create datasets of random word combinations, separated by hyphens.
Sorting Algorithms: Sort datasets using Insertion Sort, Merge Sort, and Quick Sort.
Sorting Criteria: Sort data based on the sum of ASCII values of each line.
Customizable Sizes: Generate datasets of 40, 1000, or 6000 lines for testing.
Requirements
Python 3.x: Ensure Python is installed on your system.
Random word file: Input file containing words, each on a new line, which will be combined to create the datasets.
Files in This Project
generatedata.py: Script to generate datasets with random word combinations.
quicksort.py: Implements the Quick Sort algorithm.
mergesort.py: Implements the Merge Sort algorithm.
insertionsort.py: Implements the Insertion Sort algorithm.
README.md: Documentation for the project.
Dataset Generation
How It Works
The generatedata.py script reads words from a specified file and combines them randomly into unique datasets. Each line in the generated dataset contains a combination of three random words separated by hyphens.

Command Usage
To generate a dataset, use the following command format:

bash
Copy code
python generatedata.py <filename> <n>
<filename>: The name of the input file containing the list of words (one per line).
<n>: The number of lines in the generated dataset (40, 1000, or 6000).
Example:

bash
Copy code
python generatedata.py words.txt 1000
This command will generate a file named output_dataset.txt containing 1000 lines of word combinations from the input list.

Example Output
The generated dataset will look like this:

plaintext
Copy code
1 apple-ball-cat
2 dog-fish-goat
...
n word1-word2-word3
Sorting Algorithms
DataGenSort includes three sorting algorithms: Quick Sort, Merge Sort, and Insertion Sort. Each dataset can be sorted based on the ASCII sum of characters in each line. This unique sorting criterion allows for testing of algorithm performance on text-based data.

Sorting Scripts and Usage
Each sorting script has a specific function and requires two arguments: the input file (generated dataset) and the output file (where sorted data will be saved).

1. Quick Sort
Run Quick Sort with the following command:

bash
Copy code
python quicksort.py <input_dataset> <output_file>
Example:

bash
Copy code
python quicksort.py arr1000.txt sorted_quick.txt
2. Merge Sort
Run Merge Sort with the following command:

bash
Copy code
python mergesort.py <input_dataset> <output_file>
Example:

bash
Copy code
python mergesort.py arr1000.txt sorted_merge.txt
3. Insertion Sort
Run Insertion Sort with the following command:

bash
Copy code
python insertionsort.py <input_dataset> <output_file>
Example:

bash
Copy code
python insertionsort.py arr1000.txt sorted_insertion.txt
Sorting Criteria
The sorting is based on the sum of ASCII values of characters in each line. For instance, if the line is apple-ball-cat, the ASCII sum of all characters (a=97, p=112, etc.) will be calculated, and sorting will be performed based on these sums.

Code Explanation
1. generatedata.py
Imports:

random: Used to select words randomly for each line.
sys: Allows for handling command-line arguments.
Functions:

load_words(filename): Reads words from a specified file and returns them as a list.
generate_dataset(words, n, output_file): Generates the dataset using randomly chosen words from the list.
Main Block:

Checks command-line arguments.
Loads the words from the specified file.
Calls generate_dataset to create and save the dataset.
2. quicksort.py
Imports:

sys: For handling command-line arguments.
Functions:

ascii_sum(line): Calculates the ASCII sum of characters in a line.
quick_sort(arr, low, high): Recursive Quick Sort implementation.
sort_file(input_file, output_file): Loads the dataset, applies Quick Sort based on ASCII sums, and saves the sorted dataset.
3. mergesort.py
Imports:

sys: For handling command-line arguments.
Functions:

ascii_sum(line): Calculates the ASCII sum of characters in a line.
merge_sort(arr): Recursive Merge Sort implementation.
sort_file(input_file, output_file): Loads the dataset, applies Merge Sort based on ASCII sums, and saves the sorted dataset.
4. insertionsort.py
Imports:

sys: For handling command-line arguments.
Functions:

ascii_sum(line): Calculates the ASCII sum of characters in a line.
insertion_sort(arr): Iterative Insertion Sort implementation.
sort_file(input_file, output_file): Loads the dataset, applies Insertion Sort based on ASCII sums, and saves the sorted dataset.
Example Workflow
Generate Dataset:

bash
Copy code
python generatedata.py words.txt 1000
Sort Using Quick Sort:

bash
Copy code
python quicksort.py output_dataset.txt sorted_quick.txt
Sort Using Merge Sort:

bash
Copy code
python mergesort.py output_dataset.txt sorted_merge.txt
Sort Using Insertion Sort:

bash
Copy code
python insertionsort.py output_dataset.txt sorted_insertion.txt
Each sorting script will output a sorted version of output_dataset.txt into the specified output file, based on the ASCII sum sorting criterion.

Time Complexity Analysis
Insertion Sort: 
𝑂
(
𝑛
2
)
O(n 
2
 ) average time complexity, suitable for small datasets.
Merge Sort: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) average time complexity, efficient for larger datasets.
Quick Sort: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) average time complexity, with a 
𝑂
(
𝑛
2
)
O(n 
2
 ) worst case; generally faster in practice with randomized data.
Example Files Generated
Command	Output File	Description
python generatedata.py words.txt 40	arr40.txt	40-line dataset
python quicksort.py arr40.txt sorted.txt	sorted.txt	Quick Sort on 40-line dataset
python mergesort.py arr1000.txt sorted_merge.txt	sorted_merge.txt	Merge Sort on 1000-line dataset
python insertionsort.py arr6000.txt sorted_insertion.txt	sorted_insertion.txt	Insertion Sort on 6000-line dataset
Conclusion
DataGenSort provides a versatile way to generate random word datasets and sort them using different algorithms. By sorting based on ASCII sums, this project allows for comparative analysis of sorting algorithms, offering a practical approach to testing and understanding sorting efficiencies in real-world scenarios.

Troubleshooting
Common Errors
IndexError: list index out of range: This usually happens if you forget to pass the correct arguments when running the scripts. Double-check the command format for each script.

FileNotFoundError: Ensure the input file exists and is in the same directory as the script or provide the correct path.

Invalid Input: Ensure the input file has words separated by lines, and the number of lines specified in generatedata.py matches your requirements.

License
This project is open-source and available for free use and modification.
