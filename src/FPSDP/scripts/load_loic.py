#!/usr/bin/env python
from FPSDP.Plasma.XGC_Profile.load_XGC_profile import *
from FPSDP.Geometry.Grid import *
import matplotlib as mp
mp.use('agg')
import matplotlib.pyplot as plt

xgc_path = '/global/project/projectdirs/m499/jlang/particle_pinch/'

grid2D = Cartesian2D(DownLeft = (-0.5,1.3),UpRight = (0.5,1.6),NR = 256, NZ = 512)

#grid3D = Grid.Cartesian3D(Xmin = 1.3,Xmax = 1.6,Ymin = -0.5, Ymax = 0.5, Zmin = -0.3, Zmax = 0.3, NX = 256,NY = 512,NZ = 80)

time_start = 1
time_end = 1
time_step = 1

def load(dimension,full_load,fluc_only):
    if dimension == 3:
        xgc = XGC_Loader(xgc_path,grid3D,time_start,time_end,time_step,dn_amplifier = 1,n_cross_section = 1, Full_Load = full_load, Fluc_Only = fluc_only)
    elif dimension == 2:
        xgc = XGC_Loader(xgc_path,grid2D,time_start,time_end,time_step,dn_amplifier = 1,n_cross_section = 1, Full_Load = full_load, Fluc_Only = fluc_only)

    return xgc    

xgc = load(2,True,False)
print xgc.ne_on_grid.shape

print max(xgc.ne_on_grid[0][0][:][:].max(axis=1))
plt.figure()
plt.contourf(xgc.ne_on_grid[0][0][:][:])
#plt.savefig('foo.pdf')
plt.show(True)