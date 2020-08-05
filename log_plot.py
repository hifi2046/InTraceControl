# -*- coding: UTF8 -*-
import carla
import rssw
import pickle
import math
import numpy as np
import matplotlib.pyplot as plt

print("rssw version:", rssw.version())
f=open("rsscheck.log","rb")
d=pickle.load(f)
f.close()
distance=[]
velocity=[]
front_distance=[]
brake=[]
op_x=float(d[0][1][0])
op_y=float(d[0][1][1])
i=0 
for t in d:
#    print(t[1]) #ego
    ego_x = float(t[1][0])
    ego_y = float(t[1][1])
    ego_v = float(t[1][3])
    ego_d = math.sqrt((ego_x - op_x)**2 + (ego_y - op_y)**2)
    distance.append(ego_d)
    velocity.append(ego_v)
#    print(t[2]) #other
    other_x = float(t[2][0])
    other_y = float(t[2][1])
    other_d = math.sqrt((ego_x - other_x)**2 + (ego_y - other_y)**2)
    front_distance.append(other_d)
#    print(t[3]) #control
    control_brake = float(t[3][1])
    brake.append(control_brake)
    if( control_brake != -1 ):
        print(i, t[3])
    i+=1
plt.plot(distance, label="distance")
plt.plot(front_distance, label='front distance')
plt.plot(velocity, label='velocity')
plt.plot(brake, label='brake')
plt.legend()
plt.show()
