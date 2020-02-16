
def init_objects(config_dict):
    """
    Init required project's objects using defined configuration. Returns an object dict that is added to project object. 
    This method is called  in server load step. 
    Args:
        config_dict: project config dict

    Returns: dict object in way {'<obj_nname>':<object>, ... }

    """
    # only testing purposes
    obj_list = dict()
    obj_list['input_cfg'] = config_dict
    return obj_list

