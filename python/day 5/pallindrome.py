def pallindrome(s):
    if s==s[::-1]:
        return True
    else: 
        return False
    
result=pallindrome("madam")
result1=pallindrome("121")

print(result)
print(result1)
