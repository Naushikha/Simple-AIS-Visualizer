import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt

import time

import json

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("./data/") if isfile(join("./data/", f))] # https://stackoverflow.com/a/3207973

processD = []

for thisfile in onlyfiles:
	# print(thisfile)
	f = open("./data/" + thisfile) # Opening JSON file

	data = json.load(f) # returns JSON object as a dictionary

	# Filter POSH HUSKY: 417222454
	for i in data:
		# print(i["MMSI"])
		if (i["MMSI"] == "417222454"):
			# print(i)
			processD.append(i)

	# Closing file
	f.close()

# print(processD)

newlist = sorted(processD, key=lambda d: d['TIMESTAMP']) 

# print(newlist)
# print(*newlist, sep='\n')

### Drawing map
# 6.970111, 79.821057
# 6.937585, 79.855412
# Colombo Harbor coordinates
harbor_extent = [79.821057, 79.858412, 6.937585, 6.974111] # ax.set_extent([lonmin, lonmax, latmin, latmax]
# Create a Stamen watercolor background instance / Google Maps
# terrain_requestor = cimgt.Stamen('watercolor') # cimgt.GoogleTiles()
terrain_requestor = cimgt.GoogleTiles()
# Define map size and dpi
fig = plt.figure(figsize=(10, 9), dpi=150)

# Create a GeoAxes in the tile's projection
ax = plt.axes(projection=ccrs.PlateCarree())
# Limit the extent of the map to a small longitude/latitude range
ax.set_extent(harbor_extent, crs=ccrs.PlateCarree())
# Add the Stamen data at zoom level 6
ax.add_image(terrain_requestor, 15, interpolation='spline36')

# https://stackoverflow.com/questions/49155110/why-do-my-google-tiles-look-poor-in-a-cartopy-map

# from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
# request = cimgt.GoogleTiles()

# fig = plt.figure(figsize=(13, 9))
# ax = plt.axes(projection=request.crs)

# gl = ax.gridlines(draw_labels=True, alpha=0.3)
# gl.xlabels_top = gl.ylabels_right = False
# gl.xformatter = LONGITUDE_FORMATTER
# gl.yformatter = LATITUDE_FORMATTER

# ax.set_extent(harbor_extent)
# ax.add_image(request, 15)
# ax.plot([79.821057, 79.858412], [6.937585, 6.974111], 'ob-', markersize=1.5, linewidth=0.5, linestyle="dashed")
plt.show(block=False)
input("Press Enter to continue...")

prev_ais_point = ""
for ais_point in newlist:
	if (prev_ais_point == ""):
		prev_ais_point = ais_point
		continue
	print(float(ais_point['LON']), float(ais_point['LAT']))
	plt.plot([float(prev_ais_point['LON']),float(ais_point['LON'])], [float(prev_ais_point['LAT']), float(ais_point['LAT'])], 'ob-', markersize=1.5, linewidth=0.5, linestyle="dashed")
	plt.pause(0.01) # little trick to update the map
	# time.sleep(0.1)
	prev_ais_point = ais_point # Push this for last

plt.show()

# for ais_point in newlist:
# 	print(float(ais_point['LON']), float(ais_point['LAT']))
# 	plt.plot(float(ais_point['LON']), float(ais_point['LAT']), 'ro', markersize=2)       # plot the red dot on the map
# 	plt.pause(0.01)                          # little trick to update the map
# 	time.sleep(0.1)