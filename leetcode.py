def twoSum( nums, target):
        map1 = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map1:
                return [map1[complement], i]
            map1[nums[i]] = i
            print(map1)
        
        return [-1, -1]
    

#print(twoSum([2,3,5,13,11,15,4, 7,75], 90))


def maxProfit(prices):
    
        min_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
            
        return max_profit

#print(maxProfit([7,1,5,3,6,4]))

# 238. Product of Array Except Self
# Medium
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    
    n = len(nums)

    left_product = [1]*n
    right_product = [1]*n
    answer= [1]*n

    for i in range(1, n):
        left_product[i] = left_product[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * nums[i+1]
    for i in range(0, n):
        answer[i] = left_product[i] * right_product[i]
    return answer  
    
# 53. Maximum Subarray
# Medium
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def maxProduct(nums):
        
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr_num = nums[i]
        tmp_max = max_product
        max_product = max(curr_num * tmp_max, curr_num * min_product, curr_num)
        min_product = min(curr_num * tmp_max, curr_num * min_product, curr_num)
        result = max(result, max_product)
        
    return result
    
    
def climbStairs( n):
    if n <= 2:
        return n

    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def fib1(num, dicts):
        if num <= 1:
            return num
        if num not in dicts:
            dicts[num]= fib1(num-1, dicts) + fib1(num-2, dicts)
        return dicts[num]
        
# dic = {}
# fib1(n, dic)
        
def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy any remaining elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
        
def subsetA(arr):
    # Write your code here
    
    #first we can sort array
    arr.sort(reverse=True)
    A = []
    sumA, sumRemain = 0, sum(arr)
    
    for num in arr:
        A.append(num)
        sumA += num
        sumRemain -= num
        
        if sumA > sumRemain:
            break
    return sorted(A)

def getNumber(binary):
    # Write your code here
    condition = False
    i = []
    
    while condition == False:
        if(binary.next == None):
            condition = True
        i.append(binary.data)
        binary = binary.next
    
    binary_num = 0
    count = 0
    for j in range(len(i)-1, -1, -1):
        if i[j] == 1:
            binary_num += 2**(count)
        count += 1
    return binary_num

# pali = ""

def isPalindrome(s):
    
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[len(s)-1]:
        return isPalindrome(s[1:len(s)-1])
    return False

# print(isPalindrome(pali))

def getBinary(num, result):
    
    if (num == 0):
        return result
    result = str(num%2) + result
    return getBinary(num//2, result)

# print(getBinary(10, ""))

def sumNatural(n):
    if n == 1:
        return 1
    return n + sumNatural(n-1)

# print(sumNatural(5))
# l=[0,1,2]
# print( l[0:2])
def binarySearch(ls, left, right, x):
    
    if left > right:
        return -1
    
    mid = (left+right)//2
    
    if x == ls[mid]:
        return mid
    
    if ls[mid] > x:
        return binarySearch(ls, left, mid-1, x)
    
    return binarySearch(ls, mid+1, right, x)

# print(binarySearch([1,2,3,5,8,9,10,11,15], 0, 8, 10))

dicfib = {}

def fibona(n):
    
    if n in dicfib:
        return dicfib[n]
    if n == 0 or n == 1:
        return n
    
    dicfib[n] = fibona(n-1) + fibona(n-2)
    
    return dicfib[n]

# print(fibona(100))

def mergeSort(arr):
    
    if len(arr) >= 2:
        
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        # counters for left position, right poition and updated array
        i, j, k =0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+= 1
            else:
                arr[k] = right_arr[j]
                j += 1
                
            k += 1
            
        while i <len(left_arr):
            arr[k] = left_arr[i]
            i+= 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            

# a = [55, 22, 44, 99, 77, 88, 100, 33]
# mergeSort(a)
# print(a)

def mergeSortedArray(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy any remaining elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
        
def dfsSearch(nodes, source):
    
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for node in nodes[current]:
            stack.append(node)
            
def anotherDfsSearch(nodes, source):
    
    print(source)
    for node in nodes[source]:
        anotherDfsSearch(nodes, node)
    

nodes = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e":[],
    "f":[]
}

# dfsSearch(nodes, "a")
# anotherDfsSearch(nodes, "a")

# def bfsSearch(nodes, source):
    
