import numpy as np
from scipy import stats

def get_costs(strings):
    
    costs = []
    
    for string in strings:
        
        data = np.genfromtxt(string, delimiter=',')
        slope, _, _, _, _ = stats.linregress(data[0], data[1])
        
        costs.append(slope)
    
    return costs
