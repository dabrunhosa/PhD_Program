# -*- coding: utf-8 -*-
'''
Created on September 1, 2017

@author: dabrunhosa
'''

from Analytics.FEniCS_Ex.IProblem import IProblem
from fenics import FunctionSpace,TrialFunction,TestFunction,\
                    Constant,Expression,Function,solve,\
                    inner,grad,dx

import time
from Utilities.DataEntry import Options
from NeuroCore.Equations.Conventions import Components

'''
This is the solution for the following problem:
    Problem being solved is: [0,X]
    epsilon*d2u/dx2 + u = f
    f =  (1 - epsilon*4*(pi^2))*sin(2*pi*x)
    
    BC:
        du/dx(0) = du/dx(1) = 0
        
    Solution:
        u = sin(2*pi*x)
'''
class CableModelWithF(IProblem):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "Cable Model With Font",
                                  description = "This is the solution for the \
                                                  following problem:\
                                                  Problem being solved is: [0,X]\
                                                  epsilon*d2u/dx2 + u = f \
                                                  f =  (1 - epsilon*4*(pi^2))*sin(2*pi*x)\
                                                  BC: du/dx(0) = du/dx(1) = 0 \
                                                  Solution: u = sin(2*pi*x)")
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(CableModelWithF,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
    
    
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
     
        epsilon = Constant(arguments[Components().Diffusion])
        f = Expression("(1 - epsilon*4*pow(pi,2))*cos(2*pi*x[0])",\
                       epsilon=epsilon, degree=1)
     
        a = (epsilon*inner(grad(v), grad(w)) + inner(v,w))*dx 
        L = f*w*dx
     
        # solving the variational problem.
        v = Function(H)
        solve( a == L, v)
        
        self.solution.extend(v.vector().array())
        
        return [self.solution,time.clock()-t_start]

'''
This is the solution for the following problem:
    Problem being solved is: [0,X]
    - epsilon*d2u/dx2 + u = 0
    
    BC:
        du/dx(0) = u0
        du/dx(1) = u1
        
    Solution:
        u = alpha*sinh(lambda*x) + beta*cosh(lambda*x)
        alpha = u0/lambda
        beta = u1 - u0*cosh(lambda)/lambda*sinh(lambda)
        lambda = 1/sqrt(epsilon)
'''
class CableModel(IProblem):
    
    ########################################
    ###       Constructor                ###
    ######################################## 
    
    def __init__(self,options=Options(), defaultOptions = Options(), **kw):
        
        # Define the default options
        inDefaultOptions =Options(name = "Cable Model",
                                  description = "This is the solution for the following problem:\
                                  Problem being solved is: [0,X] \
                                  - epsilon*d2u/dx2 + u = 0 \
                                  BC:\
                                  du/dx(0) = u\
                                  du/dx(1) = u1\
                                  Solution:\
                                  u = alpha*sinh(lambda*x) + beta*cosh(lambda*x)\
                                  alpha = u0/lambda\
                                  beta = u1 - u0*cosh(lambda)/lambda*sinh(lambda)\
                                  lambda = 1/sqrt(epsilon)")
        
        # Merge the default options and the user generated options
        defaultOptions = inDefaultOptions << defaultOptions
        
        super(CableModel,self).__init__(options=options, defaultOptions = defaultOptions, **kw)
    
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
     
        epsilon = Constant(arguments[Components().Diffusion])
        f = Constant(0)
     
        a = (epsilon*inner(grad(v), grad(w)) + inner(v,w))*dx 
        #Still have to figure it how to use a Neumann Condition here
        L = f*w*dx
     
        # solving the variational problem.
        v = Function(H)
        solve( a == L, v)
        
        self.solution.extend(v.vector().array())
        
        return [self.solution,time.clock()-t_start]

