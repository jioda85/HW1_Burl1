"""
HW1_function: Function to read burl1 historical wind data
================================================================================

" def data "
: function to read burl1 datafile and return the dates, wind, press information

  Input : 'filename' (e.g. 'burl1_2011.txt')
  return:  dates = dates in a datetime format (yr, mon, day, hr, min)
           wind  = wind vector (m/sec)  ([0]: Eastward, [1]: Northward) 
           press = sea-level pressure (hPa)
         
by InOk Jun
OCNG 658, Fall 2013
"""

# import statement
import numpy as np
from datetime import datetime


def data(filename):

    # open data file
    f = open(filename)

    # make an empty list
    dates = []
    dirct = []
    speed = []
    press = []

    # read data                 
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
    
    return dates, wind, press



# run the function
result = data('burl1_2011.dat')

# arrange the result from 'function'
dates = result[0]
wind  = result[1]
press = result[2]