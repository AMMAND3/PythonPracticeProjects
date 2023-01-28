for i in range(inputNum):

		num = i + 1

		if (num % 3 == 0 )and (num % 5 == 0):
			print("FizzBuzz")

		elif (num % 3 == 0 )and (num % 5 != 0):
			print("Fizz")

		elif (num % 3 != 0 )and (num % 5 == 0):
			print("Buzz")

		elif (num % 3 != 0 )and (num % 5 != 0):
			print(num)
