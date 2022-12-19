# Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and
#  they spend all of their money. iven a list of prices for the flavors of ice cream, select the two that will cost 
#  all of the money they have.

def icecreamParlor(m, arr):
    # Write your code here
    n = len(arr)
    result = []
    
    for i in range(n-1, 0, -1):
        if arr[i] < m:
            for j in range(i):
                temp = arr[i] + arr[j]
                if temp == m:
                    result = [j+1, i+1]
                    break
     
    return sorted(result)