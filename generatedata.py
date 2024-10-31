import random
import sys

# Function to load words from a file
def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to generate the dataset
def generate_dataset(words, n, output_file="output_dataset.txt"):
    with open(output_file, 'w') as file:
        for i in range(1, n+1):
            # Randomly choose 3 words and join them with '-'
            w1, w2, w3 = random.sample(words, 3)
            line_content = f"{w1}-{w2}-{w3}"
            file.write(f"{i} {line_content}\n")

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python generatedata.py <filename> <n>")
        sys.exit(1)

    filename = sys.argv[1]  # File containing the words (4_letter_words_rand.txt)
    n = int(sys.argv[2])    # Number of lines to generate (40, 1000, or 6000)

    words = load_words(filename)  # Load the words from the file

    # Generate the dataset with 'n' lines
    generate_dataset(words, n)
    print(f"Dataset with {n} lines generated in 'output_dataset.txt'.")
