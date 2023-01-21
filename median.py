def median(arr):
  arr.sort()
  mid = len(arr) // 2
  res = (arr[mid] + arr[~mid]) / 2
  return int(res)
