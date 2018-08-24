# -*- coding: utf-8 -*-
'''
Created on September 4, 2017

@author: dabrunhosa
'''

#from FEniCS_Ex.IProblem import IProblem
#from Equations.Conventions import Components()

from fenics import FunctionSpace,TrialFunction,TestFunction,\
                    Constant,Expression,Function,solve,\
                    inner,grad,dx,DirichletBC,interpolate,\
                    assemble

import time
        

class CableModelWithF():
    
    #########################################
    ####       Constructor                ###
    ######################################### 
    
    #def __init__(self,options=Options(), **kw):
        
    #    # Define the default options
    #    default_options = Options(name = "Cable Model With Font",
    #                              description = "This is the solution for the \
    #                                              following problem:\
    #                                              Problem being solved is: [0,X]X[0,T]\
    #                                              1/k*du/dt - d2u/dx2 + u = f \
    #                                              f = 4*pi2*(e^(-kt))*sin(2*pi*x)\
    #                                              BC: u(0,t) = u(1,t) = 0 \
    #                                              Initial Conditions:\
    #                                              u(x,0) = sin(2*pi*x)\
    #                                              Solution: u = (e^(-kt))*sin(2*pi*x)")
        
    #    # Merge the default options and the user generated options
    #    whole_options = default_options << options
        
    #    super(CableModelWithF,self).__init__(whole_options,**kw) 
    
    ########################################
    ###      Public Functions            ###
    ######################################## 

    def solve(self,**arguments):
        
        t_start = time.clock()
     
        # definig Function space on this mesh using Lagrange 
        #polynoimals of degree 1.
        H = FunctionSpace(self.mesh, "CG", 1)
     
        # Setting up the variational problem
        v = TrialFunction(H)
        w = TestFunction(H)
        
        coeff_dx2= Constant(1)
        coeff_v = Constant(1)
     
        f = Expression("(4*pow(pi,2))*exp(-(1/coeff_v)*t)*sin(2*pi*x[0])",
                   {'coeff_v': coeff_v}, degree=2)
    
        v0 = Expression("sin(2*pi*x[0])", degree=2)
    
        f.t = 0
        
        def boundary(x,on_boundary):
            return on_boundary
    
        bc = DirichletBC(H,v0,boundary)
    
        v1 = interpolate(v0,H)
        dt = self.steps.time

        a = (dt*inner(grad(v), grad(w)) + dt*coeff_v*inner(v,w))*dx 
        L = (f*dt - coeff_v*v1)*w*dx
    
        A = assemble(a)
        v = Function(H)
        
        T = self.domain.time[-1]
        t = dt
    
        # solving the variational problem.
        while t <= T:
            b = assemble(L, tensor=b)
            vo.t = t
            bc.apply(A,b)
            
            solve(A,v.vector(),b)
            t += dt
            
            v1.assign(v)
        
        self.solution.extend(v.vector().array())
        
        return [self.solution,time.clock()-t_start]

print(solve(Diffusion = 1,Reaction = 1))