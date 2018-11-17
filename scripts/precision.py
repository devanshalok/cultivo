#making a script to round off every decimal to 2 precision point

def precise(data,point):
    if type(data)==dict:
        a={}
        for i in data:
            if type(data[i])==float:
                data[i]=round(data[i],point)
                a[i]=data[i]
            else:
                a[i]=data[i]
    
    if type(data)==float:
        return round(data,point)
    
    if type(data)==list:
        a=[]
        for i in data:
            if type(i)==float:
                i=round(i,point)
                print(i)
                a.append(i)
            else:
                a.append(i)
    return a
#%%
a=[2,3,4.5556,3.763763,2.12]
c=['aman','anjali','lala','deva']
d=[2,2.22,2.2222,3.33333]
dd=dict(zip(c,d))
l=precise(a,3)
ll=precise(dd,1)
print(l)
print(ll)
print(precise(34.3333,2))