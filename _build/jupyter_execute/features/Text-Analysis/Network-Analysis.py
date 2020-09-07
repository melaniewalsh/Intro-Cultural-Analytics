## Named Entity Recognition — Cluster Characters

#!pip install spacy
#!python -m spacy download en_core_web_sm

!pip install fuzzywuzzy

!pip install python-Levenshtein

import spacy

from collections import Counter

import pandas as pd

import itertools

import networkx 
from networkx.algorithms.components.connected import connected_components, node_connected_component

import itertools
from fuzzywuzzy import fuzz

import glob
from pathlib import Path

pd.set_option("max_rows", 400)

import en_core_web_sm
nlp = en_core_web_sm.load()

#nlp = spacy.load('en_core_web_sm')

filepath = "../texts/literature/Jones-Lost-in-The-City.txt"

text = open(filepath).read()

document = nlp(text)

displacy.render(document, style="ent")

## Get People (More Accurately)

Sometimes spaCy will correctly tag a person as a "PERSON" but then later tag the same person as a different entity as an organization ("ORG") or a place ("GPE").

So, to get a more accurate character count, we're going to extract all the named entities that spaCy identified as a "PERSON" and then count *any* instance of that entitiy, regardless of its NER label.

Extract list of all named entities labeled "PERSON":

spacy_identified_people = []

for named_entity in document.ents:
    if named_entity.label_ == "PERSON":
        
        spacy_identified_people.append(named_entity.text)

Output list of identified to a CSV file and manually edit by hand

pd.DataFrame(Counter(spacy_identified_people).most_common(), columns=['character', 'count']).to_csv('spacy-identified-people.csv', index=False)

Re-upload CSV file for accurate list of people

spacy_identified_people = pd.read_csv('spacy-identified-people.csv')['character'].tolist()

all_people_matches = []
all_people_matches_plus_ids = []

#Get all entity matches for a previously identified person
for named_entity in document.ents:
    if named_entity.text in spacy_identified_people:
        person = named_entity.text
        
        #Remove apostrophe s
        person = person.replace("’s", "").strip()
        person_index = named_entity.start_char
        
        all_people_matches.append(person)
        all_people_matches_plus_ids.append([person, person_index])

people_tally = Counter(all_people_matches)
character_df = pd.DataFrame(people_tally.most_common())
character_df.columns = ['character', 'count']

character_df

## Cluster By Name and Distance


spaCy doesn't know that "Betsy Ann Morgan" and "Betsy Ann" should be the same person. So we're also going to pair two character names if they're an extremely close match and they occur within 800 characters of one another.

from datetime import datetime
startTime = datetime.now()

aggregated_people = []

threshold_distance = 750

#Get all entity matches for a previously identified person
for person, person_index in all_people_matches_plus_ids:
    for another_person, another_person_index in all_people_matches_plus_ids:
        distance = abs(person_index - another_person_index)
        if distance < threshold_distance:
            
            if person != another_person:
                
                if fuzz.partial_ratio(person, another_person) == 100:
                    aggregated_people.append((person, another_person))
                    
print(datetime.now() - startTime)

With itertools (slightly faster)

from datetime import datetime
startTime = datetime.now()

aggregated_people = []

threshold_distance = 750

#Get all entity matches for a previously identified person
for person, another_person in itertools.combinations(all_people_matches_plus_ids, 2):
        distance = abs(person[1] - another_person[1])
        if distance < threshold_distance:
            
            if person[0] != another_person[0]:
                
                if fuzz.partial_ratio(person[0], another_person[0]) == 100:
                    aggregated_people.append((person[0], another_person[0]))
                    
print(datetime.now() - startTime)

## Make a network!

from datetime import datetime
startTime = datetime.now()

edge_list = []

threshold_distance = 400

#Get all entity matches for a previously identified person
for person, another_person in itertools.combinations(all_people_matches_plus_ids, 2):
        distance = abs(person[1] - another_person[1])
        if distance < threshold_distance:
            
            if person[0] != another_person[0]:
                
                edge_list.append((person[0], another_person[0]))
                    
print(datetime.now() - startTime)

character_df = pd.DataFrame(Counter(edge_list).most_common(), columns=['character_pair', 'edge_weight'])
character_df['character1']=character_df['character_pair'].str[0]
character_df['character2']=character_df['character_pair'].str[1]

