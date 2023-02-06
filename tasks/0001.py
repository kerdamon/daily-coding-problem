def solve(input, k):
    input = sorted(input)

    l = 0
    p = len(input) - 1
    
    try:
        while(input[p] >= k):
            p -= 1
    except:
        return False

    while(l!=p):
        print(f'l={l} p={p}')
        if input[l] + input[p] == k:
            return True
        if input[l] + input[p] > k:
            p -= 1
        if input[l] + input[p] < k:
            l += 1

    return False

if __name__=='__main__':
    input = [10,15,3,7]
    k = 17
    # corner cases: two numbers the same
    print(solve(input, k))
    