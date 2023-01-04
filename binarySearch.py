def binarySearch(sequence, item):
  index_start = 0
  index_end = len(sequence) - 1
  
  while index_start <= index_end:
    midpoint = index_start + (index_end - index_start) // 2
    midpoint_value = sequence[midpoint]
    
    if midpoint_value == item:
      return midpoint
    elif midpoint_value > item:
      index_end = midpoint - 1
    else:
      index_start = midpoint + 1
      
  return None

seq = [1,3,7,119,120,150,400]

print(binarySearch(seq, 119))
  
  
