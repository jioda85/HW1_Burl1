"""
HW1_script: Script to read burl1 historical wind data
================================================================================
         
by InOk Jun
OCNG 658, Fall 2013
"""


# import statement
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# open data file
f = open('burl1_2011.dat')

# make an empty list
dates = []
dirct = []
speed = []
press = []


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

    # input wind data
    dirct.append( float(data[5]) )
    speed.append( float(data[6]) )
    
    # input pressure
    press.append( float(data[12]) )


# change data as array
dates = np.array(dates)
speed = np.array(speed)
dirct = np.array(dirct)
press = np.array(press)

# converting meteorological convection to oceanographic convection of wind
for i in range(len(dirct)):
    if dirct[i] == 999  : dirct[i] = np.Nan
    elif dirct[i] >= 180: dirct[i] = dirct[i] - 180
    else:                 dirct[i] = dirct[i] + 180

# calculate the wind vectors using speed & direction
wind = - speed * (np.sin(dirct * np.pi/180.), np.cos(dirct * np.pi/180.))


# print the results
print 'dates        = ', dates
print 'wind (east)  = ', wind[0]
print 'wind (north) = ', wind[1]
print 'press        = ', press


# plotting the results
plt.figure()
plt.plot(dates, wind[0], '-r')
plt.xlabel('dates')
plt.ylabel('east (m/s)')
plt.show()

plt.figure()
plt.plot(dates, wind[1], '-b')
plt.xlabel('dates')
plt.ylabel('north (m/s)')
plt.show()

plt.figure()
plt.plot(dates, press, '-g')
plt.xlabel('dates')
plt.ylabel('pressure (hPa)')
plt.show()




# NOTE: alternative format
#data = {'dates': np.array(dates), 'press': np.array(press)}
#print data['dates']
#print data['press']