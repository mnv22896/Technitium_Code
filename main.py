from collections import defaultdict
import math
quantity=['large','Xlarge','X2large','X4large','X8large','X10large']
qua=[10,20,40,80,160,320]
India_qua=[10,40,80,160,320]
china_qua=[10,20,80,160]
New_quantity=['large','Xlarge','X2large','X4large','X8large','X10large']
India_quantity=['large','Xlarge','X2large','X4large','X8large','X10large']
china_quantity=['large','Xlarge','X4large','X8large']
New_rate=[120,230,450,774,1400,2820]
India_rate=[140,413,890,1300,2970]
China_rate=[110,200,670,1180]
ans=defaultdict()
capacity=1150
hour=1 
minimum=defaultdict()
global p
p=100000
def cost(capacity,hour,qua,quantity,ans):
    global p
    for i in range(0,len(qua)):
        
        
        if capacity%qua[-i-1] ==0:
            ans[quantity[-i-1]]=int(math.floor(capacity/qua[-i-1])) 
            output=amount(ans)
            if p > output :
                p=output
                minimum[p]=ans
            ans[quantity[-i-1]]=0
            return 
            
        elif capacity > qua[-i-1]:
            ans[quantity[-i-1]]=int(math.floor(capacity/qua[-i-1])) 
            cost(capacity%qua[-i-1],hour,qua[:-i-1],quantity[:-i-1],ans)
            ans[quantity[-i-1]]=0

            
def amount(ans):
    sum=0
    for i in ans:
        sum=sum + (ans[i] * New_rate[New_quantity.index(i)])
    return sum    
t=cost(capacity,hour,qua,quantity,ans)

print(p)
