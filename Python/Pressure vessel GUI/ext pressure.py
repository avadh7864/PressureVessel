import pandas as pa
from scipy.interpolate import interp1d
import numpy as np
t=220 #thickness of shell in mm
ro=500 #outside radius of shell in mm
po=2 #external design pressure in MPa
l=4500 #length of vessel in mm
temp=200 #design temperature in celcius
temp1=temp
z=1 #for determining if the shell is cylindrical or spherical
Pa=0 #for calculating max. allowable external pressure
Pa1=0
Pa2=0
s=0 
si=0
s1=0
aval=np.array(pa.read_excel('C:\\Users\\LEGION\\OneDrive\\Desktop\\Python\\Pressure vessel GUI\\Factor AB.xlsx','Table G-Sorted'))
#print(aval)
dt=aval[1:,0] #creating individual vectors to perform interpolation
#print(dt)
ld=aval[0,1:]
#print(ld)
#a=aval[1:,]
#k=len(dt)
#kc=len(ld)
#aval=pa.DataFrame(a,index=dt,columns=ld)
#print(aval)
#aval.reindex(sorted(aval.index),axis=0).reindex(sorted(aval.columns),axis=1)
#aval.interpolate().interpolate(axis=1)
Aval=0
A=0
#j=0
#m=0
r1=(2*ro)/t
r2=l/(2*ro)
#print(aval)
#print(a)
#print(dt)
#print(r1,r2)
dtdiff=np.absolute(dt-r1)
dtind=dtdiff.argmin()
#print(dt[dtind])
#if(dt[dtind]<r1):
#    dtind+=1
#print(dt[dtind])
#print(aval[dtind+1,1:])
adt=aval[dtind+1,1:]
aind=np.argwhere(adt!=adt)
aind=aind.flatten()
adt=adt[~(adt!=adt)]
#print(adt)
#print(aind)
for i in sorted(aind,reverse=True):
    ld=np.delete(ld,i)
#print(ld)
Aval=interp1d(ld,adt)
A=Aval(r2)
print(A)
'''for l in range(0,k): #to get factor A
    if(r1<=dt[l]):
        r1=dt[l]
        print(l)
        break
for i in range(0,k):
    if(r2==ld[l]):
        A=a[l]
    elif(r2<ld[l]):
        Aval=interp1d(ld,a)
        A=Aval(r2)
        print(A)
        print(l)
        break                        
    elif(r1<dt[l]):
        break
    else:
        l+=1
#print(A)'''
bval=np.array(pa.read_excel('C:\\Users\\LEGION\\OneDrive\\Desktop\\Python\\Pressure vessel GUI\\Factor AB.xlsx','Table CS-1 Sorted'))
Temp=bval[1:,0]
#print(Temp)
a1=bval[0,1:]
#print(a1)
#b=bval[:,2]
tdiff=np.absolute(Temp-temp)
tind=tdiff.argmin()
if(Temp[tind]<temp):
    tind+=1
#print(Temp[tind])
#k1=len(Temp)
#A1=A
Bval=0
B=0
A=A.astype(np.float64)
#print(A)
#j1=0
#m1=0
#print(bval)
b=bval[tind+1,1:]
#print(b)
aind1=np.argwhere(b!=b)
aind1=aind1.flatten()
#print(aind1)
for i in sorted(aind1,reverse=True):
    a1=np.delete(a1,i)
#print(a1)    
b=b[~(b!=b)]
#print(b)
#a1=a1.astype(float)
#b=b.astype(float)
#print(a1)
#print(b)
Bval=interp1d(a1,b)
B=Bval(A)
print(B)
'''for l1 in range(0,k1): #to get factor B
    if(temp<=Temp[l1]):
        temp=Temp[l1]
        #print(l1)
        #print(temp)
        break
for i1 in range(0,k1):
    if(A1==a1[l1]):
        B=b[l1]
    elif(A1<a1[l1]):
        Bval=interp1d(a1,b)
        B=Bval(A1)
        #print(B)
        #print(l1)
        #print(a1[l1])
        break                        
    elif(temp<Temp[l1]):
        break
    else:
        l1+=1
print(B)'''
k2=0
k3=0
if(z==1): #for cylindrical vessels
    if((2*ro)/t>=10):
        Pa=(4*B)/(3*((2*ro)/t))
    elif((2*ro)/t<10):
        sval=np.array(pa.read_excel('C:\\Users\\LEGION\\OneDrive\\Desktop\\Python\\Pressure vessel GUI\\Max stress values.xlsx'))
        stress=sval[:,1]
        itemp=sval[:,0]
        #print(stress)
        #print(itemp)
        itdiff=np.absolute(itemp-temp)
        itind=itdiff.argmin()
        if(itemp[itind]<temp1):
            itind+=1    
        if(temp1!=itemp[itind]):
            temp1=itemp[itind]
        #k2=len(itemp)
        si=interp1d(itemp,stress)
        s=si(temp1)*1000
        #print(s)
        '''for i in range(0,k2):
            if(temp1==sval[i][0]):
                s=sval[i][1]*1000
                break
            elif(temp1<sval[i][0]):
                si=interp1d(itemp,stress)
                s=si(temp1)*1000
                break'''
        yval=np.array(pa.read_excel('C:\\Users\\LEGION\\OneDrive\\Desktop\\Python\\Pressure vessel GUI\\Factor AB.xlsx','Table CS-1 Sorted'))
        itemp1=yval[1:,0]
        aval1=yval[1,1:]
        k3=len(aval1)
        diff=np.absolute(itemp1-temp1)
        ind=diff.argmin()
        y1=2*yval[ind+1,k3]
        s1=min(2*s,0.9*y1)
        #print(s1)
        Pa=min((((2.167/((2*ro)/t))-0.0833)*B),(((2*s1)/((2*ro)/t))*(1-1/((2*ro)/t))))
    #print(Pa)    
    if(Pa<po):
        print('Increase thickness')
    else:
        print('Selected thickness is safe')


    
