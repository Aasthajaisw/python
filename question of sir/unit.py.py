unit=int(input("enter unit"))
total=charge=amount=0
if(unit<=50):
    amount=unit*0.50
elif(unit<50 and unit<=150):
    amount=unit*0.75
elif(unit<=150 and unit<=250):
    amount=unit*1.20
else:
    amount=unit*1.50
charge=amount*20/100
total=amount+charge
print("total bill is %d"%(total))
