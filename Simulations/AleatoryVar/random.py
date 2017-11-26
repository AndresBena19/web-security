
#!/usr/bin/python


def fullP(p,n):
 full=[]
 m=29
 pe=0
 for a in range(p,n):
  p=1
  x=a


  while(x!=1):
    p=p+1
    x=(a*x)%m

  if(p==m-1):
   full.insert(pe,a)
   pe=pe+1
 return full,pe

if __name__ == "__main__":

     a,b=fullP(1,28)
     print a
