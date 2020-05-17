'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
quantity=[large,Xlarge,2Xlarger,4Xlarge,8Xlarge,10Xlarge]
qua=[10,20,:40,0,160,320]
New_rate={large:120,Xlarge:230,2Xlarge:450,4Xlarge:774,8Xlarge:1400,10Xlarge:2820}
India_rate={large:140,2Xlarge:413,4Xlarge:890,8Xlarge:1300,10Xlarge:2970}
China_rate={large:110,Xlarge:200,4Xlarge:670,8Xlarge:1180}
ans=defaultdict()
capacity=1150
hour=1 
output=[]
def cost(capacity,hour,ouput,qua):
    if capacity==0:
        return output
    
    for i in range(len(qua)):
        if qua[i-1]%capacity ==0:
            ans[quantity[i-1]]=capacity/qua[i-1] 
        else:
            cost(qua[i-1]%capacity,hour,ouput,qua[:i-2])

