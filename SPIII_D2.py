#shree ganeshay namah
#file for prod env

#code01
import array
import statistics as sts 
list_1612 = [9, 11, 14, 15, 17, 19, 21, 22, 24, 25, 27, 33]
ct01 = sts.mean(list_1612)
print('Mean01 is', ct01)
ct02 = sts.fmean(list_1612)
print('Mean02 is', ct02)
ct03 = sts.geometric_mean(list_1612)
print('Mean03 is', ct03)
ct04 = sts.harmonic_mean(list_1612)
print('Mean04 is', ct04)
ct05 = sts.median(list_1612)
print('Mean05 is', ct05)
ct06 = sts.median_high(list_1612)
print('Mean06 is', ct06)
ct07 = sts.median_low(list_1612)
print('Mean07 is', ct07)
ct08 = sts.mode(list_1612)
print('Mean08 is', ct08)
ct09 = sts.multimode(list_1612)
print('Mean09 is', ct09)
ct10 = sts.variance(list_1612)
print(ct10)
ct11 = sts.pstdev(list_1612)
print(ct11)
ct12 = sts.stdev(list_1612)
print(ct12)
#end code

#code002
#using numpy library for stat computations
import numpy as np
array_1 = np.array([731, 755, 732, 742, 647, 649])
array_2 = np.array([424, 457, 440, 476, 532, 541])
fun1 = np.add(array_1, array_2)
print(fun1)
fun2 = np.subtract(array_1, array_2)
print(fun2)
fun3 = np.multiply(array_1, array_2)
print(fun3)
fun4 = np.divide(array_1, array_2)
print(fun4)
fun5 = np.max(array_1)
print(fun5)
fun6 = np.min(array_1)
print(fun6)
fun7 = np.mean(array_1)
print(fun7)
fun8 = np.median(array_2)
print(fun8)
fun9 = np.dot(array_2, array_2)
print(fun9)
fun10 = np.round(array_1)
print(fun10)
#end of code


#code003
sb = 11.34
ms = 14.64
pc = 12.34
jh = 16.78
best_perf = min(sb, ms, pc, jh)
print('The top performance is by:', best_perf)
#end of code


#code91
c_list = [76.22, 89.15, 91.33, 94.04, 81.02]
for winr in c_list:
    if winr < 80:
        print('Disqualified')
    elif winr == 80:
        print('Qualified 1')
    else:
        print('Qualified2')
#print results
#end of code


#code104
def nrr(truns, matches):
    return truns / matches
#calling function with arguments
netrr = nrr(2078, 24)
print('Value of NRR is', netrr)
#end of code

#code095
pystring = 'maximum length of string'
print(pystring)
#end of code

#code4545
string_typ2 = 'astringwithnospaces'
print(string_typ2[7])
#end of code

#code55644
loopv = 47500
while loopv < 1499999:
    print(loopv)
    loopv = loopv * 1.15
#end of code