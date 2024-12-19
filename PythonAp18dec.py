#sgn
#code blocks ref file
dev_reading = [29.5, 30.2, 32.7, 35.1, 36.3, 37.1, 28.9, 25.5, 23.8, 20.4, 18.4, 16.2]
for tr in dev_reading:
    if tr < 25:
        print('Low')
    elif tr == 25:
        print('Moderate')
    else:
        print('High')
#print to screen
#end of code


#codeblock2-da-s
dev_reading = [29.5, 30.2, 32.7, 35.1, 36.3, 37.1, 28.9, 25.5, 23.8, 20.4, 18.4, 16.2]
import statistics as sts
import numpy as np
mean_readings = sts.mean(dev_reading)
print(mean_readings)
fl_mean = sts.fmean(dev_reading)
print(fl_mean)
median_rd = sts.median(dev_reading)
print(median_rd)
low_r = sts.median_low(dev_reading)
print(low_r)
high_r = sts.median_high(dev_reading)
print(high_r)

#codeblock3-d-s
import numpy as np
con_arr1 = np.array([1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000])
con_arr2 = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010])
fx1 = np.add(con_arr1, con_arr2)
print(fx1)
fx2 = np.subtract(con_arr1, con_arr2)
print(fx2)
fx3 = np.multiply(con_arr1, con_arr2)
print(fx3)
fx4 = np.divide(con_arr1, con_arr2)
print(fx4)
#print to screen
fx5 = np.round(con_arr1)
print(fx5)
fx6 = np.min(con_arr1)
print(fx6)
fx7 = np.max(con_arr2)
print(fx7)
#end of code


#code-da-p%g
#defining function to calculate range of values
list01 = [331, 283, 291, 317, 339, 341, 301, 323, 261, 252, 279, 211]
lv = min(list01)
print(lv)
uv = max(list01)
print(uv)
#end of code

#cde
def rov(uv, lv):
    return uv - lv
#calling function with arguments
rv = rov(341, 211)
print(rv)
#end of code


#

rloop = 1001
while rloop < 200001:
    print('value is:', rloop)
    rloop = rloop * 1.75
#end of code
#print to screen


