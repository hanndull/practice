def flatten_array(a_list, flattened_list = []):
    """Take in a list, and flatten nested contents into one list"""

    # [[0],1,[[2],3]] --> [0,1,2,3]

    for item in a_list:

        if type(item) != list:
            flattened_list.append(item)

        else: 
            flatten_array(item, flattened_list)

    return flattened_list


assert flatten_array([[0, [1, 2, 3]], [0], 1, [[2], 3]]) == [0,1,2,3,0,1,2,3]