character_df

got_df = pd.read_csv('../data/got-edges.csv')

G=networkx.from_pandas_edgelist(got_df, 'Source', 'Target', 'Weight')
#G.add_weighted_edges_from(character_df)

G=networkx.from_pandas_edgelist(character_df, 'character1', 'character2', 'edge_weight')
#G.add_weighted_edges_from(character_df)

import matplotlib.pyplot as plt

networkx.write_graphml(G, 'lost-in-the-city-character-network.graphml', encoding='utf-8')

networkx.draw(G, with_labels=False, font_weight='bold')

import networkx as nx

from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx

# Prepare Data
G = nx.karate_club_graph()

SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "black", "red"
edge_attrs = {}

for start_node, end_node, _ in G.edges(data=True):
    edge_color = SAME_CLUB_COLOR if G.nodes[start_node]["club"] == G.nodes[end_node]["club"] else DIFFERENT_CLUB_COLOR
    edge_attrs[(start_node, end_node)] = edge_color

nx.set_edge_attributes(G, edge_attrs, "edge_color")

# Show with Bokeh
plot = Plot(plot_width=400, plot_height=400,
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot.title.text = "Graph Interaction Demonstration"

node_hover_tool = HoverTool(tooltips=[("index", "@index"), ("club", "@club")])
plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color", line_alpha=0.8, line_width=1)
plot.renderers.append(graph_renderer)

show(plot)

G=networkx.from_pandas_edgelist(character_df, 'character1', 'character2', 'edge_weight')


import bokeh.io
# this is here only for completeness to clarify where
# the methods are nested (you probably already imported this earlier)


bokeh.io.reset_output()
bokeh.io.output_notebook()

degrees = dict(networkx.degree(G))
networkx.set_node_attributes(G, name='node_size', values=degrees)

from bokeh.plotting import figure

HOVER_TOOLTIPS = [
       ("Character", "@index"),
        ("Degree", "@node_size")
]

plot = figure(plot_width=500, plot_height=500, tooltips = HOVER_TOOLTIPS, tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
            x_range=Range1d(-5.1, 5.1), y_range=Range1d(-5.1, 5.1), title='Game of Thrones Network')

#node_hover_tool = HoverTool(tooltips=[])

#plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

graph_renderer = from_networkx(G, networkx.spring_layout, scale=5, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size='node_size', fill_color=Spectral4[0])
graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.8, line_width=1)

plot.renderers.append(graph_renderer)
plot.xgrid.visible = False
plot.ygrid.visible = False
show(plot)

## Circle Graph

from bokeh.models import EdgesAndLinkedNodes, NodesAndLinkedEdges
HOVER_TOOLTIPS = [
       ("Character", "@index"),
        ("Degree", "@node_size")
]

plot = figure(plot_width=500, plot_height=500, tooltips = HOVER_TOOLTIPS, tools="pan,wheel_zoom,save,reset, tap", active_scroll='wheel_zoom',
            x_range=Range1d(-5.1, 5.1), y_range=Range1d(-5.1, 5.1), title='Game of Thrones Network')

graph_renderer = from_networkx(G, networkx.circular_layout, scale=10, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size=10, fill_color=Spectral4[0])
graph_renderer.node_renderer.selection_glyph = Circle(size=10, fill_color=Spectral4[2])
graph_renderer.node_renderer.hover_glyph = Circle(size=10, fill_color=Spectral4[1])

graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)
graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=1)
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=1)

graph_renderer.selection_policy = NodesAndLinkedEdges()
graph_renderer.inspection_policy = EdgesAndLinkedNodes()

plot.renderers.append(graph_renderer)
plot.xgrid.visible = False
plot.ygrid.visible = False
show(plot)


graph_renderer.node_renderer.data_source

graph_renderer.layout_provider.graph_layout.items()

names = []
x_coordinates = []
y_coordinates = []

for name, x_y_coords in graph_renderer.layout_provider.graph_layout.items():
    names.append(name)
    x_coordinates.append(x_y_coords[0])
    y_coordinates.append(x_y_coords[1])

label_map = dict(zip(names, [x_coordinates, y_coordinates]))

G.nodes()

source = ColumnDataSource(data=graph_renderer.layout_provider.graph_layout)

