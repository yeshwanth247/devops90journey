name=input("enter the name:")
vowels=0
consonants=0
name=name.lower()
for i in range(len(name)):
    if name[i] in 'aeiou':
        vowels+=1
    else:
        consonants+=1

print("no.of vowels are:",vowels)    
print("no.of consonants are:",consonants)    