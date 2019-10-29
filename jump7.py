a=1
while(a<=100):
    if(a%7==0 or a%10==7 or a//10==7):
        continue
    a+=1
    print(a)   