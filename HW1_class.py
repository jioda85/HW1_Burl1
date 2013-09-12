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
        
        dates  = []
        press  = []
        wind_U = []
        wind_V = []

        for line in f.readlines()[2:]:
            data = line.split()
            year   = int(data[0])
            month  = int(data[1])
            day    = int(data[2])
            hour   = int(data[3])
            minute = int(data[4])
            
            dates.append( datetime(year, month, day, hour, minute) )  
            press.append( float(data[12]) )
            wind_U.append( -float(data[6]) * np.sin(float(data[5]) * np.pi/180.) )
            wind_V.append( -float(data[6]) * np.cos(float(data[5]) * np.pi/180.) )

        dates = np.array(dates)
        press = np.array(press)
        wind_U = np.array(wind_U)
        wind_V = np.array(wind_V)
        
        print 'dates        = ', dates
        print 'wind (east)  = ', wind[0]
        print 'wind (north) = ', wind[1]
        print 'press        = ', press
    
        self.dates  = dates
        self.wind_U = wind_U
        self.wind_V = wind_V
        self.press  = press
