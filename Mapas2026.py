import numpy as np
import matplotlib.pyplot as plt

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

def FazFiguraDiagramaBifurcacao( As, X, L, \
              figsize=(9,4.1), alpha=0.1, ylimL=[-5, 1],
              SHOW=True ):
  plt.figure(figsize=figsize)
  ax = plt.subplot(3,1,(1,2))
  plt.subplots_adjust(hspace=0.0)
  plt.plot( As, X.T, ',k', alpha=alpha )
  plt.xlabel( 'a' )
  plt.ylabel( 'x' )
  ax2 = plt.subplot(3,1,3)
  ax2.sharex(ax)
  plt.plot( As, 0*As, '-r', lw=0.5 )
  plt.plot( As, L, ',b' )
  plt.xlabel( 'a' )
  plt.ylabel( 'L' )
  plt.xlim([min(As), max(As)])
  plt.ylim(ylimL)
  if SHOW:
    plt.show()
#
