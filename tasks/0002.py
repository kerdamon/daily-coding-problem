'''
Took me: 31 min 30 sec for solve_1 using dynamical programming
'''

import time

def solve_1(input): # divine and conquer, dynamical programming
    '''
    n is length of input data
    Time complexity: O(n)
    Space complexity: O(n)
    '''

    mul_tab_l = [0 for i in range(len(input))] # value under each index i is value for sum of elements from beggining of array to index i
    mul_tab_r = [0 for i in range(len(input))] # value under each index i is value for sum of elements from index i to end of array

    mul_tab_l[0] = input[0]
    for index, val in enumerate(input[1:], start=1):
        mul_tab_l[index] = val * mul_tab_l[index-1]

    mul_tab_r[len(input) - 1] = input[len(input) - 1]
    for index in reversed(range(len(input)-1)):
        mul_tab_r[index] = input[index] * mul_tab_r[index+1]

    product_array = [0 for i in range(len(input))]
    product_array[0] = mul_tab_r[1]
    product_array[len(input)-1] = mul_tab_l[len(input)-2]
    for index in range(1, len(input) - 1):
        product_array[index] = mul_tab_l[index-1] * mul_tab_r[index+1]

    return product_array

def solve_2(input): # using division
    product = 1
    for elem in input:
        product *= elem
    
    product_array = []
    for elem in input:
        product_array.append(product//elem)

    return product_array

def solve(input):
    return solve_2(input)

def test(input):
    if solve_1(input) == solve_2(input):
        print(f'OK All methods are returning the same results')
    else:
        print(f'Wrong No all methods are returning the same results')

if __name__=='__main__':
    input = [1,2,3,4,5]
    print(solve(input))
    # test(input)
    # start_1 = time.time()
    # solve_1(input)
    # stop_1 = time.time()
    # print(f'Time to execute method 1: {stop_1 - start_1}')
    # start_2 = time.time()
    # solve_2(input)
    # stop_2 = time.time()
    # print(f'Time to execute method 2: {stop_2 - start_2}')