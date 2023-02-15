a=int(input("enter amount"))
b=100
a=a-100
tt=a//2000
a=a-(tt*2000)
fh=a//500
a=a-(fh*500)
th=a//200
a=a-(th*200)
hh=a//100
hh=hh+1
tmp=('''no two thousand:{}\n five hundred:{}\n two hundred:{}\n hundred:{}\n)''')
out=tmp.format(tt,fh,th,hh)
print(out)
