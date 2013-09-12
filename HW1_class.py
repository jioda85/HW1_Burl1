# ==============================================================================
# HW1_class: Class to read burl1 historical wind data
# ==============================================================================
# by InOk Jun
# OCNG 658, Fall 2013
# ==============================================================================

# import statement
import numpy as np
from datetime import datetime

class data():
    '''
    class to read burl1 datafile and return the dates, wind, press information
    
    Input : 'filename' (e.g. 'burl1_2011.txt')
    Output:  self.dates = dates in a datetime format (yr, mon, day, hr, min)
    self.wind  = wind vector (m/sec)  ([0]: Eastward, [1]: Northward)
    self.press = sea-level pressure (hPa)
    
    Example:
    >> from HW1_class import data
    >> result = data('burl1_2011.txt')
    >> result.dates
    >> result.wind
    >> result.press
    '''
    

    def __init__(self, filename):
        
        self.filename = filename
        f = open(self.filename)
        
        dates = []
        dirct = []
        speed = []
        press = []

        for line in f.readlines()[2:]:
            data = line.split()
            year   = int(data[0])
            month  = int(data[1])
            day    = int(data[2])
            hour   = int(data[3])
            minute = int(data[4])
            dates.append( datetime(year, month, day, hour, minute) )
            dirct.append( float(data[5]) )
            speed.append( float(data[6]) )    
            press.append( float(data[12]) )
    
        dates = np.array(dates)
        speed = np.array(speed)
        dirct = np.array(dirct)
        press = np.array(press)
        
        for i in range(len(dirct)):
            if dirct[i] == 999  : dirct[i] = np.Nan
            elif dirct[i] >= 180: dirct[i] = dirct[i] - 180
            else:                 dirct[i] = dirct[i] + 180
            
        wind = - speed * (np.sin(dirct * np.pi/180.), np.cos(dirct * np.pi/180.))
        
        print 'dates        = ', dates
        print 'wind (east)  = ', wind[0]
        print 'wind (north) = ', wind[1]
        print 'press        = ', press
    
        self.dates = dates
        self.wind  = wind
        self.press = press
