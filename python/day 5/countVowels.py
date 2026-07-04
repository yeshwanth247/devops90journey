count=0
def count_vowels(s):
    s.lower()
    global count
    for i in range(len(s)):
        if s[i] in "aeiou":
            count+=1
    return count      

result=count_vowels("aeiou") 
print(result) 
 

