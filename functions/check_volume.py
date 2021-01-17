def check_volume(params, volumes=[8., 10.]):
    
    assert volumes[0] < volumes[1]

    volume = (params[0] ** 2) * params[1]
    
    if volume>=volumes[0] and volume<=volumes[1] and params[0]*params[1]>0:
        return True
    else:
        return False
