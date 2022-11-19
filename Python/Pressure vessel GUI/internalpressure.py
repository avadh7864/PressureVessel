import pandas as pa
from scipy.interpolate import interp1d
import numpy as np
t=0 #thickness of shell
tc=0 #thickness due to circumferencial stress
tl=0 #thickness due to longitudinal stress
z=1 #for cylindrical shell z=1, for spherical shell z=2
e=0.85 #joint efficiency 85% for welded joints
r= 500 #get inner radius of cylinder in mm from user
p=100 #get internal design pressure of cylinder in kPa from user
temp=101 #get design temperature in celcius from user
sval=np.array(pa.read_excel('C:\\Users\\LEGION\\OneDrive\\Desktop\\Python\\Pressure vessel GUI\\Max stress values.xlsx'))
k=len(sval)
stress=sval[:,1]
itemp=sval[:,0]
#print(stress)
#print(itemp)
itdiff=np.absolute(itemp-temp)
itind=itdiff.argmin()
if(itemp[itind]<temp):
   itind+=1    
if(temp!=itemp[itind]):
   temp=itemp[itind]
#k2=len(itemp)
si=interp1d(itemp,stress)
s=si(temp)*1000
'''s=0 #max allowable stress
si=0 #for getting interpolated values
for i in range(0,k):
 if(temp==sval[i][0]):
    s=sval[i][1]
    break
 elif(temp<sval[i][0]):
    si=interp1d(itemp,stress)
    s=si(temp)*1000
    break'''
if(z==1):
   tc=((p*r)/(s*e-0.6*p))
   tl=((p*r)/(2*s*e+0.4*p))
   t=max(tc,tl)
elif(z==2):
 t=((p*r)/(2*s*e-0.2*p))
print(t) 