import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z)

coords = [[(u2, v2) for u2 in np.arange(0, 2 * np.pi, np.pi / 360)] for v2 in np.arange(0, np.pi, np.pi / 360)]
for ix in range(len(coords)):
    u1, v1 = coords[ix][0]
    x1 = 10 * np.outer(np.cos(u1), np.sin(v1))
    y1 = 10 * np.outer(np.sin(u1), np.sin(v1))
    z1 = 10 * np.outer(np.ones(np.size(u1)), np.cos(v1))
    ax.scatter(x1, y1, z1, color = "red")

# Set an equal aspect ratio
ax.set_aspect('equal')

plt.show()
plt.close()
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# set up orthographic map projection with
# perspective of satellite looking down at 45N, 100W.
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# draw coastlines, country boundaries, fill continents.
#map.drawcoastlines(linewidth=0.25)
#map.drawcountries(linewidth=0.25)
#map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
#map.drawmapboundary(fill_color='aqua')
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
# make up some data on a regular lat/lon grid.
nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons*180./np.pi, lats*180./np.pi)
# contour data over the map.
#cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
#plt.title('contour lines over filled continent background')


# plot blue dot on Boulder, colorado and label it as such.
lon, lat = -104.237, 40.125 # Location of Boulder
# convert to map projection coords. 
# Note that lon,lat can be scalars, lists or numpy arrays.
xpt,ypt = map(lon,lat) 
# convert back to lat/lon
lonpt, latpt = map(xpt,ypt,inverse=True)
map.plot(xpt,ypt,'bo')  # plot a blue dot there
# put some text next to the dot, offset a little bit
# (the offset is in map projection coordinates)
plt.text(xpt+100000,ypt+100000,'Boulder (%5.1fW,%3.1fN)' % (lonpt,latpt))

plt.show()
plt.close()