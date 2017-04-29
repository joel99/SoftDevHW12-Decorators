def get_args(args_tuple):
    tuple_in_string_form = str(args_tuple)
    return tuple_in_string_form[1:-1].strip(',')

def get_kwargs(kwargs_dict):
    kwargs_key_value_pairs = ['{0}={1}'.format(key_value_pair[0], key_value_pair[1]) for key_value_pair in kwargs_dict.items()]
    return ','.join(kwargs_key_value_pairs) if kwargs_key_value_pairs else None
    
