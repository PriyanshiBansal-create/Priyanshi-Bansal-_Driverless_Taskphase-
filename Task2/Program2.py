# Create hash table with 10 empty lists
hash_table = []
for i in range(10):
    hash_table.append([])

# Input numbers
n = int(input("Enter number of integers: "))
numbers = []
for i in range(n):
    num = int(input("Enter number:"))
    numbers.append(num)

# Insert using modulo 10
for num in numbers:
    index = num % 10 
    hash_table[index].append(num)

# Print hash table
print("Hash Table:")
for i in range(10):
    print("Index",i,":", hash_table[i])