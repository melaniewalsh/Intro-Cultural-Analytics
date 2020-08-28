# Custom Map Backgrounds

You can use custom base maps with Folium! 

**Import Folium**

import folium

## *Game of Thrones*

To use a custom basemap, we need to set the `tiles` parameter to a custom map image and the `attr` parameter to the source of the the map.

For this *Game of Thrones* map, we're also setting zoom and lat/lon bounds so the user can't navigate off the map.

folium.Map(location=[0, 30],
           zoom_start=4, min_zoom=4, max_zoom=10,
           max_bounds=True,
           min_lon=0, max_lon=70, min_lat=-40, max_lat=40,
           tiles='https://cartocdn-gusc.global.ssl.fastly.net//ramirocartodb/api/v1/map/named/tpl_756aec63_3adb_48b6_9d14_331c6cbc47cf/all/{z}/{x}/{y}.png',
           attr='Textures and Icons from https://www.textures.com/ & https://thenounproject.com/')

Source [https://carto.com/blog/game-of-thrones-basemap/](https://carto.com/blog/game-of-thrones-basemap/)

## Watercolor

folium.Map(location=[0, 30],
           zoom_start=2,
           tiles='http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg',
           attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.')

Source [http://maps.stamen.com/#watercolor/12/37.7706/-122.3782](http://maps.stamen.com/#watercolor/12/37.7706/-122.3782)

## National Geographic

folium.Map(location=[0, 30],
           zoom_start=4,

           tiles='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
           attr="Sources: National Geographic, Esri, Garmin, HERE, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, INCREMENT P")

Source [https://www.arcgis.com/home/item.html?id=b9b1b422198944fbbd5250b3241691b6](https://www.arcgis.com/home/item.html?id=b9b1b422198944fbbd5250b3241691b6)