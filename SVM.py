#import sys
#sys.path.append('C:\Python27\Lib\site-packages')
#import cvxopt

from cvxopt.solvers import qp 
from cvxopt.base import matrix
import numpy, pylab, random, math

#r = qp(matrix(P) , matrix(q) , matrix(G) , matrix(h)) 
#alpha = list(r[’x’])