source[0]

LabelSet(x='x', y='y', text='names', level='glyph',
         x_offset=5, y_offset=5, source=source)

values()

type(graph_renderer.layout_provider.graph_layout)





x, y = zip(*graph.layout_provider.graph_layout.values())



from bokeh.models import EdgesAndLinkedNodes, NodesAndLinkedEdges
from bokeh.models import CustomJSTransform, LabelSet

HOVER_TOOLTIPS = [
       ("Character", "@index"),
        ("Degree", "@node_size")
]

plot = figure(plot_width=500, plot_height=500, tooltips = HOVER_TOOLTIPS, tools="pan,wheel_zoom,save,reset, tap", active_scroll='wheel_zoom',
            x_range=Range1d(-5.1, 5.1), y_range=Range1d(-5.1, 5.1), title='Game of Thrones Network')

graph_renderer = from_networkx(G, networkx.spring_layout, scale=5, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size='node_size', fill_color=Spectral4[0])
graph_renderer.node_renderer.selection_glyph = Circle(size='node_size', fill_color='green')
graph_renderer.node_renderer.hover_glyph = Circle(size='node_size', fill_color='red')

graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)
graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color='green', line_width=1)
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color='red', line_width=1)


graph_renderer.selection_policy = NodesAndLinkedEdges()
graph_renderer.inspection_policy = NodesAndLinkedEdges()



plot.renderers.append(graph_renderer)
plot.xgrid.visible = False
plot.ygrid.visible = False



from bokeh.transform import transform    

# add the labels to the node renderer data source
source = graph_renderer.node_renderer.data_source
source.data['names'] = [str(x) for x in source.data['index']]

# create a transform that can extract the actual x,y positions
code = """
    var result = new Float64Array(xs.length)
    for (var i = 0; i < xs.length; i++) {
        result[i] = provider.graph_layout[xs[i]][%s]
    }
    return result
"""
xcoord = CustomJSTransform(v_func=code % "0", args=dict(provider=graph_renderer.layout_provider))
ycoord = CustomJSTransform(v_func=code % "1", args=dict(provider=graph_renderer.layout_provider))

# Use the transforms to supply coords to a LabelSet 
labels = LabelSet(x=transform('index', xcoord),
                  y=transform('index', ycoord),
                  text='names', text_font_size="12px",
                  x_offset=5, y_offset=5,
                  source=source, render_mode='canvas')

plot.add_layout(labels)
show(plot)




plot = Plot(plot_width=1000, plot_height=1000,
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))

node_hover_tool = HoverTool(tooltips=[("", "@index")])
plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

graph_renderer = from_networkx(G, networkx.spring_layout, scale=2, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.8, line_width=1)
plot.renderers.append(graph_renderer)

show(plot)

!pip install visJS2jupyter

!pip install py2cytoscape

import visJS2jupyter.visJS_module

nodes = G.nodes()
edges = list(G.edges())

nodes_dict = [{"id":n, "x":pos[n][0]*300, "y":pos[n][1]*300} for n in nodes]
node_map = dict(zip(nodes,range(len(nodes))))  # map to indices for source/target in edges

for i in range(len(edges)):
    print(node_map[edges][i][0])
    #"source":node_map[edges[i][0]], "target":node_map[edges[i][1]]} 

nodes = list(G.nodes()) # must cast to list to maintain compatibility between nx 1.11 and 2.0
edges = list(G.edges())

!pip show bokeh

from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx
from bokeh.io import output_notebook, show

output_notebook()

!pip install pygraphviz

degrees = [degree for node, degree in networkx.degree(G)]

degrees = networkx.degree(G)

G.get_node_attributes()

networkx.info(G)

from bokeh.models import ColumnDataSource

node_size = {k:5*v for k,v in G.degree()} 

degree = networkx.degree(G)
networkx.set_node_attributes(G,  degree, 'degree')

degrees = dict(networkx.degree(G))
networkx.set_node_attributes(G, name='node_size', values=degrees)

pd.DataFrame.from_dict({k:v for k,v in G.nodes(data=True)}, orient='index')

node_source = ColumnDataSource(pd.DataFrame.from_dict({k:v for k,v in G.nodes(data=True)}, orient='index'))

plot = Plot(plot_width=400, plot_height=400,
            x_range=Range1d(-1.1,1.1), y_range=Range1d(-1.1,1.1))

