import random as r

st = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&0123456789"
n = int(input("Enter the lenght of the password...:"))
pas = r.choices(st,weights=None,k=n)
pas_st = ""

for i in range(n):
    pas_st += str(pas[i])
print("Password is:- ",pas_st)
