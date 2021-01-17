def compute_cost(params, base_cost=37.8, side_cost=5.75):
    '''
    base -> Length in units m
    height -> length in units m
    base_cost -> in units of $/m^2
    side_cost -> in units of $/m^2

    Function returns cost of box given material cost and units.
    '''
    
    return (params[0]**2*(base_cost)) + (params[0]*params[1]*(side_cost))
