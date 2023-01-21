def findZigZagSequence(a, n):
    # first we sort
    # [1, 2, 3, 4, 5]
    a.sort()
    
    # we get the midpoint and switch the last element with midpoint
    # [1, 2, 5, 4, 3]
    mid = int(n/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    # here it is already zigzaf
    # but in case it isn't, we look at midpoint(+1 becaus 0 indexed)
    # and the last position to check(not the last element because largest is fixed properly, plus 0 indexing)
    st = mid + 1
    ed = n - 2
    
    # now just switch from left to right
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    # unnecessary printing statements
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