graph_renderer = from_networkx(G, networkx.spring_layout, scale=10, center=(0,0))

#style
graph_renderer.node_renderer.data_source = node_source
graph_renderer.node_renderer.glyph = Circle(fill_color = 'blue',size = 'node_size' , line_color = None)

graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=2)


plot.renderers.append(graph_renderer)

show(plot)

# Prepare Data
#G = nx.karate_club_graph()

#SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "black", "red"
#edge_attrs = {}

# for start_node, end_node, _ in G.edges(data=True):
#     edge_color = SAME_CLUB_COLOR if G.nodes[start_node]["club"] == G.nodes[end_node]["club"] else DIFFERENT_CLUB_COLOR
#     edge_attrs[(start_node, end_node)] = edge_color

# nx.set_edge_attributes(G, edge_attrs, "edge_color")

# Show with Bokeh
plot = Plot(plot_width=1000, plot_height=1000,
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))

#plot.title.text = "Lost in the City Characters"

node_hover_tool = HoverTool(tooltips=[("", "@index")])
plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

graph_renderer = from_networkx(G, networkx.spring_layout, scale=10, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
#graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.8, line_width=1)
plot.renderers.append(graph_renderer)

#output_file("interactive_graphs.html")
show(plot)

fig = networkx.draw_networkx(G)
fig(figsize=(20,10))

fig, ax = plt.subplots(1, 1, figsize=(20, 10));
networkx.draw_networkx(G, ax=ax, with_labels=True)

import json

nodes = [{'name': str(i)}
         for i in G.nodes()]
links = [{'source': u[0], 'target': u[1]}
         for u in G.edges()]
with open('graph.json', 'w') as f:
    json.dump({'nodes': nodes, 'links': links},
              f, indent=4,)

<div id="d3-example"></div>
<style>
.node {stroke: #fff; stroke-width: 1.5px;}
.link {stroke: #999; stroke-opacity: .6;}
</style>

With the aggregated character names, we're going to use the Python library networkX to create a cluster of character names.

G=networkx.Graph()
G.add_edges_from(aggregated_people)
people_clusters  = list(connected_components(G))
people_clusters = [sorted(cluster, key=len, reverse=True) for cluster in people_clusters]
people_clusters

def add_clustered_characters(row):
    character = row['character']
    for cluster in people_clusters:
        if character in cluster:
            return cluster

def clean_and_unpack_cluster(row):
    if row['clustered_characters'] == None:
        cluster = row['character']
    else:
        cluster = " // ".join(row['clustered_characters'])
    return cluster

character_df['clustered_characters'] = character_df.apply(add_clustered_characters, axis=1)

character_df['clustered_characters'] = character_df.apply(clean_and_unpack_cluster, axis=1)

character_df

Manually edit

#character_df.sort_values(by=['clustered_characters', 'count']).to_csv('clustered_characters_draft.csv')

#character_df = pd.read_csv('clustered_characters_edited.csv')

character_df.groupby('clustered_characters')[['count']].sum().sort_values(by='count', ascending=False).reset_index()

## Cluster By Name

from fuzzywuzzy import process

def cluster_characters(row):
    possibilities = process.extract(row['character'], character_df['character'].unique(), scorer=fuzz.partial_ratio)
    possibilities = [possible[0] for possible in possibilities if possible[1] == 100]
    possibilities = [combo for combo in itertools.combinations(possibilities, 2)]
    return possibilities

clustered_by_named = character_df.apply(cluster_characters, axis=1)



G=networkx.Graph()
G.add_edges_from(clustered_by_named)
people_clusters  = list(connected_components(G))
people_clusters = [sorted(cluster, key=len, reverse=True) for cluster in people_clusters]
people_clusters

def add_clustered_characters(row):
    character = row['character']
    for cluster in people_clusters:
        if character in cluster:
            return cluster

def clean_and_unpack_cluster(row):
    if row['clustered_characters'] == None:
        cluster = row['character']
    else:
        cluster = " // ".join(row['clustered_characters'])
    return cluster

character_df['clustered_characters'] = character_df.apply(add_clustered_characters, axis=1)

character_df['clustered_characters'] = character_df.apply(clean_and_unpack_cluster, axis=1)

character_df