
from collections import defaultdict
import math
quantity=['large','Xlarge','X2large','X4large','X8large','X10large']
qua=[10,20,40,80,160,320]
New_rate={'large':120,'Xlarge':230,'Xlarge':450,'X4large':774,'X8large':1400,'X10large':2820}
India_rate={'large':140,'X2large':413,'X4large':890,'X8large':1300,'X10large':2970}
China_rate={'large':110,'Xlarge':200,'X4large':670,'X8large':1180}
ans=defaultdict()
capacity=1150
hour=1 
output=defaultdict(tuple)
p=0
def cost(capacity,hour,ouput,qua,quantity,ans):
    
   
    
    for i in range(0,len(qua)):
        print(qua[-i-1],capacity,i,qua)
        
        
        if capacity%qua[-i-1] ==0:
            ans[quantity[-i-1]]=int(math.floor(capacity/qua[-i-1])) 
            print(ans,capacity,quantity[-1-i])
            output[i]=ans
            ans[quantity[-i-1]]=0
            return 
            
        elif capacity > qua[-i-1]:
            ans[quantity[-i-1]]=int(math.floor(capacity/qua[-i-1])) 
            cost(capacity%qua[-i-1],hour,ouput,qua[:-i-1],quantity[:-i-1],ans)
            ans[quantity[-i-1]]=0
            
            
t=cost(capacity,hour,output,qua,quantity,ans)
print(output)
            
        
