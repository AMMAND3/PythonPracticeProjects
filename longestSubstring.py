# Python3 program to find the find the Longest continuous
# sequence of '0' after repeating Given K time

# Function to find the longest subof 0's
def longest_substring(s, k):
	# To store size of the string
	n = len(s)

	if(k>1):
		s += s
		n *= 2

	# To store the required answer
	ans = 0

	# Find the longest subof 0's
	i = 0
	while (i < n):
		x = 0

		# Run a loop upto s[i] is zero
		while (i < n and s[i] == '0'):
			x,i=x+1, i+1
		ans = max(ans, x)
		i+=1

	# Check the conditions
	if(k==1 or ans!=n):
		return ans

	else:
		return (ans//2)*k


# Driver code

s = "010001000"

k = 4

# Function call
print(longest_substring(s, k))

