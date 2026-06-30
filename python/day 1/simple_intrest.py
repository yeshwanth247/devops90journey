#si=(p*t*r)/100

principal=float(input("enter the principal : "))
time=float(input("enter the time in years : "))
rate_of_intrest=float(input("enter the rate of interest: "))


simple_intrest=(principal*time*rate_of_intrest)/100

print("simple interst is:",simple_intrest)

amount=principal+simple_intrest

print("total amount = ",amount)