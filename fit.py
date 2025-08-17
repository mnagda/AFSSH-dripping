import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * np.exp(-b * x) + (1-a)

#x = np.linspace(0,4,50)
#y = func(x, 2.5, 1.3, 0.5)
#yn = y + 0.2*np.random.normal(size=len(x))

## Extracting value that is varied
# Read the first number from the first file
with open('../variation.inp', 'r') as file1:
    first_line = file1.readline().strip()
    first_number = float(first_line.split()[0])  # Extract the first number

# Convert the first number to an integer to use as a row index
row_index = int(first_number)

# Open the second file and read the appropriate row
with open('AFSSH.inp', 'r') as file2:
    for current_index, line in enumerate(file2):
        if current_index == row_index-1:
            # Extract the first number from the line
            value = float(line.split()[0])
            break


data = np.loadtxt("pop.out")
x=data[:,0]
yn=data[:,1]
p=np.array([0.8,2.e-5])

popt, pcov = curve_fit(func, x, yn,p,maxfev=9000)

filename = '../rate.out'

#if os.path.exists(filename):
#    append_write = 'a' # append if already exists
#else:
#    append_write = 'w' # make a new file if not
#
#rates = open(filename,append_write)
#rates.write(popt[1],(pcov[1,1])**0.5),popt[0],pcov[0,0]**0.5 + '\n')
#rates.close()

with open(filename, 'a+') as f:
    f.write(f"{value} {popt[1]} {pcov[1,1]**0.5} {1-popt[0]} {pcov[0,0]**0.5}\n")

print("rate (fs-1)=",popt[1],(pcov[1,1])**0.5)
print("thermal pop =",1-popt[0],pcov[0,0]**0.5)

#plt.figure()
#plt.plot(x, yn, 'ko', label="Original Noised Data")
#plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
#plt.legend()
#plt.show()

