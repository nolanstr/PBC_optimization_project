import numpy as np
import sys
sys.path.append('~/Documents/PBC/PBC_optimzation_project/functions')
from scipy import optimize

from check_volume import check_volume
from compute_cost import compute_cost

def objective(params):
    '''
    used to compute the cost of any combination of base and height params
    '''
    check = check_volume(params)
    if check == True:
        return compute_cost(params)
    else:
        return np.inf


x_0 = np.array([10., 0.1])
mk = {'method':'Nelder-Mead'}


op_values = optimize.basinhopping(objective, x_0, minimizer_kwargs=mk, 
                                    niter=500)
import pdb;pdb.set_trace()
