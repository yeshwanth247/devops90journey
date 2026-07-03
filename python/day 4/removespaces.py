word=input("enter the name: ")
word=word.strip()
wordAS=" "
for i in range(len(word)):
    if word[i]==" ":
        continue
    wordAS+=word[i]

print(wordAS)