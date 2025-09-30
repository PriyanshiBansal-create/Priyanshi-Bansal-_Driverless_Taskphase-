# Insert number in sorted order using binary search
def binary_insert(list, num):
    
    low=0
    high=len(list)-1
    
 
    while low <= high:
        mid=(low + high)//2
        
        if list[mid] < num:
            low=mid+1
        else:
            high=mid-1
    
 
    list.insert(low, num)

# Initialize hash table with 10 empty lists
hash_table = []
for i in range(10):
    hash_table.append([])

# Input numbers
n=int(input("Enter number of integers: "))
numbers=[]
for i in range(n):
    num=int(input("Enter number:"))
    numbers.append(num)

# Insert numbers into hash table in sorted order
for num in numbers:
    index=num%10 
    binary_insert(hash_table[index],num)

# Print hash table
print("Hash Table:")
for i in range(10):
    print("Index",i,":", hash_table[i])
