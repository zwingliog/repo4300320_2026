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
              figsize = None, alpha = 0.1, ylimL = None,
              SHOW = True, DEVOLVE_fig_axs = False ):
  if figsize is not None:
    fig = plt.figure(figsize=figsize)
  else:
    fig = plt.figure()
  axs = []
  axs.append( plt.subplot(3,1,(1,2)) )
  plt.subplots_adjust(hspace=0.0)
  plt.plot( As, X.T, ',k', alpha=alpha )
  plt.xlabel( 'a' )
  plt.ylabel( 'x' )
  axs.append( plt.subplot(3,1,3) )
  axs[1].sharex(axs[0])
  plt.plot( As, 0*As, '-r', lw=0.5 )
  plt.plot( As, L, ',b' )
  plt.xlabel( 'a' )
  plt.ylabel( 'L' )
  plt.xlim([min(As), max(As)])
  if ylimL is not None:
    plt.ylim(ylimL)
  if SHOW:
    plt.show()
  if DEVOLVE_fig_axs:
    return fig, axs
#

def contadorPeriodo( X, delta=1e-5, pMax=np.inf, nVerMin=0 ):
  if X.ndim==1:
    X = np.atleast_2d(X).T
  Ps = []
  for x in X.T:
    repetidos = np.nonzero( abs(x-x[0])<delta )[0]
    p = 0
    if len(repetidos)>1: # o x contem o x[0]
      pi = np.diff(repetidos)
      if ( max(pi)==min(pi) ) and ( pi[0]<=np.min((pMax,(len(x)-nVerMin))) ):
        p = pi[0]
        for i in range(p):
          if max( abs(x[i::p]-x[i]) )>delta:
            p = 0
            break
    Ps.append( p )
  return np.asarray(Ps)
#
