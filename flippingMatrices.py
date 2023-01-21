def flippingMatrix(matrix):
    # remember
    #     [0] [1] [2] [3]
    # [0] a    b   b   a        
    # [1] c    d   d   c    
    # [2] c    d   d   c     
    # [3] a    b   b   a
    #
    # so we only have to look at the indexes where it can be flippd as a quadrant,
    # otherwise we would rather look at the sum of all quadrants
    
    n = int(len(matrix)/2)
    maxv = 0
    total = 0
    
    for i in range(0, n):
        for j in range(0, n):
            maxv = -500000
            maxv = max(matrix[i][j], maxv)
            maxv = max(matrix[i][2*n - j - 1], maxv)
            maxv = max(matrix[2*n - i -1][j], maxv)
            maxv = max(matrix[2*n - i - 1][2*n - j - 1], maxv)
            
            total += maxv
            
    return total
