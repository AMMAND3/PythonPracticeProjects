def insertion_sort(sequence):
  for i in range(1, len(sequence)):
    value_to_sort = sequence[i]
    
    while sequence[i-1] > value_to_sort and i >0:
      sequence[i-1], sequence[i] = sequence[i], sequence[i-1]
      i = i - 1
      
  return sequence

seq = [1,4,3,6,2,3,4,5,2,9,8,5]
print(insertion_sort(seq))

# O(n) best case and O(n^2) worst case
