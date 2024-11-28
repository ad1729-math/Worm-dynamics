import math as m 
import numpy as np 
import matplotlib.pyplot as plt 
import csv 
from collections import Counter
from scipy.optimize import curve_fit

def read_float_list_from_csv(filename):
    float_list = []

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            for line in reader:
                for value in line:
                    try:
                        float_value = float(value)
                        float_list.append(float_value)
                    except ValueError:
                        print(f"")
    except IOError:
        print(f"Unable to open file: {filename}")

    return float_list

def FD(x):
    return np.log(x)

filename0='Len_dist_bc_2000_L51_p100.csv'
filename1='Len_dist_bc_2000_L51_p50.csv'

float_list0 =read_float_list_from_csv(filename0)
float_list1 =read_float_list_from_csv(filename1)

nc,n1=599,341
v=500
N,N1=2000,5000

D0_=[]
for i in range(nc):
    D_0=[]
    for j in range(i*v, (i+1)*v):
        D_0.append(float_list0[j])
    D0_.append(D_0)

D1_=[]
for i in range(n1):
    D1_0=[]
    for j in range(i*v, (i+1)*v):
        D1_0.append(float_list1[j])
    D1_.append(D1_0)

def count_elements(sorted_list, N):
    # Count occurrences of each element in the list
    element_count = Counter(sorted_list)
    
    # Create a list to hold counts from 1 to N
    result = []
    for i in range(-1, N+1):
        result.append(element_count.get(i, 0))  # Get the count, default to 0 if not found

    return result

D0=[]
for i in range(nc):
   Count_dist=count_elements(D0_[i], N)
   D0.append(Count_dist)

D1=[]
for i in range(n1):
   Count_dist=count_elements(D1_[i], N1)
   D1.append(Count_dist)

A_=np.sum(D0, axis=0)
A=[FD((a)/nc/N) for a in A_]

A1_=np.sum(D1, axis=0)
A1=[FD((a)/n1/N1) for a in A1_]

Len=[FD(i) for i in range(1,N+1)]
Len1=[FD(i) for i in range(1,N1+1)]

l1,l2=954,985

def fg(x,a,b,s):
    return np.log(b)-((x-a)/s)**2

# A_log=[np.log(vals) for vals in A[l1:l2]]

# popt=curve_fit(fg, Len[l1:l2], A_log)[0]
# a0,b0,s0=popt[0],popt[1],popt[2]

# X=np.linspace(l1,l2,1000)
# Fit=[b0*np.exp(-((x-a0)/s0)**2) for x in X]

O1=[0 for v in Len1]

plt.plot(Len[0:], A[2:], 'rd')
plt.plot(Len1[0:], A1[2:], 'bd')
# plt.plot(X, Fit, 'g', linewidth='3')
plt.plot(Len1, O1, 'g', linewidth='3')
plt.show()


