def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

result=largest(5,6,8)    
result1=largest(0,6,2)    
result2=largest(5,1,3)    

print(result)
print(result1)
print(result2)
