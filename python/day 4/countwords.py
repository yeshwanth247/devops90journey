sentence=input("enter the sentence: ")
sentence=sentence.split()
count=0
for i in range(len(sentence)):
    if i<len(sentence):
        count+=1

print("no.of words in the sentence: ",count)