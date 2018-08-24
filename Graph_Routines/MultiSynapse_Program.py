#'''
#Created on 12/12/2014

#@author: dabrunhosa
#'''
#from collections import defaultdict
#import networkx as nx
#import matplotlib.pyplot as plt
#from collections import Iterable

#class Multi_Mapping():

#    ###################################
#    ##  GLOBAL VARIABLES            ###
#    ###################################
    
#    dendAxonSynapseDict = None
#    dendConvertTable = None
#    convDendTable = None
#    synapse_graph = None
    
#    ###################################
#    ##  FUNCTIONS                   ###
#    ###################################
    
#    def __init__(self):
#        self.dendAxonSynapseDict = defaultdict(dict)
#        self.dendConvertTable = defaultdict(dict)
#        self.convDendTable = defaultdict(dict)
        
#    def get_all_nodes(self):
#        all_nodes = []
        
#        for node in self.synapse_graph.nodes():
#            dendNumber = node.find('p')
#            if dendNumber > -1:
#                all_nodes.append(str(node[0:dendNumber]))
#            else:
#                all_nodes.append(str(node))
                
#        return all_nodes
        
#    def _breakInfo(self,line):
#        parts = []
#        string_data = line
        
#        while string_data != "":
#            partitions = string_data.partition(",")
            
#            if partitions[-1] != "\n":
#                parts.append(partitions[0].partition("\n")[0])
#                string_data = partitions[-1]
                
#        return parts
    
#    '''This function is designed to read the synapse pairs
#    file and arrange the information in various dictionaries
#    to be read at a later state. 
    
#    Because of some weird error finding strings, it was 
#    necessary to create two dictionaries for the conversion
#    of strings back and forth'''
#    def readFile(self,synapse_file):
#        #Read File
#        synapsePairs = open(synapse_file,"r")
#        self.synapse_graph = nx.MultiGraph()
        
#        #Conversion Number - Negative to
#        # be able differentiate from axons
#        conv_number = -1
        
#        while 1:
#            #Read line by line of the file
#            line = synapsePairs.readline()
            
            
#            if not line:
#                break
            
#            # Find dendrite and axon
#            spacePos = line.find("-")+1
#            endString = line.find("\n")
            
#            processName =  line[0:spacePos-1]
#            connectionsNames = self. _breakInfo(line[spacePos:endString]) 
            
#            for name in connectionsNames:
                
#                divisionPos = name.find("_")
#                dendName = name[0:divisionPos]
#                dendAttribute = name[divisionPos+1:]
                
#                self.synapse_graph.add_edge(processName, dendName, weight=1,attribute=dendAttribute)
    
            
#    '''
#    Function receive the name of the axons or axon or dendrite or dendrites
#    and return all the dendrites or axons that are connected to it.
#    '''
#    def retrieveNeighboors(self,axons_name):
#        dendrites = []
        
#        if not isinstance(axons_name, Iterable) or isinstance(axons_name, str):
#            axons_name = [axons_name]
            
#        for axon in axons_name:

#            tempDict = self.synapse_graph[axon]

#            neighbors = []
            
#            try:
#                for process,info in tempDict.items():
#                    neighbors.append(process+ '_'+ info.values()[0]['attribute'])
#            except nx.NetworkXError as error: 
#                print error.message
#                continue
            
#            dendrites.append(neighbors)
            
#        return dendrites
    
#    '''
#    Function draws the synapse graph.
#    '''
#    def drawGraph(self):
#        # positions for all nodes       
#        pos = nx.spring_layout(self.synapse_graph)
                        
#        # nodes
#        plt.figure(num=None, figsize=(300, 300), dpi=100, facecolor='w', edgecolor='k')
#        nx.draw_networkx_nodes(self.synapse_graph,pos,node_size=400)
            
#        # edges
#        nx.draw_networkx_edges(self.synapse_graph,pos,width=1.2)
         
#        # labels for the nodes
#        nx.draw_networkx_labels(mg.synapse_graph,pos,font_size=13,font_family='sans-serif')
            
#        #plt.savefig('multiGraph.pdf')
#        plt.show()
        
#    def graphProperties(self):
#        #Basic Degrees of graph
#        degree = self.synapse_graph.degree(self.synapse_graph.nodes())
         
#        #Density of Graph (number possible to present
#        density = nx.density(self.synapse_graph)
         
#        #Transitivity (Mean cluster normalized)
#        transitivity = nx.transitivity(self.synapse_graph)
         
#        # The eccentricity of a node v is the maximum distance from v to all other nodes in G.
#        #eccentricity = nx.eccentricity(graph)
         
#        #Betweenness Centrality (Fraction of shortest path that pass through node).
#        bet_centrality = nx.betweenness_centrality(self.synapse_graph)
         
#        #Closenness Centrality
#        clos_centrality = nx.closeness_centrality(self.synapse_graph)
        
#        graph_properties = defaultdict(dict)
        
#        graph_properties['degree_all_nodes'] = degree
#        graph_properties['Density'] = density
#        graph_properties['Transitivity'] = transitivity
#        graph_properties['Betweenness Centrality'] = bet_centrality
#        graph_properties['Closenness Centrality'] = clos_centrality
        
#        return graph_properties
    
#    ''' 
#    This method was designed to calculate the distance between two dendrites.
#    The paths are calculated using the shortest path algorithm in a Graph, in
#    this way we get all the shortest paths. To get all the simple paths, the 
#    algorithm takes to long to process.
#    '''
#    def find_path(self,source,target):
        
#        print list(nx.all_simple_paths(self.synapse_graph, source, target, 7))
        
#        print "After Simple Path"        
#        print "Finding paths .... "
#        print list(nx.all_shortest_paths(self.synapse_graph, source, target))
##         print list(nx.all_simple_paths(synapse_graph, conv_number_a, conv_number_b))
#if __name__ == '__main__':
#    mg = Multi_Mapping()
#    mg.readFile('all_process_connections.txt')
#    mg.drawGraph()
## 
#    print "Axons connected to d000 are: ",mg.retrieveNeighboors("d000p")
##multiGraph.find_path("d001p", "d009p")
### 
##print multiGraph.synapse_graph.edges(["d01","a151"],data=True)
##print multiGraph.get_all_nodes()
