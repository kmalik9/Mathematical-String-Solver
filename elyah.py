# Performs the computation based on the operands and operator
def compute(x, y, op): 
	
	if op == '+':
		return x + y 
	if op == '-':
		return x - y 
	if op == '*':
		return x * y 
	if op == '/':
		return x / y

# Using PEMDAS priority rules, sets a priority value for the type of computation
def priority(op): 
	
	# Priority for addition/subtraction is lower that that of multiplication/division
	if op == '+' or op == '-': 
		return 1
	if op == '*' or op == '/': 
		return 2

# Takes in a string representation of a mathematical expression and solves the answer
def solve(expression): 
	
	# Create two separate stacks for the operands and operations 
	operands = []  
	operations = []

	# Index variable to traverse string 
	i = 0

	# Remove all whitespace from the string before solving expression
	expression = expression.replace(" ","")
	
	while i < len(expression):
		
		
		# If current element is an open parenthesis, push to operations stack 
		if expression[i] == '(': 
			operations.append(expression[i])
		
		# If current element is a positive number, push to operands stack  
		elif expression[i].isdigit():
			# Integer value
			val = 0

			# Decimal Value
			dec = 0

			# Counter for decimal value order of magnitude
			count = 1
			
			# Traverse through all digits of operand 
			while (i < len(expression) and (expression[i].isdigit() or expression[i]=='.')): 

				# Calculate integer value of operand
				if expression[i].isdigit():
					val = (val * 10) + float(expression[i]) 
					i += 1

				# If there is a decimal value, calculate that as well
				else:
					i += 1
					while (i < len(expression) and expression[i].isdigit()):
						dec = dec+float(expression[i])/(10**count)
						count += 1
						i+=1

			# Add integer and decimal value together and append to operands stack
			operands.append(val+dec) 
			continue
		
		# If current element is a close parenthesis, evaluate the entire expression within the parentheses
		elif expression[i] == ')': 
		
			# Perform all computations within the parentheses and update operands stack accordingly
			while len(operations) != 0 and operations[-1] != '(': 
			
				operand2 = operands.pop() 
				operand1 = operands.pop() 
				op = operations.pop() 
				
				operands.append(compute(operand1, operand2, op)) 
			
			# Pop open parenthesis from operations stack 
			operations.pop() 

		# If the operand is a negative number, do the same as for positive operands, except make the operand negative
		elif expression[i] == '-' and (not expression[i-1].isdigit() or i==0):

			# Move index to first digit of negative number
			i+=1

			# Integer value
			val = 0

			# Decimal value
			dec = 0

			# Counter for decimal value order of magnitude
			count = 1
			
			# Traverse through all digits of operand
			while (i < len(expression) and (expression[i].isdigit() or expression[i]=='.')): 

				# Calculate integer value of operand
				if expression[i].isdigit():
					val = (val * 10) + float(expression[i]) 
					i += 1

				# If there is a decimal value, calculate that as well
				else:
					i += 1
					while (i < len(expression) and expression[i].isdigit()):
						dec = dec+float(expression[i])/(10**count)
						count += 1
						i+=1

			# Add integer and decimal value together, subtract result from zero to make it negative, and append to operands stack
			operands.append(0-(val+dec)) 
			continue
		
		# Otherwise, current element is an operator 
		else: 
		
			# Apply all computations before the current operator, as long as they have higher or equal priority to the current operator
			while (len(operations) != 0 and priority(operations[-1]) >= priority(expression[i])): 
						
				operand2 = operands.pop() 
				operand1 = operands.pop() 
				op = operations.pop() 
				
				operands.append(compute(operand1, operand2, op))
			
			# Push operator to operator stack
			operations.append(expression[i]) 
		
		i += 1
	
	# Once the entire expression has been traversed, apply any remaining computations 
	while len(operations) != 0: 
		
		operand2 = operands.pop() 
		operand1 = operands.pop() 
		op = operations.pop() 
				
		operands.append(compute(operand1, operand2, op)) 
	
	# Answer is on the top of the operands stack
	answer = operands[-1]
	return answer

# main
if __name__ == "__main__":  
    print(solve("-100.75 * (5+ 2 * 12 ) / 14- -100.75"))
