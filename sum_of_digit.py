# Python program to
# compute sum of digits in
# number.

# Function to get sum of digits


def digSum(n):

	if (n == 0):
		return 0
	if (n % 9 == 0):
		return 9
	else:
		return (n % 9)

# Driver program to test the above function
n = 1357
print(digSum(n))



# This code is contributed by
# Smitha Dinesh Semwal






