a=int(input("enter year"))
b=((a%4==0)+(a%100!=0))+(a%400==0)
n=b%2
num="leap year"*(1-n)+"not leap year"*(n)
print(num)

