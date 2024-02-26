#
#  Python source for figure in 2016 SPIE paper
#
#  ARC - 05jul2016
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#
#  x,yvals are the points' coordinates; x,yoff the arrow to the label;
#  arrow array has the arrow direction.
#
xvals = [ 1989, 1983, 2003, 1994, 2019, 1948, 1978,
          2000, 2000, 1996, 2006, 2013, 2025, 2028, 2024 ]
yvals = [  0.29, 0.57, 0.85, 2.5, 6.5, 5.8, 3.0,
           6.5, 8.2, 10.0, 8.4, 22.8, 24.5, 30, 39.3 ]

xoff  = [20, 20, -20, -20, 10, -20, 60, -40,  80,  40, -20, 50,  20,  20,  20 ]
yoff  = [40, 30,  40,  40, 30, -40,-30, -50, -70, -30, -10,-20, -20, -20, -20 ]
arrow = [   1,  1, 1, 1, 1, 1,   1,   1,   1,   1, 1, 1, 1, 1, 1 ]

labels = [ 'Hipparcos', 'IRAS', 'Spitzer', 'Hubble', 'JWST', 'Hale',
          'Lick', 'MMT, Magellan', 'Subaru, VLT, Gemini',
          'Keck', 'LBT-mono','LBT', 'GMT', 'TMT', 'E-ELT']

#plt.subplots_adjust(bottom = 0.1)

#
#  Plot space vs ground seperately so as to use different markers for each
#
sca_g = plt.scatter(xvals[5:15],yvals[5:15],marker='.')
sca_g._sizes=(np.ones(9))*250
sca_s = plt.scatter(xvals[0:5],yvals[0:5],color='red',marker='*')
sca_s._sizes=(np.ones(5))*100

for i in range(len(xvals)):
  if ( arrow[i] == 1 ):
    plt.annotate( labels[i], (xvals[i], yvals[i]),  \
       xytext=(-xoff[i], -yoff[i]), textcoords='offset points', \
       arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
  else:
    plt.annotate( labels[i], (xvals[i], yvals[i]),  \
       xytext=(-xoff[i], -yoff[i]), textcoords='offset points' )


# kludgey, but simple way to draw an arrow by itself
GroundXY = [2030, 27]
GroundXYoff = [-220,-100]
SpaceXY =  [2030, 9]
SpaceXYoff =  [-220,-37]
plt.annotate( "", GroundXY,  \
       xytext=GroundXYoff, textcoords='offset points', \
       arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0', \
            color='blue'))
plt.annotate( "", SpaceXY,  \
       xytext=SpaceXYoff, textcoords='offset points', \
       arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0', \
            color='red'))
zline = plt.axhline(y=0, color='black')
zline.set_dashes([8, 4, 2, 4, 2, 4])

#  get rid of the ticks (e.g., -10) at lower left
ax = plt.gca()
ax.set_xticks([1940,1960, 1980, 2000, 2020, 2040])
ax.set_yticks([0,10, 20, 30, 40])
ax.set_ylim([-10,50])

plt.xlabel('Year')
plt.ylabel('Aperture (m)' )
plt.show()
