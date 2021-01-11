# Mapping

In this lesson, we're going to learn how to analyze and visualize geographic data.

# Geocoding with GeoPy

First, we're going to geocode data — aka get coordinates from addresses or place names — with the Python package [GeoPy](https://geopy.readthedocs.io/en/stable/#). GeoPy makes it easier to use a range of third-party [geocoding API services](https://geopy.readthedocs.io/en/stable/#), such as Google, Bing, ArcGIS, and OpenStreetMap.

Though most of these services require an API key, Nominatim, which uses OpenStreetMap data, does not, which is why we're going to use it here.

### Install GeoPy

!pip install geopy

### Import Nominatim

From GeoPy's list of possible geocoding services, we're going to import Nominatim:

from geopy.geocoders import Nominatim

### Nominatim & OpenStreetMap

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Openstreetmap_logo.svg/256px-Openstreetmap_logo.svg.png" border=2 >

Nominatim (which means "name" in Latin) uses [OpenStreetMap data](https://www.openstreetmap.org/relation/174979) to match addresses with geopgraphic coordinates. Though we don't need an API key to use Nominatim, we do need to create a unique [application name](https://operations.osmfoundation.org/policies/nominatim/). 

Here we're initializing Nominatim as a variable called `geolocator`. Change the application name below to your own application name:

geolocator = Nominatim(user_agent="YOUR NAME's mapping app", timeout=2)

To geocode an address or location, we simply use the `.geocode()` function:

location = geolocator.geocode("South Cayuga Street")

location

### Google Geocoding API

The Google Geocoding API is superior to Nominatim, but it requires an API key and more set up. To enable the Google Geocoding API and get an API key, see [Get Started with Google Maps Platform](https://developers.google.com/maps/gmp-get-started) and [Get Started with Geocoding API](https://developers.google.com/maps/documentation/geocoding/start).

#from geopy.geocoders import GoogleV3
#google_geolocator = GoogleV3(api_key="YOUR-API-KEY HERE")
#google_geolocator.geocode("Cayuga Street")

### Get Address

print(location.address)

### Get Latitude and Longitude

print(location.latitude, location.longitude)

### Get "Importance" Score

print(f"Importance: {location.raw['importance']}")

### Get Class and Type

print(f"Class: {location.raw['class']} \nType: {location.raw['type']}")

### Get Multiple Possible Matches

possible_locations = geolocator.geocode("College Ave", exactly_one=False)

for location in possible_locations:
    print(location.address)
    print(location.latitude, location.longitude)
    print(f"Importance: {location.raw['importance']}")

location = geolocator.geocode("College Ave, Ithaca NY")

print(location.address)
print(location.latitude, location.longitude)
print(f"Importance: {location.raw['importance']}")

## Geocode with Pandas

To geocode every location in a CSV file, we can use Pandas, make a Python function, and `.apply()` it to every row in the CSV file.

import pandas as pd
pd.set_option("max_rows", 400)
pd.set_option("max_colwidth", 400)

Here we make a function with `geolocator.geocode()` and ask it to return the address, lat/lon, and importance score:

def find_location(row):
    
    place = row['place']
    
    location = geolocator.geocode(place)
    
    if location != None:
        return location.address, location.latitude, location.longitude, location.raw['importance']
    else:
        return "Not Found", "Not Found", "Not Found", "Not Found"

To start exploring, let's read in a CSV file with a list of places in and around Ithaca.

ithaca_df = pd.read_csv("../data/ithaca-places.csv")

ithaca_df

Now let's `.apply()` our function to this Pandas dataframe and see what results Nominatim's geocoding service spits out.

ithaca_df[['address', 'lat', 'lon', 'importance']] = ithaca_df.apply(find_location, axis="columns", result_type="expand")
ithaca_df

**What do you notice about these results?** ☝️☝️☝️

<a href="https://exhibits.library.cornell.edu/biggest-little-fashion-city/feature/wharton-studio-inc"><img src="https://photos.wikimapia.org/p/00/05/41/92/38_big.jpg" ></a>

**[Wharton Studio Inc.](https://exhibits.library.cornell.edu/biggest-little-fashion-city/feature/wharton-studio-inc)** (1914-1919) — early 20th-century Ithaca movie studio, located in what is now Stewart Park  
*To check out more historical photos of Wharton Studio Inc., see [the Cornell library](https://digital.library.cornell.edu/catalog/ss:550440).*

# Making Interactive Maps

To map our geocoded coordinates, we're going to use the Python library [Folium](https://python-visualization.github.io/folium/). Folium is built on top of the popular JavaScript library [Leaflet](https://leafletjs.com/).

To install and import Folium, run the cells below:

!pip install folium

import folium

### Base Map

First, we need to establish a base map. This is where we'll map our geocoded Ithaca locations. To do so, we're going to call `folium.Map()`and enter the general latitude/longitude coordinates of the Ithaca area at a particular zoom.

(To find latitude/longitude coordintes for a particular location, you can use Google Maps, [as described here](https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=en).)

ithaca_map = folium.Map(location=[42.44, -76.5], zoom_start=14)
ithaca_map

### Add a Marker

Adding a marker to a map is easy with Folium! We'll simply call `folium.Marker()` at a particular lat/lon, enter some text to display when the marker is clicked on, and then add it to our base map.

folium.Marker(location=[42.444695, -76.482233], popup="Intro to Cultural Analytics").add_to(ithaca_map)
ithaca_map

### Add Markers From Pandas Data

To add markers for every location in our Pandas dataframe, we can make a Python function and `.apply()` it to every row in the dataframe.

def create_map_markers(row, map_name):
    folium.Marker(location=[row['lat'], row['lon']], popup=row['place']).add_to(map_name)

Before we apply this function to our dataframe, we're going to drop any locations that were "Not Found" (which would cause `folium.Marker()` to return an error).

found_ithaca_locations = ithaca_df[ithaca_df['address'] != "Not Found"]

found_ithaca_locations.apply(create_map_markers, map_name=ithaca_map, axis='columns')
ithaca_map

### Save Map

ithaca_map.save("Ithaca-map.html")

## Torn Apart / Separados

The data in this section was drawn from [Torn Apart / Separados Project](https://github.com/xpmethod/torn-apart-open-data). It maps the locations of Immigration and Customs Enforcement (ICE) detention facilities, as featured in [Volume 1](http://xpmethod.plaintext.in/torn-apart/volume/1/).

### Add a Circle Marker

There are a few [different kinds of markers](https://python-visualization.github.io/folium/quickstart.html#Markers) that we can add to a Folium map, including circles. To make a circle, we can call `folium.CircleMarker()` with a particular radius and the option to fill in the circle. You can explore more customization options in the [Folium documentation](https://python-visualization.github.io/folium/modules.html#folium.vector_layers.CircleMarker). We're also going to add a hover `tooltip` in addition to a `popup`.

def create_ICE_map_markers(row, map_name):
    
    folium.CircleMarker(location=[row['lat'], row['lon']], raidus=100, fill=True,
                popup=folium.Popup(f"{row['Name'].title()} <br> {row['City'].title()}, {row['State']}", max_width=200),
                  tooltip=f"{row['Name'].title()} <br> {row['City'].title()}, {row['State']}"
                 ).add_to(map_name)

ICE_df = pd.read_csv("../data/ICE-facilities.csv")
ICE_df

US_map = folium.Map(location=[42, -102], zoom_start=4)
US_map

ICE_df = ICE_df.dropna(subset=['lat', 'lon'])

ICE_df.apply(create_ICE_map_markers, map_name=US_map, axis="columns")
US_map

## Choropleth Maps

```margin Choropleth Map
Choropleth map = a map where areas are shaded according to a value
```

The data in this section was drawn from [Torn Apart / Separados Project](https://github.com/xpmethod/torn-apart-open-data). This data maps the "cumulative ICE awards since 2014 to contractors by congressional district," as featured in [Volume 2](http://xpmethod.plaintext.in/torn-apart/volume/2/).

To create a chropleth map with Folium, we need to pair a "geo.json" file (which indicates which parts of the map to shade) with a CSV file (which includes the variable that we want to shade by).

The following data was drawn from [the Torn Apart / Separados project](https://github.com/xpmethod/torn-apart/tree/master/data/districts)

US_districts_geo_json = "../data/ICE_money_districts.geo.json"

US_districts_csv = pd.read_csv("../data/ICE_money_districts.csv")

US_districts_csv = US_districts_csv .dropna(subset=['districtName', 'representative'])

US_districts_csv

US_map = folium.Map(location=[42, -102], zoom_start=4)

folium.Choropleth(
    geo_data = US_districts_geo_json,
    name = 'choropleth',
    data = US_districts_csv,
    columns = ['districtName', 'total_awards'],
    key_on = 'feature.properties.districtName',
    fill_color = 'GnBu',
    line_opacity = 0.2,
    legend_name= 'Total ICE Money Received'
).add_to(US_map)

US_map

### Add a Tooltip to Choropleth

tooltip = folium.features.GeoJson(
    US_districts_geo_json,
    tooltip=folium.features.GeoJsonTooltip(fields=['representative', 'state', 'party', 'total_value'], localize=True)
                                )
US_map.add_child(tooltip)
US_map