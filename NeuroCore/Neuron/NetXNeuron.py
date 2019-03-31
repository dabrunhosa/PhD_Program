# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

import networkx as nx

from NeuroCore.Models.Conditions.Dirichlets import Dirichlet
from NeuroCore.Neuron.INeuron import INeuron
from Conventions.Classes import Names
from Conventions.NeuroCore.Neuron.Segment.Base import BaseParameters as constants
# -*- coding: utf-8 -*- This program will define a generalized form of segment
# that can incorporate: Axon, Mylenized Axon, Ranvier Node, Soma and Dendrites
from Utilities.DataEntry import Options

class MeshError(AttributeError): 
    pass

class NetXNeuron(INeuron):

    ########################################
    ###           Constructor            ###
    ########################################

    def __init__(self, options=Options(), defaultOptions=Options(), **kw):
        # Define the default options
        inDefaultOptions = Options(**{constants().Name: Names().NetXNeuron,
                                      constants().Structure: nx.DiGraph(),
                                      constants().NeuronName: None,
                                      constants().GlobalConditions: None})

        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions

        super(NetXNeuron, self).__init__(options=options, defaultOptions=defaultOptions, **kw)
        
        
    ########################################
    ###       Public Functions           ###
    ######################################## 
    
    def insert_segments(self,segment):
        
        # Defines the Segment nodes 
        node_0 = self.node_count
        node_1 = self.node_count + 1
        
        # Add the Segment (as an edge) and nodes for the 
        # internal Graph structure.
        self.mesh.add_edge(node_0,node_1,weight=1,
                     attr_dict={'segment':segment})
        
        # Add the Segment - Node relation to the 
        # internal Set structure.
        self.segment_nodes[segment] = (node_0,node_1)
        
        # Updates the next node numbers
        self.node_count += 2
       
    def connect_segments(self,first_segment,second_segment,first_pos=1,sec_pos=0):
        
        # Check if the connection positions are correct
        if (first_pos != 0 and first_pos != 1) or (sec_pos != 0 and sec_pos != 1):
            
            error_message = 'unexpected value for first_pos or '\
                            +'sec_pos got'+str(first_pos)+' and '\
                            +str(sec_pos)+' expecting 0 or 1.'\
                            +'The segments are connected'\
                            +'in the beginning and end using a'\
                            +'reference element system. The beginning is'\
                            +' represented by 0 and the end by 1.'
            
            raise MeshError(error_message)
        
        try:
            # Get the Nodes from each segment
            first_segment_nodes = self.segment_nodes.get(first_segment)
            second_segment_nodes = self.segment_nodes.get(second_segment)
            
        except KeyError:
            error_message = "The segments have to be inserted first."
            
            raise MeshError(error_message)
        
        # Get the nodes that should be merged. When two
        # edges are connected one of the nodes in the 
        # connection points should be removed and the
        # other gets the connections from the removed one.
        first_node = first_segment_nodes[first_pos]
        second_node = second_segment_nodes[sec_pos]
        
        geometric_mesh = self.mesh
        
        if  geometric_mesh.degree(first_node) == 3 or \
            geometric_mesh.degree(second_node) == 3:
            
            error_message = "one of the segments is in the maximum "\
                            +"capacity of three connections. "\
                            +first_segment.name+" connections: "\
                            +str(geometric_mesh.degree(first_node))\
                            +" ."+second_segment.name+" connections: "\
                            +str(geometric_mesh.degree(second_node))\
                            +"."
            
            raise MeshError(error_message)
        else:
            
            # Get all the edges (successors of the node) 
            # and organize all the information
            for edge in geometric_mesh.edges(second_node):
                
                edge_data = geometric_mesh.get_edge_data(*edge)
                
                geometric_mesh.add_edge(first_node,edge[1],weight=1\
                                        ,attr_dict=\
                                        {'segment':edge_data['segment']})
                                
                self.segment_nodes.set(edge_data['segment'],(first_node,edge[1]))
             
            # Organize the predecessors    
            for predecessor in geometric_mesh.predecessors(second_node):
                  
                edge = (predecessor, second_node)
                edge_data = geometric_mesh.get_edge_data(*edge)
                  
                geometric_mesh.add_edge(predecessor,first_node,weight=1\
                                        ,attr_dict=\
                                        {'segment':edge_data['segment']})
                                  
                self.segment_nodes.set(edge_data['segment'],(predecessor,first_node))
            
            # Now that everything is done, the 
            # node is removed.  
            geometric_mesh.remove_node(second_node)
            
    def __define_boundary_conditions(self):
        
        boundary_conditions = {}
        
        for node in self.__mesh.nodes():
            
            if self.__mesh.degree(node) == 1:
                boundary_conditions[node] = Dirichlet(0)
                    
        return boundary_conditions 
    
    def _get_connections(self,segments):
        
        segment_nodes = self.__segment_nodes
        edge_segment = {}
        segments_connected = {}
        
        geo_mesh = self.__mesh
        all_edges = geo_mesh.edges()
        
#         print segment_nodes
#         print nodes_segment
        
        for segment in segments:
            
            edge = segment_nodes.get(segment)
            segment_edges = list()
            
            for poss_edge in all_edges:
                if edge[0] in poss_edge or edge[-1] in poss_edge:
                    segment_edges.append(poss_edge)
            
            
            segment_edges.remove(edge)
            
            segments_connected[edge] = segment_edges
            edge_segment[edge] = segment
        
        return [segments_connected,edge_segment]    
        
    def _get_segments(self,edges=None):
        
        # If no edges are passed return
        # all the segments in the mesh.
        if edges is None:
            return self.__segment_nodes.keys()
        else:
            pass
        
    def _get_mesh(self,segments=None):
        
        # If no segments are passed
        # so need to return entire
        # mesh.
        if segments is None:
            return self.__mesh
        else:
            triples = list()
            segment_nodes = self.__segment_nodes
            
            for segment in segments:
                temp_list = list(segment_nodes[segment])
                temp_list.append({"segment":segment})               
                triples.append(tuple(temp_list))
                
            new_graph = nx.DiGraph()
            new_graph.add_edges_from(triples)
            
            return new_graph
        
                
    def create_region(self,model,segments=None):
        
        if segments is None:
            segments = self._get_segments()
        
        [segments_connected,edge_segment] = self._get_connections(segments)
        
        new_region = model.create_region(segments_connected,self._get_mesh(segments),model,edge_segment)
        self.__regions.append(new_region)
        
        return new_region
    
    def identify_boundary_conditions(self):          
        return self.__define_boundary_conditions()
    
    def solve(self,boundary_conditions,delta_t,final_time):
        
        for region in self.__regions:
            region.solve(boundary_conditions,delta_t,final_time)