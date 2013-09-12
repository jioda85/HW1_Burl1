# ==============================================================================     
# HW1_script: Script to read burl1 historical wind data
# ==============================================================================     
# by InOk Jun
# OCNG 658, Fall 2013
# ==============================================================================     

# import statement
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# open data file
f = open('burl1_2011.dat')

# make an empty list
dates = []
press = []
wind_U = []
wind_V = []

# read data using "for" loop (readlines)              
for line in f.readlines()[2:]:
    
    # split the data 
    data = line.split()
    
    # input time data
    year   = int(data[0])
    month  = int(data[1])
    day    = int(data[2])
    hour   = int(data[3])
    minute = int(data[4])
    dates.append( datetime(year, month, day, hour, minute) )
    
    # input pressure
    press.append( float(data[12]) )
    
    # converting meteorological convection to oceanographic convection of wind
    wind_U.append( -float(data[6]) * np.sin(float(data[5]) * np.pi/180.) )
    wind_V.append( -float(data[6]) * np.cos(float(data[5]) * np.pi/180.) )
 
       
# change data as array
dates = np.array(dates)
press = np.array(press)
wind_U = np.array(wind_U)
wind_V = np.array(wind_V)


# print the results
print 'dates        = ', dates
print 'wind (east)  = ', wind_U
print 'wind (north) = ', wind_V
print 'press        = ', press

# plotting the results
plt.figure()
plt.plot(dates, wind_U, '-r')
plt.xlabel('dates')
plt.ylabel('east (m/s)')
plt.show()

plt.figure()
plt.plot(dates, wind_V, '-b')
plt.xlabel('dates')
plt.ylabel('north (m/s)')
plt.show()

plt.figure()
plt.plot(dates, press, '-g')
plt.xlabel('dates')
plt.ylabel('pressure (hPa)')
plt.show()
