

#!/usr/bin/python

i=0

aif=[15,47,71,111,123,152,166,226,310,320]
sif=[43,36,34,30,38,40,31,29,36,30]
di=[]
ci=[]

while (i<10):

      ai = aif[i]
      if (len(ci)!=0):
        if (ai < ci[i-1]):
           di.insert(i , ci[i-1]-ai)
        else:
	   di.insert(i , 0)
      else:
        di.insert(i , 0)

      si = sif[i]
      ci.insert(i , ai+di[i]+si)
      i = i+1

print "di = " + str(di)
print "ci = " + str(ci)
