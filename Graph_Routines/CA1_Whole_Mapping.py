## -*- coding: utf-8 -*-

#from collections import defaultdict

## graph libs
#import networkx as nx

## plot libs
#import matplotlib
#import matplotlib.pyplot as plt
## from mayavi import mlab

## other libs
#import tools
#import math
#import time
#import re
#import numpy as np

## utility libs
#import Neuropil_Util
#import Neuropil_Synapse

####################################
###         UNUSED CODE           ##
####################################
##def return_shaft_nodes(self, thres=None):
##    '''return a subgraph of the nodes believe to comprise the shaft,
##    as well as the longest path subgraph'''
##    l_p_nodes = self.longest_path(self.whole_graph)
##    sub_g_lp = self.whole_graph.subgraph(l_p_nodes)
##    diam_list = self.get_attri_graph_nodes(sub_g_lp, 'diam')
##    diam_mean = np.mean(diam_list)
##    if thres is None:
##        thres = diam_mean
##    else:
##        thres = diam_mean + (np.std(diam_list) * thres)
##    diam_thres_nodes = np.array(sub_g_lp.nodes())[thres < diam_list]
##    sub_g_diam_thres = self.whole_graph.subgraph(diam_thres_nodes)
##    list_sub_g_thres_cp = list(
##        nx.weakly_connected_Components()(sub_g_diam_thres))
##    sel = np.argsort(
##        np.array([len(i) for i in list_sub_g_thres_cp]))[::-1][0]
##    sub_g_shaft = sub_g_lp.subgraph(list_sub_g_thres_cp[sel])
##    return {'shaft': sub_g_shaft, 'lp': sub_g_lp}

##def most_colin_node_w_diam_thres(self, subgraph, thres=None, return_list=False):
##    '''returns an index for the node which is
##    most colinear amongst the nodes with the
##    largest diameters'''
##    # find biggest nodes
##    diam_list = self.get_attri_graph_nodes(subgraph, 'diam')
##    diam_mean = np.mean(diam_list)
##    if thres is None:
##        thres = diam_mean
##    else:
##        thres = diam_mean + (np.std(diam_list) * thres)
##    larg_node_list = np.array(subgraph.nodes())[thres < diam_list]
##    # print('thres ->{}'.format(thres))
##    # test_out = [subgraph.nodes().index(i) for i in larg_node_list]
##    # print(len(larg_node_list))
##    # calculate angle between vectors
##    out = []
##    for i in larg_node_list:
##        out_temp = []
##        for j in larg_node_list:
##            if i != j:
##                out_temp.append(
##                    tools.sse_0_vect_cross_unit_vect(i.coordinates, j.coordinates))
##        out.append(out_temp)
##    x = np.mean(np.array(out), axis=1)
##    if return_list is False:
##        idx = np.argmin(x)
##        # print('idx -> {}'.format(idx))
##        most_coll_node = larg_node_list[idx]
##        # print('idx other -> {}'.format(nodes.index(most_coll_node)))
##        return subgraph.nodes().index(most_coll_node)
##    else:
##        return np.array([subgraph.nodes().index(larg_node_list[i]) for i in np.argsort(x)])

##def get_attri_graph_nodes(self, graph_obj=None, attribute=None):
##    if (graph_obj is None):
##        graph_obj = self.whole_graph
##    return np.array([getattr(i, attribute) for i in graph_obj.nodes()])

##def graphProperties(self):
##    # Basic Degrees of graph
##    degree = self.whole_graph.degree(self.whole_graph.nodes())

##    # Density of Graph (number possible to present
##    density = nx.density(self.whole_graph)

##    # Transitivity (Mean cluster normalized)
##    transitivity = nx.transitivity(self.whole_graph)

##    # The eccentricity of a node v is the maximum distance from v to all other nodes in G.
##    # eccentricity = nx.eccentricity(graph)

##    # Betweenness Centrality (Fraction of shortest path that pass through
##    # node).
##    bet_centrality = nx.betweenness_centrality(self.whole_graph)

##    # Closenness Centrality
##    clos_centrality = nx.closeness_centrality(self.whole_graph)

