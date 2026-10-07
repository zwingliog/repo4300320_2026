import numpy as np

def fun_Lorenz( t, r, rho=28, sigma=10, Beta=8/3 ):
  x, y, z = r
  dxdt = sigma*(y-x)
  dydt = x*(rho-z) - y
  dzdt = x*y - Beta*z
  return np.array( [dxdt, dydt, dzdt] )
#

def jac_Lorenz( t, r, rho=28, sigma=10, Beta=8/3 ):
  x, y, z = r
  dxpdxyz = [ -sigma, sigma, 0 ]
  dypdxyz = [ (rho-z), -1, x ]
  dzpdxyz = [ y, x, -Beta ]
  return np.array( [dxpdxyz, dypdxyz, dzpdxyz] )
#

