a=input("enter the letter: ")
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("letter is vowel")
elif a.isdigit():
    print("letter is a digit")
else:
    print("letter is consonant")    