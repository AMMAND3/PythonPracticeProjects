def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            
            if i == j:
                sum1 += arr[i][j]
            if i+j == len(arr)-1:
                sum2 += arr[i][j]
    return abs(sum1-sum2)
