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

filename='Len_dist_b1_L51_p100.csv'
float_list =read_float_list_from_csv(filename)

n=17
v=500
N=1000

D=[]
for i in range(n):
    D_0=[]
    for j in range(i*v, (i+1)*v):
        D_0.append(float_list[j])
    D.append(D_0)

def count_elements(sorted_list, N):
    # Count occurrences of each element in the list
    element_count = Counter(sorted_list)
    
    # Create a list to hold counts from 1 to N
    result = []
    for i in range(-1, N+1):
        result.append(element_count.get(i, 0))  # Get the count, default to 0 if not found

    return result

D0=[]
for i in range(n):
   Count_dist=count_elements(D[i], N)
   D0.append(Count_dist)

A_=np.sum(D0, axis=0)
A=[a/n/N for a in A_]


Len=[i+1 for i in range(N)]

l1,l2=786,904

def fg(x,a,b,s):
    return np.log(b)-((x-a)/s)**2

# A_log=[np.log(vals) for vals in A[l1+2:l2+2]]

# popt=curve_fit(fg, Len[l1:l2], A_log)[0]
# a0,b0,s0=popt[0],popt[1],popt[2]

# X=np.linspace(l1,l2,1000)
# Fit=[b0*np.exp(-((x-a0)/s0)**2) for x in X]

O1=[0 for v in Len[0:N]]

plt.plot(Len[0:N], A[2:N+2], 'rd')
# plt.plot(X, Fit, 'b', linewidth='3')
plt.plot(Len[0:N], O1, 'g', linewidth='3')
plt.show()