##    return [degree, density, transitivity, bet_centrality, clos_centrality]

##def calcTransferResistance(self, comp_1, comp_2):
##    all_elements_in_path = nx.shortest_path(self.whole_graph,
##                                            self.dendrite_compartments[
##                                                comp_1],
##                                            self.dendrite_compartments[comp_2])

##    for i in xrange(len(all_elements_in_path) - 1):
##        current_dendrite = all_elements_in_path[i]
##        next_dendrite = all_elements_in_path[i + 1]
##        '''
##        current_part2 = current_dendrite.Part_2
##        next_part2 = next_dendrite.Part_2
##        '''
##        distance_between = np.sqrt(
##            (current_dendrite.coordinates - next_dendrite.coordinates) ** 2)
##        weight_between = self.whole_graph.get_edge_data(
##            current_dendrite, next_dendrite)
##        '''
##        distance_between = math.sqrt(math.pow((current_part2.x - next_part2.x), 2) + math.pow(
##            (current_part2.y - next_part2.y), 2) + math.pow((current_part2.z - next_part2.z), 2))
##        weight_between = self.whole_graph.get_edge_data(
##            current_dendrite, next_dendrite)
##        '''
##        transfer_resistance = weight_between[
##            'weigth'] / (4 * math.pi * distance_between)

##        print "The distance between compartments is: ", distance_between
##        print "The transfer resitance between them is: ", transfer_resistance

##def consistency_check(self):
##    print "Checking for consistency of the data entered......"
##    for node in self.whole_graph.nodes():

##        string_neighbors = ""
##        node_neighboors = nx.neighbors(self.whole_graph, node)

##        for neighbor in node_neighboors:
##            string_neighbors = string_neighbors + " , " + neighbor.name

##        # print node.name + " has "+ string_neighbors + " as neighboors"

##        if len(node_neighboors) > 2:
##            print "WTFFFFF, something wrong in node:" + node.name
##        elif len(node_neighboors) == 2:
##            neighbor_1_number = int(
##                node_neighboors[0].name.partition("_")[2])
##            neighbor_2_number = int(
##                node_neighboors[1].name.partition("_")[2])
##            node_number = int(node.name.partition("_")[2])
##            order_numbers = [
##                node_number, neighbor_1_number, neighbor_2_number]
##            order_numbers.sort()
##            connection_check = (((order_numbers[
##                                0] + 1) == order_numbers[1]) and (order_numbers[1] == (order_numbers[2] - 1)))
##            if not connection_check:
##                print "WTFFFFF, something wrong in the connections of node:" + node.name

##    print "Consistency finished..."

##def longest_path(self, graph_obj=None):
##    '''returns a simple path of maximum length in a given graph'''
##    if graph_obj is None:
##        graph_obj = self.whole_graph
##    dist = {}  # stores [node, distance] pair
##    for node in nx.topological_sort(graph_obj):
##        # pairs of dist,node for all incoming edges
##        pairs = [(dist[v][0] + 1, v) for v in graph_obj.pred[node]]
##        if pairs:
##            dist[node] = max(pairs)
##        else:
##            dist[node] = (0, node)
##    node, (length, _) = max(dist.items(), key=lambda x: x[1])
##    path = []
##    while length > 0:
##        path.append(node)
##        length, node = dist[node]
##    return list(reversed(path ))

#class Part():
#    """
#    The representation of a part of the compartment.
#    Every compartment is composed by two parts.

#    This class has the obrigatory parameters: x,y,z,diam
#    and the optional parameters: surfaceArea,vol.
    
#    Notice that the optional parameters will be assigned 
#    to a default value if the user does not provide
#    a value for them.

#    Example of use: Part(x,y,z,diam,surfaceArea,vol)
#    """

#    def __init__(self, pX, pY, pZ, pDiam, pSurfaceArea=0.0, pVol=0.0):
#        self.coordinates = np.array([pX, pY, pZ])
#        self.diam = float(pDiam)
#        self.surfaceArea = float(pSurfaceArea)
#        self.vol = float(pVol)

#class Compartment():
#    """
#    The representation of a compartment.

