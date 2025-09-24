# Take input for number of strings to be entered
n_strings=int(input("Enter number of strings:"))


# Initialize an empty list to store the input strings
list_strings=[]


# Loop to take 'n' strings from the user
for i in range(n_strings):
    s=input("Enter string to input:")
    list_strings.append(s)


# Initialize an empty dictionary to store alphabet frequencies
alpha_dic={}


for s in list_strings:
    
    for i in s:
        
        if i.isalpha():
            
            if i.lower() in alpha_dic:
                alpha_dic[i.lower()]+=1       # Increment count if already present
            
            else:
                alpha_dic[i.lower()]=1        # Add new key if not present


print(alpha_dic)