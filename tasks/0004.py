'''
Took me: 1h 10min to come up close (solution_2), but I was stuck. I read the answer and then coded solution_3
'''

def solution_3(input):
    '''
    n is length of input data
    Time complexity: O(n)
    Space complexity: O(1)
    '''

    n = len(input)
    for i, _ in enumerate(input):
        while input[i] > 0 and input[i] <= n and input[i]-1 != i:
            index = input[i]-1
            input[i], input[index] = input[index], input[i]

    for i,e in enumerate(input):
        if e != i+1:
            return i+1
        
    return n+1

def solution_2(input):
    '''
    n is length of input data
    Time complexity: O(n)
    Space complexity: O(1)
    Not working, because solution is not checking all numbers. During swapping can swap good number to already checked range.
    '''
    n = len(input)
    for i, e in enumerate(input):
        if e > 0 and e <= n:
            temp = input[e-1]
            input[e-1] = e
            input[i] = temp


    for i,e in enumerate(input):
        if e != i+1:
            return i+1
        
    return n+1


def solution_1(input):
    '''
    n is length of input data
    Time complexity: O(n)
    Space complexity: O(n)
    '''

    n = len(input)
    places = [0 for i in range(n)]
    for i in input:
        if i > 0 and i <= n:
            places[i-1] = 1
    
    for i, e in enumerate(places, 1):
        if e == 0:
            return i
    
    return n + 1

if __name__=='__main__':
    input = [1,2,0]
    print(solution_3(input))