#     This class has the obrigatory parameters: [part1,part2], pName
#    and the optional parameters: id,type.
    
#    Notice that the optional parameters will be assigned 
#    to a default value if the user does not provide
#    a value for them.

#    Example of use: Compartment([part1,part2],name,id,type)
#    """

#    def __init__(self, pParts, pName, pId=0, pType='nil'):
#        #put vol, sa, type only in compartment
#        self.parts = np.array(pParts)
#        self.name = str(pName) 
#        self.id = int(pId)
#        self.type = str(pType)
#        self.coordinates = np.mean((pParts[0].coordinates, pParts[1].coordinates), 0)
#        self.vol = np.mean((pParts[0].vol, pParts[1].vol), 0)
#        self.surfaceArea = np.mean((pParts[0].surfaceArea, pParts[1].surfaceArea), 0)
#        self.diam = np.mean((pParts[0].diam, pParts[1].diam), 0)

#class Process():
#    """
#    The representation of a Process.

#     This class has the obrigatory parameters: pCompartments
#     ( a dictionary with key as a compartment number and
#     value as a filled Compartment class), pName
#    and the optional parameters: type.
    
#    Notice that the optional parameters will be assigned 
#    to a default value if the user does not provide
#    a value for them.

#    Example of use: Process([comp1,comp2,..],name,type)
#    """

#    def __init__(self, pName, pType='nil'):
#        self.compartments = []
#        self.name = str(pName) 
#        self.type = str(pType)

#    def AddCompartment(self,pFirstCompartment,pSecondCompartment):
#        if len(self.compartments) != 0:
#            self.compartments.append(pSecondCompartment)
        
#        self.compartments.append(pFirstCompartment)

#class Whole_Mapping():

#    ###################################
#    ##  GLOBAL VARIABLES            ###
#    ###################################

#    whole_processes = None
#    whole_graph = None
#    connectionGraph = None

#    ###################################
#    ##  FUNCTIONS                   ###
#    ###################################

#    def __init__(self):
#        self.connectionGraph = Neuropil_Synapse.Synapse_Mapping()
#        self.connectionGraph.readFile('all_process_connections.txt')
#        self.whole_processes = defaultdict(dict)
#        self.whole_graph = nx.DiGraph()

#    def get_attri_graph_nodes(self, graph_obj=None, attribute=None):
#        if (graph_obj is None):
#            graph_obj = self.whole_graph
#        return np.array([getattr(i, attribute) for i in graph_obj.nodes()])

#    def readFiles(self, process_files): 
#        """
#        Read all files passed and create the graph
#        where each node is a Compartment class.

#        Depends on external package NetworkX

#        Example of use: readFiles([files])
#        """

#        process_files = Neuropil_Util.IterableVersion(process_files)

#        # Get all the numbers in any format (being float or int)
#        numberPattern = "[-+]?[0-9]*\.?[0-9]+(?:e[-+][0-9]+)?"

#        # Compiled version of the Regular Expression above that gets
#        # all the numbers in the file
#        numberSplitter = re.compile(numberPattern)

#        # Get all the numbers divided by commas
#        allNumbersPattern = "(?:" + numberPattern + ",?)"

#        # Compiled version of the Regular Expression above that gets
#        # all the morphology line in the file
#        morphologySplitter = re.compile("(" + numberPattern + "\s*-\s*" + allNumbersPattern + "*)\s*\n?")

#        # Compiled version of the Regular Expression above that gets
#        # all the connection lines in the file
#        connectionSplitter = re.compile(numberPattern + "\(" + numberPattern + "\)\s+?-\s+?" + 
#                        numberPattern + "\(" + numberPattern + "\)")

#        # Create dictionary of all the compartments in the file
#        allCompartments = defaultdict(dict)

#        for file in process_files:
#            # Get Processe Name
#            process_name = Neuropil_Util.GetFileName(file)

#            # Read the file received
#            process_info = open(file, "r")
#            all_lines = process_info.read()

#            currentLine = 0
#            matching_lines = morphologySplitter.findall(all_lines)
#            separated_data = [numberSplitter.findall(line) for line in matching_lines]

