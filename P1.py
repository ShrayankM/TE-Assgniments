import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm
import  numpy as np

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from colour import Color
df_p_2013_list = []
df_p_2014_list = []
df_p_2015_list = []
df_p_2016_list = []
df_p_2017_list = []
output = dict()
count = 0

fig, ax = plt.subplots(figsize=(10,20))
india = Basemap(resolution='i', # c, l, i, h, f or None
            projection='merc',
            lat_0=27.90, lon_0=29.4,
            llcrnrlon=68.03, llcrnrlat= 7.78, urcrnrlon=97.43, urcrnrlat=35.76)
india.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
india.drawmapboundary(fill_color='lightblue')
india.fillcontinents(color='yellow',lake_color='#46bcec')
india.drawcoastlines()
india.readshapefile('F:\SDLProjects\Shapefile\India','areas')
#for i in india.areas:
#    print(i)
#for i in india.areas_info:
#  print(i)
patches = []
color_patch = []
df_p = pd.read_csv("Population_new.csv")

df_p_stateN = df_p.iloc[:,0]

df_p_2013N = df_p.iloc[:,1]

df_color = pd.read_csv("ColorN.csv")
df_colorC = df_color.iloc[:,0]
df_codeL = np.array(df_colorC)
df_newL = []

df_states = pd.read_csv("B2c.csv")


df_poly = pd.DataFrame({
        'shapes': [Polygon(np.array(shape), True) for shape in india.areas],
        'State': [area['NAME_1'] for area in india.areas_info]
    })
df_poly =df_poly.merge(df_states,on='State',how='left')
cmap = plt.get_cmap('Oranges')
pc=PatchCollection(df_poly.shapes,zorder=2)
norm = Normalize()

pc.set_facecolor(cmap(norm(df_poly['2013'].fillna(0).values)))
ax.add_collection(pc)

mapper = matplotlib.cm.ScalarMappable(norm=norm , cmap=cmap)
mapper.set_array(df_poly['2013'])
plt.colorbar(mapper,shrink=0.4)

plt.show()
