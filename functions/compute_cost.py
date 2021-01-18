from .data_grabber import get_costs


def compute_cost(params):
    '''
    base -> Length in units m
    height -> length in units m
    base_cost -> in units of $/m^2
    side_cost -> in units of $/m^2

    Function returns cost of box given material cost and units.
    '''
    strings = ['material_a.csv',
                'material_b.csv']
    costs = get_costs(strings)
    base_cost = costs[0]
    side_cost = costs[1]

    return (params[0]**2*(base_cost)) + (params[0]*params[1]*(side_cost))
