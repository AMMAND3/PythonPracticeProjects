def flippingMatrix(matrix):
    # Write your code here
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
