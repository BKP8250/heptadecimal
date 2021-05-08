def split(word):
    return list(word) 
def ini(k): 
   sum1=0 
   for i in range(0,len(k)): 
       if(k[i].isnumeric()): 
          posi=17i 
          hepti=posi*int(k[i]) 
          sum1+=hepti return(sum1) 
 def strin(m): 
     sum=0 
     for i in range(0,len(m)): 
        if(m[i].isalpha()): 
         for j in range(0,7): 
            if(m[i]==l[j]): 
              hept=17i pos=10+j 
              num=hept*pos 
              sum+=num 
            else: continue return(sum)

a=input("enter the string") 
b=split(a[::-1]) 
l=['A','B','C','D','E','F','G'] 
c=ini(b)+strin(b) 
print(c)

