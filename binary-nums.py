def recurse_to_binary(
    n, 
    binary_n = [],
    index = 0,
    binary_nums = [128, 64, 32, 16, 8, 4, 2, 1]):

    """recursive version"""

    if n > 255: 
        return None
    
    try:
        if binary_n[7] == 0 or binary_n[7] == 1:
            return binary_n
    
    except:
        num = binary_nums[index]

        if n//num:
            n -= num
            binary_n.append(1)
        else:
            binary_n.append(0)

        index += 1

        return recurse_to_binary(n, binary_n, index)


def iterate_to_binary(n):
    """iterative version"""

    if n > 255:
        return None

    binary_nums = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_n = []

    for num in binary_nums:
        if n//num:
            binary_n.append(1)
            n -= num
        else:
            binary_n.append(0)

    return binary_n


def convert_to_binary(n):
    """long form"""

    if n > 255:
        return None

    binary_n = [0,0,0,0,0,0,0,0]
    
    indice_0 = n//128
    if indice_0:
        binary_n[0] = 1
        n = n - 128
    
    indice_1 = n//64
    if indice_1:
        binary_n[1] = 1
        n = n - 64

    indice_2 = n//32
    if indice_2:
        binary_n[2] = 1
        n = n - 32

    indice_3 = n//16
    if indice_3:
        binary_n[3] = 1
        n = n - 16

    indice_4 = n//8
    if indice_4:
        binary_n[4] = 1
        n = n - 8
    
    indice_5 = n//4
    if indice_5:
        binary_n[5] = 1
        n = n - 4
     
    indice_6 = n//2
    if indice_6:
        binary_n[6] = 1
        n = n - 2
    
    indice_7 = n//1
    if indice_7:
        binary_n[7] = 1
        n = n - 1
    
    return binary_n

n = 78
print(convert_to_binary(n))
print(iterate_to_binary(n))
print(recurse_to_binary(n))