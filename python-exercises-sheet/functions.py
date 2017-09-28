#5
def miles_to_feet(miles):
    feet = 5280
    return (miles*feet)

#6
def total_seconds(hours, minutes, seconds):
    return((hours*60*60)+(minutes*60)+seconds)

#7
import math
from math import hypot
def point_distance(x0,y0,x1,y1):
    return(math.hypot(x1 - x0,y1 - y0))
