'''
Took me: 36 min 30 sec for solve_method_1 to work properly, but went through solve_method_2 during process of solving task.
'''

def solve_method_1(input, k):
    '''
    n is length of input data
    Time complexity: O(n*log(n)) since sorting list is most expensive operation
    Space complexity: O(1)
    '''

    input = sorted(input)

    l = 0
    p = len(input) - 1
    
    try:
        while(input[p] >= k):
            p -= 1
    except:
        return False

    while(l!=p):
        if input[l] + input[p] == k:
            return True
        if input[l] + input[p] > k:
            p -= 1
        if input[l] + input[p] < k:
            l += 1

    return False

def solve_method_2(input, k):
    '''
    n is length of input data
    Time complexity: O(n) since there are one loop depending on n, and lookups in sets are O(1)
    Space complexity: O(m), where m is n without duplicates, so there would be O(n) in worst case
    '''

    seen = set(input[:1])
    for elem in input:
        if (k - elem) in seen:
            return True
        seen.add(elem)
    return False

def solve(input, k):
    return solve_method_1(input, k)

if __name__=='__main__':
    input = [10,15,3,7]
    k = 17
    print(solve(input, k))
    