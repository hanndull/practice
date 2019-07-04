# write fn that takes n and returns nth fibonnaci num

# 3 --> 1

# 0
# 1
# 1
# 2
# 3
# 5

def find_fibonacci_value(n):
    fib_dict = {0:0,
                1:1,
                }
    
    for num in range(0,n+1):
        if num not in fib_dict:
            value = fib_dict[num-1] + fib_dict[num-2]
            fib_dict[num] = value

    return fib_dict[n]


assert find_fibonacci_value(5) == 5
assert find_fibonacci_value(3) == 2


def find_fibonacci_recursively(n, counter=2, fib_dict={0:0,1:1}):

    if n in fib_dict:
        return fib_dict[n]

    fib_dict[counter] = fib_dict[counter-1] + fib_dict[counter-2]
    counter+=1

    return find_fibonacci_recursively(n, counter, fib_dict)



assert find_fibonacci_recursively(5) == 5
assert find_fibonacci_recursively(3) == 2

# k-binacci -- k as another variable parameter (how many nums to add)