#            objectType = Neuropil_Util.GetCompartmentType(file)

#            # Get all the compartments. Notice that each compartment is 
#            # composed by two parts (top and bottom)
#            for currentLine in range(0, len(separated_data) - 1, 2):
#                part1 = Part(
#                    float(separated_data[currentLine][1]), float(
#                        separated_data[currentLine][2]),
#                    float(separated_data[currentLine][3]), float(
#                        separated_data[currentLine][4]),
#                    pSurfaceArea=float(separated_data[currentLine][5]), pVol=float(separated_data[currentLine][6])
#                )
#                part2 = Part(
#                    float(
#                        separated_data[currentLine + 1][1]), float(separated_data[currentLine + 1][2]),
#                    float(
#                        separated_data[currentLine + 1][3]), float(separated_data[currentLine + 1][4]),
#                    pSurfaceArea=float(separated_data[currentLine + 1][5]), pVol=float(separated_data[currentLine + 1][6])
#                )

#                # Add a new Compartment (composed of the above parts) and 
#                # create a key entry (from the that compartment id) 
#                allCompartments[separated_data[currentLine][0]] = Compartment(
#                    [part1, part2], process_name + '_comp' + separated_data[currentLine][0], 
#                    pId=separated_data[currentLine][0],pType=objectType)

#            matching_lines = connectionSplitter.findall(all_lines)
#            separated_data = [numberSplitter.findall(line) for line in matching_lines]
#            connections = []
#            tempProcess = Process(process_name,objectType)

#            # Add all the compartments to the graph using
#            # the connections as a way to determine the 
#            # which compartment is connected to which
#            for line_list in separated_data:
#                self.whole_graph.add_edge(
#                    allCompartments[line_list[0]], allCompartments[line_list[2]], weigth=1.0)
#                connections.append([allCompartments[line_list[0]], allCompartments[line_list[2]]])
#                tempProcess.AddCompartment(allCompartments[line_list[0]],allCompartments[line_list[2]])
            
#            # Prepare dictionary for the next file 
#            if self.whole_processes.has_key(objectType):
#                self.whole_processes[objectType].append(tempProcess)
#            else:
#                self.whole_processes[objectType] = [tempProcess]
#            allCompartments.clear()

#        test = ""

#    def draw_graph3d(graph, graph_colormap='winter', bgcolor = (1, 1, 1),
#                     node_size=0.03,
#                     edge_color=(0.8, 0.8, 0.8), edge_size=0.002,
#                     text_size=0.008, text_color=(0, 0, 0)):

#        H=nx.Graph()

#        # add edges
#        for node, edges in graph.items():
#            for edge, val in edges.items():
#                if val == 1:
#                    H.add_edge(node, edge)

#        G=nx.convert_node_labels_to_integers(H)

#        graph_pos=nx.spring_layout(G, dim=3)

#        # numpy array of x,y,z positions in sorted node order
#        xyz=np.array([graph_pos[v] for v in sorted(G)])

#        # scalar colors
#        scalars=np.array(G.nodes())+5
#        mlab.figure(1, bgcolor=bgcolor)
#        mlab.clf()

#        pts = mlab.points3d(xyz[:,0], xyz[:,1], xyz[:,2],
#                            scalars,
#                            scale_factor=node_size,
#                            scale_mode='none',
#                            colormap=graph_colormap,
#                            resolution=20)

#        for i, (x, y, z) in enumerate(xyz):
#            label = mlab.text(x, y, str(i), z=z,
#                              width=text_size, name=str(i), color=text_color)
#            label.property.shadow = True

#        pts.mlab_source.dataset.lines = np.array(G.edges())
#        tube = mlab.pipeline.tube(pts, tube_radius=edge_size)
#        mlab.pipeline.surface(tube, color=edge_color)

#        mlab.show() # interactive window    

#    def drawGraph(self, graph_obj=None, name_file='graph_out.pdf', 
#                  diff_color_node=None, labels=False,pDisable3D=True):
#        if graph_obj is None:
#            graph_obj = self.whole_graph

