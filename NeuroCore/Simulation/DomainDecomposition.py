'''
Created on May 29, 2014

@author: dabrunhosa
'''

from copy import copy

import networkx as nx
import numpy as np
from NeuroCore.Simulation.IData import Segment_Info

from NeuroCore.Models.Conditions import Neumann
from NeuroCore.Simulation.ICore import ICore
from Utilities.DataEntry import Options, Options_User


class DomainDecomposition(ICore):
    
    ########################################
    ###       Private Variables          ###
    ######################################## 
    
    # All the attributes allowed to be access.
    class_attributes = ['int_connections','segments_connected',
                        'model','edges_segment','decomposition_table',
                        'edge_decomposition']
    
    # Class to threat the Option Class 
    class_option = Options_User()
    
    ########################################
    ###           Constructor            ###
    ######################################## 
    
    def __init__(self,segments_connected,connection_scheme,\
                 model,edges_segment,boundary_conditions):
        
        self.__name = "Domain Decomposition"
        self.__global_conditions = boundary_conditions
        
        int_connections = nx.DiGraph()
        int_connections.add_edges_from(connection_scheme.edges())
            
        
        # Define the class options
        class_options = Options(int_connections = int_connections,
                                segments_connected = segments_connected,
                                model = model,
                                edges_segment = edges_segment,
                                decomposition_table = Set('Decomposition_Table'),
                                edge_decomposition = list())
        
        # Initialize the options
        self.class_option.init_options(self,class_options,{})
        
    ########################################
    ###       Private Functions          ###
    ######################################## 
        
    def _get_correct_segment(self,connected_segments,nodes):        
        try: 
            return [connected_segments[connected_segments.index((nodes[0],nodes[-1]))],(nodes[0],nodes[-1])]
        except:
            return [connected_segments[connected_segments.index((nodes[-1],nodes[0]))],(nodes[-1],nodes[0])]
        
    def _already_set(self,continuity,connected_segment):
        
        for item in continuity:
            if (item[0] in connected_segment) or (item[-1] in connected_segment):
                return True
            
        return False
        
    def _create_decomposition_table(self,boundary_conditions):
        do_loop = True
        available_segments = copy(self.segments_connected.keys())
        
        current_line = -1
        current_column = 0
        
        while do_loop:
            processing = available_segments[-1]
            
            if not self.decomposition_table.contains_key(processing):
                info = Segment_Info()                        
            else:
                info = self.decomposition_table.get(processing)
            
            info.connected.extend(self.segments_connected.get(processing))
            
            for node in processing:
                try: 
                    info.nodes_handled.index(node)
                except:
                    for segment_connected in info.connected:
                        if node in segment_connected:
                            current_line += 1
                            info.continuity.add(segment_connected,(current_line,1))
                            
                            if not self.decomposition_table.contains_key(segment_connected):
                                temp_info = Segment_Info()
                                temp_info.continuity.add(processing,(current_line,-1)) 
                                self.decomposition_table.add(segment_connected,temp_info)                       
                            else:
                                temp_info = self.decomposition_table.get(segment_connected)
                                temp_info.continuity.add(processing,(current_line,-1))
                                self.decomposition_table.set(segment_connected,temp_info)
                                
                            
            
            for node in processing:
                
                try:
                    info.nodes_handled.index(node)
                except:
                
                    node_id = 0
                    sign = 1
                    
                    predecessors = self.int_connections.predecessors(node)
                    sucessors = self.int_connections.successors(node)
                    
                    if node == processing[0]:
                        node_id = -1
                        sign = -1
                    else:
                        node_id = 0
                        sign = 1
                    
                    other_node = processing[node_id]
                    
                    try:
                        predecessors.remove(other_node)
                    except:
                        if len(sucessors) > 0:
                            sucessors.remove(other_node)
                        
                    connections = predecessors + sucessors
                    already_set = False
                    
                    for connect in connections:
                
                        [temp_segment,temp_edge] = self._get_correct_segment(info.connected, [connect,node])
                        temp_info = self.decomposition_table.get(temp_segment)
                        
                        try:
                            temp_info.derivative.get(node)
                        except: 
                            if not already_set:
                                current_line += 1
                                info.derivative.add(node,(current_line,sign))
                                info.nodes_handled.append(node)
                                already_set = True
                                
                            if temp_edge[0] == node: 
                                temp_sign = -1
                            else:
                                temp_sign = 1
                            
                            temp_info.derivative.add(node,(current_line,temp_sign))
                            temp_info.nodes_handled.append(node)
                            self.decomposition_table.set(temp_segment,temp_info)
            
            if (processing[0] in boundary_conditions.keys()) or \
                        (processing[1] in boundary_conditions.keys()):
                    
                    if processing[0] in boundary_conditions.keys():
                        current_line += 1
                        info.boundary.add((current_line,0),boundary_conditions.get(processing[0]))
                        
                    if processing[1] in boundary_conditions.keys():
                        current_line += 1
                        info.boundary.add((current_line,1),boundary_conditions.get(processing[1]))
               
            info.column = (current_column,current_column+1)
            
            if not self.decomposition_table.contains_key(processing):
                self.decomposition_table.add(processing,info)
            else:
                self.decomposition_table.set(processing,info)
            
            current_column += 2
            available_segments.pop()
            
            if len(available_segments) == 0:
                do_loop = False
        
    def __setattr__(self,attributeName,value):
        
        # Check if the given attribute is 
        # an allowed one.
        if attributeName in self.class_attributes:
            # If it's add it to the internal
            # dictionary
            self.__dict__[attributeName] = value
        else:
            error_message = "The attribute: '"+attributeName+ \
                            "' is not an allowed attribute to set."
            
            raise AttributeError(error_message)
        
    def __getattr__(self,attributeName):
        
        if attributeName in self.class_attributes:
            return self.__dict__[attributeName]
        elif attributeName == 'options':
            return self.class_attributes
        else:
            error_message = "The attribute name: "+attributeName+ \
                            " is not an allowed attribute to get."
            raise AttributeError(error_message)
        
    def _assemble_decomposition(self):
        
        num_segments = len(self.decomposition_table)
        
        decomposition_matrix = np.zeros([2*num_segments,2*num_segments])
        decomposition_font = np.zeros([2*num_segments,1])
        
        for segment_edge,segment_info in self.decomposition_table.items():
