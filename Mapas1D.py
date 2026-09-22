import numpy as np
import matplotlib.pyplot as plt
from repo4300320_2026.Mapas2026 import contadorPeriodo

def mapas1D(x0, a, funMapa=lambda x,a:a*x*(1-x), n=1, nT=0):
  x = x0
  X = []
  for i in range(-nT,n):
    x = funMapa(x,a)
    if i >= 0:
      X.append(x)
  return np.asarray(X)
#

def LyapunovMapas1D( X, As, funMapa = lambda x,a : a*x*(1-x), \
                    xMax=1, delX=1e-9, fPrimeMinimo=1e-10, Ps=None ):
  As = np.atleast_1d(As)
  if X.ndim==1:
    Xs = np.atleast_2d(X.T)
  else:
    Xs = X.copy()
  if Ps is None:
    Ps = contadorPeriodo( Xs, nVerMin=10 )
  Ls = []
  for x, a, p in zip(Xs.T, As, Ps):
    if p>1 and (len(x) % p)>0:
      x = x[:-int(len(x) % p)]
    x0 = x
    f = funMapa(x0,a)
    x0plus = x0+delX
    x0plus[x0plus>xMax] = x0[x0plus>xMax]-delX
    fplus = funMapa(x0plus,a)
    fPrime = np.maximum( np.abs(fplus-f)/np.abs(x0plus-x0), fPrimeMinimo )
    Ls.append( np.mean( np.log(fPrime) ) )
  return np.array(Ls)
#