#        # plt.figure(num=None, figsize=(150, 150), dpi=50, facecolor='w',
#        # edgecolor='k')
#        plt.figure()

#        # set node sizes
#        max_node_size = 100.0
#        diam_list = self.get_attri_graph_nodes(graph_obj, 'diam')
#        max_diam = max(diam_list)
#        node_size_list = [max_node_size * (i / max_diam) for i in diam_list]

#        # set node colors
#        if diff_color_node is None:
#            node_color = 'r'
#        else:
#            # different node color is a list of nodes
#            node_color = ['r'] * len(graph_obj.nodes())
#            if type(diff_color_node) is nx.classes.digraph.DiGraph:
#                for i in diff_color_node:
#                    node_color[graph_obj.nodes().index(i)] = 'b'
#            elif type(diff_color_node) is list or type(diff_color_node) is np.ndarray:
#                for i in diff_color_node:
#                    node_color[i] = 'b'
#            else:
#                node_color[diff_color_node] = 'b'
#        # nodes
#        # positions for all nodes
#        # pos = nx.spring_layout(graph_obj)

#        if pDisable3D:
#            pos = {}
#            for node in graph_obj.nodes():
#                pos[node] = node.coordinates[:2]

#            nx.draw_networkx_nodes(
#                graph_obj, pos, node_size=node_size_list, node_color=node_color)

#            # edges
#            centrality = nx.degree_centrality(graph_obj)
#            w_l = [int(math.ceil(centrality[node] * 3.0)) for node in centrality]
#            nx.draw_networkx_edges(graph_obj, pos, width=w_l)

#            # labels
#            if labels:
#                dendrite_labels = defaultdict(dict)

#                for node in graph_obj.nodes():
#                    dendrite_labels[node] = node.name

#                nx.draw_networkx_labels(
#                    graph_obj, pos, font_size=10, font_family='sans-serif', labels=dendrite_labels)
#            plt.show()
#            plt.savefig(name_file)
#        else:
#            pos3D = {}
#            for node in graph_obj.nodes():
#                pos3D[node] = node.coordinates
#            # numpy array of x,y,z positions in sorted node order
#            xyz=np.array([pos[v] for v in sorted()])

#            # scalar colors
#            scalars=np.array(G.nodes())+5
#            mlab.figure(1, bgcolor=bgcolor)
#            mlab.clf()

#            pts = mlab.points3d(xyz[:,0], xyz[:,1], xyz[:,2],
#                                scalars,
#                                scale_factor=node_size,
#                                scale_mode='none',
#                                colormap='Blues',
#                                resolution=20)

#            for i, (x, y, z) in enumerate(xyz):
#                label = mlab.text(x, y, str(i), z=z,
#                                  width=text_size, name=str(i), color=text_color)
#                label.property.shadow = True

#            pts.mlab_source.dataset.lines = np.array(G.edges())
#            tube = mlab.pipeline.tube(pts, tube_radius=edge_size)
#            mlab.pipeline.surface(tube, color=edge_color)

#            mlab.show() # interactive window    

    
#    def calculateSynapses(self):             
#        print self.connectionGraph.GetSynapseConnections("sy071")

#if __name__ == '__main__':
#    #Neuropil_Util.OrganizeData() 

#    #allFilesLocation = Neuropil_Util.GetLocation()
#    #allProcesses = Neuropil_Util.GetAllFiles(allFilesLocation,pExtension="skel",pFullPathMode=True,pInFolder=True)
#    dendritePicture = "./InputFiles/Dendrites/d001-dec-imp-fixed.skel"

#    g = Whole_Mapping()
#    g.readFiles(dendritePicture)
#    #g.calculateSynapses() 

#    #shaft_nodes_sub = g.return_shaft_nodes(thres=0.0)
#    #g.draw_graph3d(g.whole_graph)
#    g.drawGraph(graph_obj=g.whole_graph,
#                name_file='whole_shaft_high.pdf')
#    #g.drawGraph(graph_obj=shaft_nodes_sub['shaft'], name_file='shaft.pdf')
#    #g.drawGraph(graph_obj=shaft_nodes_sub['lp'], name_file='lp.pdf')
