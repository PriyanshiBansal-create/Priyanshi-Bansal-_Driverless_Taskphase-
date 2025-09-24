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


# ---------------- MAIN PROGRAM ---------------- #

# Initialize an empty list to store input strings
strings=[]

n=int(input("Enter number of strings:"))

#loop to take n strings from the user
for i in range(n):
    s=input("Enter string:")
    strings.append(s)


# Create an object of string_list class
obj=string_list(strings)


# Call the sorting function
sorted_list=obj.string_sorter()


print(sorted_list)
