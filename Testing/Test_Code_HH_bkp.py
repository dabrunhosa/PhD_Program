#'''
#Created on 21/07/2014

#@author: dabrunhosa
#'''

#from Segments import Segment
#from Utils import Options
#from GeoMeshes import Geometric_Mesh
#from CompMeshes import Computational_Mesh
#from Models import HH_Model
#from Approximations import Galerkin_Approximation
#from ODESolver import BackwardEuler

#from Conditions import Neumann

#import numpy
#import math
#import time

#domain_length = 1.0
#delta_x = 0.1
#delta_t = 0.1


#spatial_elements = numpy.arange(0, domain_length + delta_x, delta_x)
 
#V_0 = []

#def initial_values(x):
#    return -65.0

#for x in spatial_elements:
#    V_0.append(initial_values(x))
 
#V_0 = numpy.transpose(V_0)

#neuro_options = Options(domain_length=domain_length,delta_x = delta_x,initial_state=V_0,diameter=f)
#segment0 = Segment('Axon0',neuro_options)
## segment01 = Segment('Axon01',neuro_options)
## segment00 = Segment('Axon00',neuro_options)
## segment_0 = Segment('Axon -0',neuro_options)
## segment_1 = Segment('Axon -1',neuro_options)

#geoMesh = Geometric_Mesh()

#geoMesh.insert_segments(segment0)
##  geoMesh.insert_segments(segment00)
##  geoMesh.insert_segments(segment01)
##  geoMesh.insert_segments(segment_0)
##  geoMesh.insert_segments(segment_1)
##    
##  geoMesh.connect_segments(segment0, segment01)
##  geoMesh.connect_segments(segment0, segment00)
##    
##  geoMesh.connect_segments(segment_0, segment0)
##  geoMesh.connect_segments(segment_1, segment0)
##    
## geoMesh.draw_neuroscience_mesh()

#cm = 1
 
#compMesh = Computational_Mesh(geometric_mesh=geoMesh)
#approximation = Galerkin_Approximation(delta_x=delta_x)
#ode_approximation = BackwardEuler(delta_t=delta_t,coeff_t=cm)

#def model_function(x,t):
#    return 4*(math.pi**2)*math.exp(-t)*math.sin(2*math.pi*x)

#a = 238
#rl = 35.4

## coeff_dx_2 = -a/(2*rl)
#coeff_dx_2 = -1
## Ermentrout Parameters
#conductance_gk = 36
#conductance_gNa = 120
#conductance_gLeaky = 0.3

#final_time = 30.0

#print coeff_dx_2

## # Abbot Parameters
## conductance_gk = 0.36
## conductance_gNa = 1.2
## conductance_gLeaky = 0.003

#def font(x,t):
#    return 10


#cable_model = HH_Model(coeff_dx2=coeff_dx_2,conductance_gk=conductance_gk,conductance_gNa=conductance_gNa,
#                       conductance_gLeaky=conductance_gLeaky,pde_approximation=approximation,
#                       pde_time_approximation=ode_approximation,ode_approximation=ode_approximation)

#compMesh.create_region(cable_model)

##Identify all the boundary conditions and return a list with
##default values and types
#boundary_conditions = compMesh.identify_boundary_conditions()

##Set the boundary conditions to the desired type and
##value

#boundary_conditions.set(0,Neumann(0))
#boundary_conditions.set(1,Neumann(0))

#t_start = time.clock() 
#compMesh.solve(boundary_conditions, delta_t=delta_t, final_time=final_time)
#print time.clock()-t_start  
    

