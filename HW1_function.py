# ==============================================================================
# HW1_function: Function to read burl1 historical wind data
# ==============================================================================
# by InOk Jun
# OCNG 658, Fall 2013
# ==============================================================================

# import statement
import numpy as np
from datetime import datetime


def data(filename):
    '''
    function to read burl1 datafile and return the dates, wind, press information
    
    Input : 'filename' (e.g. 'burl1_2011.txt')
    return:  dates = dates in a datetime format (yr, mon, day, hr, min)
    wind  = wind vector (m/sec)  ([0]: Eastward, [1]: Northward)
    press = sea-level pressure (hPa)
    '''
    
    # open data file
    f = open(filename)

    # make an empty list
    dates = []
    press = []
    wind_U = []
    wind_V = []

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
    
    return dates, wind_U, wind_V, press



# run the function
result = data('burl1_2011.dat')

# arrange the result from 'function'
dates   = result[0]
wind_U  = result[1]
wind_V  = result[2]
press   = result[3]
