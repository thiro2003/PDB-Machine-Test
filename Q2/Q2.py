# 2. Write a program that reads a large text file and:
# • Counts word frequency using dictionary
# • Removes stopwords
# • Displays top 10 frequent words
# • Handle file-related exceptions properly
# • Measure execution time using decorator

import time
import string
from collections import Counter


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\nExecution Time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper



@measure_time
def process_file(filename):

    stopwords = {
        "the", "is", "in", "and", "to", "of", "a", "an", "on", "for",
        "with", "as", "by", "at", "from", "that", "this", "it",
        "are", "was", "were", "be", "has", "have", "had"
    }

    word_freq = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
               
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.lower().split()

                for word in words:
                    if word not in stopwords:
                        word_freq[word] = word_freq.get(word, 0) + 1

        
        top_10 = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

        print("\nTop 10 Frequent Words:\n")
        for word, count in top_10:
            print(f"{word} : {count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")



if __name__ == "__main__":
    filename = input("Enter file name: ")
    process_file(filename)