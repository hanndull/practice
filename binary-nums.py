def iterate_from_binary(n):
    """iterate from binary to ascii"""

    list_n = list(str(n))
    binary_nums = from_binary_convert_list(len(list_n)-1)
    ascii_n = 0
    index = 0

    for num in list_n:
        if num == '1':
            ascii_n += binary_nums[index]
        index += 1

    return ascii_n


def recurse_to_binary(n, binary_nums, binary_n = [], index = 0):
    """recursive version to find binary of ASCII decimal number
    Use to_binary_convert_list fn for binary_nums parameter
    """

    try:
        num = binary_nums[index]

        if n//num:
            n -= num
            binary_n.append(1)
        else:
            binary_n.append(0)

        index += 1

        return recurse_to_binary(n, binary_nums, binary_n, index)
    
    except:
        return int(stringify_list(binary_n))


def iterate_to_binary(n):
    """iterative version"""

    binary_nums = to_binary_convert_list(n)
    binary_n = []

    for num in binary_nums:
        if n//num:
            binary_n.append(1)
            n -= num
        else:
            binary_n.append(0)

    return stringify_list(binary_n)


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
    
    return int(stringify_list(binary_n))


def stringify_list(a_list):
    """helper function to turn results into str"""

    string = ""
    for char in a_list:
        string += str(char)

    return string

def to_binary_convert_list(n):
    """helper function to create binary conversion list as long as needed
    n = the total sum of the ascii code value
    """

    conversion_list = []
    conversion_value = 1

    while conversion_value <= n:
        conversion_list.insert(0, conversion_value)
        conversion_value *= 2

    return conversion_list


def from_binary_convert_list(n):
    """helper function to create binary conversion list as long as needed
    n = length of stringified/listified binary number
    """

    conversion_list = []
    conversion_value = 1
    index = 0

    while index <= n:
        conversion_list.insert(0, conversion_value)
        conversion_value *= 2
        index += 1

    return conversion_list


n = int(input('What decimal number would you like to convert to binary? >> '))
print(recurse_to_binary(n, binary_nums=to_binary_convert_list(n)))

x = int(input('What binary number would you like to convert to decimal? >> '))
print(iterate_from_binary(x))
