import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# set up orthographic map projection with
# perspective of satellite looking down at 45N, 100W.
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color="#EE99AA",lake_color="#6699CC")
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color="#6699CC")
# draw lat/lon grid lines every 10 degrees.
map.drawmeridians(np.arange(0,360,10))
map.drawparallels(np.arange(-90,90,10))
# make up some data on a regular lat/lon grid.
#nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
#lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
#lons = (delta*np.indices((nlats,nlons))[1,:,:])
#wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
#mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# compute native map projection coordinates of lat/lon grid.
#x, y = map(lons*180./np.pi, lats*180./np.pi)
# contour data over the map.
#cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
plt.title("An example of spherical distance")

def make_pt(longit, latit, type_use = "", text_use = ""):
    xpts, ypts = map(longit, latit) 
    lonpts, latpts = map(xpts, ypts, inverse = True)
    if type_use != "":
        map.plot(xpts, ypts, color = type_use, marker = "o")
    if text_use != "":
        plt.text(xpts + 400000, ypts + 400000, text_use, backgroundcolor = "#FFFFFF")

lon4, lat4 = -104.237, 40.125 # Boulder
lon3, lat3 = -71.057083, 42.361145 # Boston
lon5, lat5 = -123.116226, 49.246292 # Vancouver
lon1, lat1 = -149.863129, 61.217381 # Anchorage
lon2, lat2 = -66.916664, 10.500000 # Carracas

for lon in np.arange(lon1, lon2, (lon2 - lon1) / 100):
    make_pt(lon, lat1, type_use = "#EECC66", text_use = "")
    make_pt(lon, lat2, type_use = "#EECC66", text_use = "")

for lat in np.arange(lat1, lat2, (lat2 - lat1) / 100):
    make_pt(lon1, lat, type_use = "#997700", text_use = "")
    make_pt(lon2, lat, type_use = "#997700", text_use = "")

for pct_use in np.arange(0, 1, 0.01):
    lon = lon1 + (lon2 - lon1) * pct_use
    lat = lat1 + (lat2 - lat1) * pct_use
    make_pt(lon, lat, type_use = "#994455", text_use = "")

make_pt(lon1, lat1, type_use = "#004488", text_use = "$P$($\\lambda_{1}$, $\\varphi_{1}$)") # 'Boulder (%5.1fW,%3.1fN)' % (lonpt1, latpt1))
make_pt(lon2, lat2, type_use = "#004488", text_use = "$Q$($\\lambda_{2}$, $\\varphi_{2}$)")
make_pt(lon1, lat2, type_use = "#004488", text_use = "($\\lambda_{1}$, $\\varphi_{2}$)")
make_pt(lon2, lat1, type_use = "#004488", text_use = "($\\lambda_{2}$, $\\varphi_{1}$)")

lonm, latm = (lon1 + lon2) / 2, (lat1 + lat2) / 2
make_pt(max(lon1, lon2), latm, type_use = "", text_use = "$\\Delta\\varphi=\\varphi_{2}-\\varphi_{1}$")
make_pt(lonm, min(lat1, lat2), type_use = "", text_use = "$\\Delta\\lambda=\\lambda_{2}-\\lambda_{1}$")
make_pt(lonm, latm, type_use = "", text_use = "$d$")

plt.savefig("globe.png", bbox_inches = "tight")
plt.savefig("globe.svg", bbox_inches = "tight")
plt.savefig("globe.pdf", bbox_inches = "tight")
plt.close()