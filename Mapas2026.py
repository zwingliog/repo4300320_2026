import numpy as np

def mapaLogistico(x0, a, n=1, nT=0):
  x = x0
  X = []
  for i in range(-nT,n):
    x = a*x*(1-x)
    if i >= 0:
      X.append(x)
  return np.asarray(X)
#

def LyapunovLogistico( X, a, fPrimeMinimo=1e-10 ):
  L = np.zeros_like(a)
  for x in X:
    fPrime = np.maximum( np.abs(a*(1-2*x)), fPrimeMinimo )
    L += np.log(fPrime)
  return L/X.shape[0]
#

