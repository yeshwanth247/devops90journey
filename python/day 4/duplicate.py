word=input("enter the word: ")
arr=[]

for i in range(len(word)):
    for j in range(len(word)):
        if word[i]==word[j] and i!=j:
           arr.append(word[i])

print("duplicate characters in the word are: ",arr)           