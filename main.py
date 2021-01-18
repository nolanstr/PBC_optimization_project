from functions.objective import objective

from scipy import optimize
import numpy as np

x_0 = np.array([10., 0.1])
mk = {'method':'Nelder-Mead'}


op_values = optimize.basinhopping(objective, x_0, minimizer_kwargs=mk, 
                                    niter=500)
import pdb;pdb.set_trace()
