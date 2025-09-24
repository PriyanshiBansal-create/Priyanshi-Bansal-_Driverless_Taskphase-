# Define a class for handling a list of strings
class string_list:

    def __init__(self,list):
        self.list=list
    
    # Selection sort function (case-insensitive sorting)
    def string_sorter(self):
        l=self.list
        length=len(self.list)
        
        for i in range(length-1):
            minindx=i
            
            for j in range(i+1,length):
                if l[j].lower() < l[minindx].lower():
                    minindx=j
            
            l[i] , l[minindx] = l[minindx] , l[i]
        
        return l
    
    # Binary search function (works only on sorted list)
    def binarysearch(self,key):
        l=self.list
        low = 0
        high = len(l)-1
       
        while low <= high:
            mid=(low+high)//2
            
            if l[mid]==key:
                return mid
            elif l[mid]<key:
                low=mid+1
            elif l[mid]>key:
                high=mid-1
        
        else:
            return "Not Found"  


# ------------------- Main Program -------------------

strings=[]   
n=int(input("Enter number of strings:"))

# Input n strings from user
for i in range(n):                         
    s=input("Enter string:")
    strings.append(s)


# Create object of StringList class
obj=string_list(strings)


#sort the list by calling the string_sorter() fuction in class string_list()
sorted_list=obj.string_sorter()
print(sorted_list)

element=input("Enter element to find :")


# Perform binary search by calling the binarysearch() function in class string_list()
index=obj.binarysearch(element)


if str(index).isdigit():
    print("Position of the given element is :",index+1)

else:
    print("Position of the given element is :",index)