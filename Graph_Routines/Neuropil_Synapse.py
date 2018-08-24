#import Neuropil_Util
#from collections import defaultdict
 
## graph libs
#import networkx as nx
 
#class Synapse_Mapping():
 
#    ###################################
#    ##  GLOBAL VARIABLES            ###
#    ###################################
     
#    synapseConnections = None
#    connection_graph = None
     
#    ###################################
#    ##  FUNCTIONS                   ###
#    ###################################
     
#    def __init__(self):
#        self.synapseConnections = defaultdict(dict)
         
#    def get_all_nodes(self):
#        all_nodes = []
         
#        for node in self.connection_graph.nodes():
#            dendNumber = node.find('p')
#            if dendNumber > -1:
#                all_nodes.append(str(node[0:dendNumber]))
#            else:
#                all_nodes.append(str(node))
                 
#        return all_nodes
     
#    '''This function is designed to read the synapse pairs
#    file and arrange the information in various dictionaries
#    to be read at a later state. 
     
#    Because of some weird error finding strings, it was 
#    necessary to create two dictionaries for the conversion
#    of strings back and forth'''
#    def readFile(self,synapse_file):
#        #Read File
#        synapsePairs = open(synapse_file,"r")
#        self.connection_graph = nx.MultiGraph()
         
#        #Conversion Number - Negative to
#        # be able differentiate from axons
#        conv_number = -1
 
#        all_lines = synapsePairs.read()
 
#        currentLine = 0
#        matching_lines = Neuropil_Util.synapsePattern.findall(all_lines)
#        #separated_data = [Neuropil_Util.numberSplitter.findall(line) for line in matching_lines]
         
#        for line in matching_lines:
#            if not line:
#                break
 
#            # Find dendrite and axon
#            spacePos = line.find("-")+1
#            endString = line.find("\n")
             
#            processName =  line[0:spacePos-1]
#            connectionsNames = line[spacePos:endString].split(",")
             
#            for name in connectionsNames:
                 
#                divisionPos = name.find("_")
#                dendName = name[0:divisionPos]
#                dendAttribute = name[divisionPos+1:]
                 
#                self.connection_graph.add_edge(processName, dendName, weight=1,attribute=dendAttribute)
 
#                if self.synapseConnections.has_key(dendAttribute):
#                    self.synapseConnections[dendAttribute].append(processName)
#                    self.synapseConnections[dendAttribute].append(dendName)
#                    self.synapseConnections[dendAttribute] = set(self.synapseConnections[dendAttribute])
#                else:
#                     self.synapseConnections[dendAttribute] = [processName, dendName]
     
#    def GetSynapseConnections(self,pSynapseName):
#        if self.synapseConnections.has_key(pSynapseName):
#            return self.synapseConnections[pSynapseName]
         
#        return None
             
#    '''
#    Function receive the name of the axons or axon or dendrite or dendrites
#    and return all the dendrites or axons that are connected to it.
#    '''
#    def retrieveNeighboors(self,process_name):
#        dendrites = []
         
#        process_name = Neuropil_Util.IterableVersion(process_name)
             
#        for axon in process_name:
 
#            tempDict = self.connection_graph[axon]
 
#            neighbors = []
             
#            try:
#                for process,info in tempDict.items():
#                    neighbors.append(process+ '_'+ info.values()[0]['attribute'])
#            except nx.NetworkXError as error: 
#                print error.message
#                continue
             
#            dendrites.append(neighbors)
             
#        return dendrites
 
#    def retrieveNodes(self,pAttribute):
#        nodes = []
#        allEdges = self.connection_graph.edges(data=True)
#        for edge in allEdges:
#            if pAttribute in edge[2]['attribute']:
#                nodes.append([edge[0],edge[1]])
#        for axon in pAttribute:
 
#            tempDict = self.connection_graph[axon]
 
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
#        pos = nx.spring_layout(self.connection_graph)
                         
#        # nodes
#        plt.figure(num=None, figsize=(300, 300), dpi=100, facecolor='w', edgecolor='k')
#        nx.draw_networkx_nodes(self.connection_graph,pos,node_size=400)
             
#        # edges
#        nx.draw_networkx_edges(self.connection_graph,pos,width=1.2)
          
#        # labels for the nodes
#        nx.draw_networkx_labels(mg.connection_graph,pos,font_size=13,font_family='sans-serif')
             
#        #plt.savefig('multiGraph.pdf')
#        plt.show()
         
#    def graphProperties(self):
#        #Basic Degrees of graph
#        degree = self.connection_graph.degree(self.connection_graph.nodes())
          
#        #Density of Graph (number possible to present
#        density = nx.density(self.connection_graph)
          
#        #Transitivity (Mean cluster normalized)
#        transitivity = nx.transitivity(self.connection_graph)
          
#        # The eccentricity of a node v is the maximum distance from v to all other nodes in G.
#        #eccentricity = nx.eccentricity(graph)
          
#        #Betweenness Centrality (Fraction of shortest path that pass through node).
#        bet_centrality = nx.betweenness_centrality(self.connection_graph)
          
#        #Closenness Centrality
#        clos_centrality = nx.closeness_centrality(self.connection_graph)
         
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
         
#        print list(nx.all_simple_paths(self.connection_graph, source, target, 7))
         
#        print "After Simple Path"       
#        print "Finding paths .... "
#        print list(nx.all_shortest_paths(self.connection_graph, source, target))
 
#if __name__ == '__main__':
 
#    test = Neuropil_Synapse()
#    test.readFile("all_process_connections.txt")
#    print test.retrieveNeighboors(["a001","a002"])
 
#    for synapse,synapsePair in test.synapseConnections.items():
#        if len(synapsePair) > 2:
#            print synapse,synapsePair
