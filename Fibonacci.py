def fibonacci(number, last_number):
	"""Create the fibonacci sequence"""

	#Initialie the variables
	first_number = number 		#The first number in the sequence
	second_number = first_number + 1 	#The second number in the sequence
	number_list.append(first_number)


	#Ensure the user inputs a valid number
	if number >= 0 and last_number >= 0:
		#A loop to create the fibonacci sequence
		while (number <= last_number):
			number = first_number + second_number	#Sumation of the two numbers
			first_number = second_number	
			second_number = number

			number_list.append(first_number)	#Add the numbers created to the array
	
		#Output of the fibonacci sequence
		print("\nThis is the fibonacci sequence \n" + str(number_list))

		check_number(int(input("\nEnter the number to be checked\n")))	
	else:
		print("Invalid input")


	

def check_number(number2):
	"""Check the user's number if it's in the fibonacci sequence"""
	
	#Check if the user's input is correct
	if number2 < 0:
		print("Invalid input")

	#If input is correct check if the number is the fibonacci sequence
	if number2 in number_list:
		print("\nThe number is in the fibonacci sequence")
	else:
		print("\nThe number is not in the fibonacci sequence\n")


number_list=[]
fibonacci(int(input("Enter the first number in the sequence\n ")), int(input("Enter the last_number in the sequence\n ")))		
			
