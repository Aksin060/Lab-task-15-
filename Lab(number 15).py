import math
import math as mh
m1 = (3.78*(math.e**4-math.e**3))/(4**(1/3)+3**(1/5))
m2 = mh.log(3)*(mh.sin((1/2)*mh.sin(-(2*2**0.5)/3)))
if abs(m1-2*m2)<=1:
    m3 = (m1-2*m2)/(m1**2+2)
else:
    m3 = 2/(m1-2*m2)
print(m3)