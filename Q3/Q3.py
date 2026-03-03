import threading
import random
import statistics
import csv


numbers = []
even_numbers = []
results = {}

lock = threading.Lock()

numbers_generated = threading.Event()
even_filtered = threading.Event()

def generate_numbers():
    global numbers
    temp = [random.randint(1, 1000) for _ in range(100)]
    
    with lock:
        numbers.extend(temp)
        results["Total Numbers Generated"] = len(numbers)
    
    print("Thread 1: Generated 100 random numbers")
    numbers_generated.set()



def filter_even_numbers():
    numbers_generated.wait()
    
    global even_numbers
    with lock:
        even_numbers = [num for num in numbers if num % 2 == 0]
        results["Total Even Numbers"] = len(even_numbers)
    
    print("Thread 2: Filtered even numbers")
    even_filtered.set()


def calculate_statistics():
    even_filtered.wait()
    
    with lock:
        if len(even_numbers) > 0:
            mean_val = statistics.mean(even_numbers)
            std_dev = statistics.stdev(even_numbers) if len(even_numbers) > 1 else 0
            
            results["Mean of Even Numbers"] = round(mean_val, 2)
            results["Standard Deviation"] = round(std_dev, 2)
        else:
            results["Mean of Even Numbers"] = 0
            results["Standard Deviation"] = 0
    
    print("Thread 3: Calculated statistics")


t1 = threading.Thread(target=generate_numbers)
t2 = threading.Thread(target=filter_even_numbers)
t3 = threading.Thread(target=calculate_statistics)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


# storing data in csv
with open("thread_results.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=results.keys())
    writer.writeheader()
    writer.writerow(results)

print("All threads completed successfully.")
print("Results saved to thread_results.csv")