import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(0.5)

# Task 2: Print letters
def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(f"Letter: {letter}")
        time.sleep(0.5)

# Task 3: Simulate a countdown
def countdown():
    for i in range(5, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(0.5)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=countdown)

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All tasks completed.")