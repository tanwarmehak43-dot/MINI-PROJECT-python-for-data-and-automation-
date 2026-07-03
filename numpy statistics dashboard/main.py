import numpy as np

numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

arr = np.array(numbers)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))