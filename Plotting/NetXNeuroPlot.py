## -*- coding: utf-8 -*-
#'''
#Created on September 6, 2017

#@author: dabrunhosa
#'''

#from Plotting.IPlot import IPlot 
#import networkx as nx
#from Utilities.Utils import Set
#import operator
#import math
#from Queue import Queue
#import matplotlib.pyplot as plt

#class NetX_NeuroPlot(IPlot):
        
#    ########################################
#    ###       Private Functions          ###
#    ######################################## 
    
#    def __insert_node_level(self,level_sequence,level,node):
        
#        if not level_sequence.contains_key(level):
#            # add the level and a unique list of nodes
#            level_sequence.add(level, set([node]))
#        else:
#            # Find level and add node the Sequence 
#            # will ignore non-unique nodes
#            level_sequence.get(level).add(node)
    
#    def __find_number_levels(self,mesh_origin,origin,flow_direction_name):
        
#        number_levels = 0
#        level_nodes = []
#        begin = False
        
#        for level in mesh_origin.values():
            
#            if flow_direction_name == 'predecessors':
#                if origin in level:
#                    level_nodes.append([origin])
#                    break
#                else:
#                    level_nodes.append(level)
#                    number_levels += 1
#            elif flow_direction_name == 'successors':
                
#                if origin in level:
#                    level_nodes.append([origin])
#                    begin = True
#                elif begin:
#                    level_nodes.append(level)
#                    number_levels += 1
                
#        return [number_levels,level_nodes]
    
#    def __find_origins(self):
        
#        # Create a Set for the New Order
#        # of the nodes
#        new_order = Set('New_Order')
#        geometric_mesh = self.__data
        
#        # Get all the Graph's paths
#        all_paths = nx.shortest_path_length(geometric_mesh)
#        has_path = True
        
#        # Define a default longest path and level
#        current_longest_path = -1
#        current_level = 0
        
#        while has_path:
            
#            # Find the longest path using the iteration object (key,value) and
#            # the Operator class to get the second position of the tuple (value).
#            longest_path = max(all_paths.iteritems(),key=operator.itemgetter(1))

#            longest_path_length = max(longest_path[1].iteritems(),key=operator.itemgetter(1))[1]
            
#            if longest_path_length < current_longest_path:
#                current_level += 1
            
#            # Every time the node of longest path is added
#            # to the appropriated level, the longest path 
#            # is setted and the current path is
#            # deleted from the options
#            self.__insert_node_level(new_order, 'level_'+str(current_level), longest_path[0])
#            current_longest_path = longest_path_length   
#            del all_paths[longest_path[0]]
            
#            if all_paths == {}:
#                has_path = False
                
#        return new_order
    
#    def __find_central_segment(self):
#        geometric_mesh = self.__mesh
        
#        # Calculate the betweenness of the entire graph
#        betweenness_centrality = nx.betweenness_centrality(geometric_mesh)  
        
#        # The node with the higgest score is the central node     
#        central_node = max(betweenness_centrality,key=betweenness_centrality.get)
        
#        biggest_path = -1
#        central_segment = ()
        
#        predecessors = geometric_mesh.predecessors(central_node)
#        sucessors = geometric_mesh.successors(central_node)
        
#        all_neighbors = predecessors + sucessors
        
#        for node in all_neighbors:
#            largest_path = max(nx.shortest_path_length(geometric_mesh, source=node).values())
            
#            if largest_path > biggest_path or biggest_path == -1:
#                biggest_path = largest_path
                
#                if node in predecessors:
#                    edge = (node,central_node)
#                else:
#                    edge = (central_node,node)
                
#                central_segment = edge
                        
#        return central_segment
    
#    def __organize_vertically(self,mesh_origin,origin,flow_direction):
        
#        vertical_list = Queue()
#        neuro_layout = {}
        
#        vertical_list.put_nowait(origin)
        
#        base_level_distance = 0.2
#        level_distance = base_level_distance
#        [number_of_levels,level_nodes] = self.__find_number_levels(mesh_origin, origin,flow_direction.__name__)
#        brothers_distance = lambda distance,angle: (math.sin((math.pi*angle)/180)*distance)*2
        
#        for _ in xrange(0,number_of_levels-1):
#            level_distance *= 2
            
#        level = number_of_levels + 1
#        angle = 120
        
#        if flow_direction.__name__ == 'predecessors':
#            x = 0  
#            y = 0
#            position = -1
#        elif flow_direction.__name__ == 'successors':
#            x = level_distance
#            y = 0
#            position = 0
        
#        neuro_layout[origin] = (x,y)
        
#        while not vertical_list.empty():
            
#            node = vertical_list.get(block = False)
#            first = True
                
            
#            if level_nodes != []:
                    
#                if node not in level_nodes[position]:
#                    level -= 1
#                    level_nodes.pop(position)
#                    level_distance -= 0.1*level_distance
#                    angle -= 0.7*angle
                    
#            if flow_direction.__name__ == 'predecessors':
#                x_dislocation = -level_distance
#            elif flow_direction.__name__ == 'successors':
#                x_dislocation = level_distance 
 
#            for item in flow_direction(node):
#                x = neuro_layout[node][0] + x_dislocation
                
#                if first:
#                    y = neuro_layout[node][1] - (brothers_distance(level_distance,angle)/2)
#                    first = False
#                else:
#                    y = neuro_layout[node][1] + (brothers_distance(level_distance,angle)/2) 
                
#                neuro_layout[item] = (x,y)
#                vertical_list.put_nowait(item)
                
#        return neuro_layout

#    def __neuroscience_layout(self):
        
#        mesh_origins = self.__find_origins()
#        neuroscience_mesh = self.__mesh
#        central_segment = self.__find_central_segment()
        
#        neuro_layout = self.__organize_vertically(mesh_origins,central_segment[0], neuroscience_mesh.predecessors)        
#        neuro_layout.update(self.__organize_vertically(mesh_origins,central_segment[1], neuroscience_mesh.successors))
        
#        return neuro_layout
    
#    ########################################
#    ###       Public Functions          ###
#    ######################################## 
    
#    def show(self):
        
#        scale_factor = 1.2
                
#        if len(self.__data.nodes()) is not 0:  
            
#            # positions for all nodes
#            pos = self.__neuroscience_layout()
            
#            # nodes
#            nx.draw_networkx_nodes(self.__data,pos,node_size=scale_factor*300)
            
#            # edges
#            nx.draw_networkx_edges(self.__data,pos,width=scale_factor*0.5)
            
#            # labels for the nodes
#            nx.draw_networkx_labels(self.__data,pos
#                                    ,font_size=scale_factor*13,
#                                    font_family='sans-serif')

            
#            # labels for the edges
#            edge_labels = {}
            
#            for edge in self.__data.edges():
#                node = self.__data.get_edge_data(*edge)['segment']
#                edge_labels[edge] = node.name
            
#            nx.draw_networkx_edge_labels(self.__data,
#                                    pos,edge_labels=edge_labels,\
#                                    font_size=scale_factor*12,
#                                    font_family='sans-serif')
            
#            plt.show()
#        else:
#            print "The Mesh does not have any elements." 
            
#        def save(self,path_location=None):
#            raise NotImplementedError
