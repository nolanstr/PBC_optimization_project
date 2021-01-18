import numpy as np
import sys
sys.path.append('~/Documents/PBC/PBC_optimzation_project/functions')
from scipy import optimize
from scipy import stats

class box:

    def __init__(self, strings):
        
        self.volumes = [8., 10.]
        self._get_costs(strings)

    def _get_costs(self, strings):
        
        self.costs = []
        
        for string in strings:
            
            data = np.genfromtxt(string, delimiter=',')
            slope, _, _, _, _ = stats.linregress(data[0], data[1])
            
            self.costs.append(slope)

    def _check_volume(self):
        
        assert self.volumes[0] < self.volumes[1]

        self.volume = (self.params[0] ** 2) * self.params[1]
        
        if self.volume >= self.volumes[0] and \
                self.volume <= self.volumes[1] and \
                self.params[0] * self.params[1] > 0:
            
            self.check = True
        else:
            self.check = False


    def _compute_cost(self):
        '''
        base -> Length in units m
        height -> length in units m
        base_cost -> in units of $/m^2
        side_cost -> in units of $/m^2

        Function returns cost of box given material cost and units.
        '''
        
        cost = (self.params[0]**2*(self.costs[0])) + \
                    (self.params[0]*self.params[1]*(self.costs[1]))
        return cost

    def objective(self, params):
        '''
        used to compute the cost of any combination of base and height params
        '''
        self.params = params

        self._check_volume()
        
        if self.check == True:
            return self._compute_cost()
        else:
            return np.inf
    
    def optimize(self, x_0=np.array([10., 0.1]), niter=1000):

        mk = {'method':'Nelder-Mead'}

        self.op_vals = optimize.basinhopping(self.objective, x_0, 
                                        minimizer_kwargs=mk, niter=niter)