#             print segment_edge,segment_info
            column_0 = segment_info.column[0]
            column_1 = segment_info.column[1]
            
            segment = self.edges_segment.get(segment_edge)
#             print segment.v_result
            
            for edge,info in segment_info.continuity.items():
                
                if segment_edge[0] in edge:
                    v_til_position = 0
                else:
                    v_til_position = 1
                
                continuity_line = info[0]
                continuity_sign = info[1]
                
                decomposition_matrix[continuity_line,column_0] = continuity_sign*segment.v_result.get('v_til_1')[v_til_position]
                decomposition_matrix[continuity_line,column_1] = continuity_sign*segment.v_result.get('v_til_2')[v_til_position]
                
                decomposition_font[continuity_line] += -continuity_sign*segment.v_result.get('v_hat')[v_til_position]
              
            for derivative in segment_info.derivative.values():
                derivative_line = derivative[0]
                derivative_value = derivative[1]
                
                if derivative_value < 0:
                    column = column_0
                else:
                    column = column_1
                    
                decomposition_matrix[derivative_line,column] = derivative_value
                  
            for info,boundary in segment_info.boundary.items():               
                boundary_line = info[0]
                column = segment_info.column[info[1]]
                
                decomposition_font[boundary_line] = boundary.get_value()
                
                if boundary.get_type() == 'Dirichlet':
                    decomposition_matrix[boundary_line,column_0] = segment.v_result.get('v_til_1')[column]
                    decomposition_matrix[boundary_line,column_1] = segment.v_result.get('v_til_2')[column]
                    decomposition_font[boundary_line] -= segment.v_result.get('v_hat')[column]
                elif boundary.get_type() == 'Neumann':
                    decomposition_matrix[boundary_line,column] = 1
                    
        return [decomposition_matrix,decomposition_font]                
                       
    def _solve_decomposition(self,decomposition_matrix,decomposition_font):
        
        lambda_results = np.linalg.solve(decomposition_matrix, decomposition_font)
        
        for segment_edge in self.decomposition_table:
            segment = self.edges_segment.get(segment_edge)
            
            lambda_1 = lambda_results[segment_edge[0]]
            lambda_2 = lambda_results[segment_edge[1]]
            
            v_til_1 = segment.v_result.get('v_til_1')[2]
            v_til_2 = segment.v_result.get('v_til_2')[2]
            v_hat = segment.v_result.get('v_hat')[2]
            
            segment.results.append(lambda_1*v_til_1 + lambda_2*v_til_2 + v_hat) 
  

    ########################################
    ###       Public Functions           ###
    ########################################       
                    
    def solve(self,delta_t,final_time):
        
        # Create the Decomposition Table
        self._create_decomposition_table(self.__global_conditions)
        
        segment_conditions = ("v_til_1",[Neumann(1,0),Neumann(0,1)]),("v_til_2",[Neumann(0,0),Neumann(1,1)]),("v_hat",[Neumann(0,0),Neumann(0,1)])
        number_time_loops = (int)(final_time / delta_t)
        
        for i in range(number_time_loops):
            for segment in self.edges_segment.values():
                segment.run((i+1)*delta_t,segment_conditions,self.model)
              
            [decomposition_matrix,decomposition_font] = self._assemble_decomposition()
            self._solve_decomposition(decomposition_matrix,decomposition_font)
            
        for segment in self.edges_segment.values():
#             self.solution_error(segment,delta_t)
            self.show_results_simpler(segment) 
