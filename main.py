import calculator

inputn = str()
number1 = int()
number2 = int()
answer = float()

def Variables_0():
	print("Current Variable Configurations in 'main.py' (GLOBAL):")
	print("(string) inputn = ", inputn)
	print("(integer) number1 = ", number1)
	print("(integer) number2 = ", number2)
	print("(floating point) answer = ", answer)

print("Welcome to ccDOS!\n")

while (inputn != "shut"):
	inputn = input("input> ")

	if (inputn == "shut"):
		print("Shutting off...")
	
	elif (inputn == "V_0"):
		Variables_0()

	elif (inputn == "basic-add"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicAddition(number1, number2)
		print("Answer:", answer)
	
	elif (inputn == "basic-subtract"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicSubtraction(number1, number2)
		print("Answer:", answer)

	elif (inputn == "basic-multiply"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicMultiplication(number1, number2)
		print("Answer:", answer)

	elif (inputn == "basic-divide"):
		number1 = calculator.basicCalculator.basicNumberInput()
		number2 = calculator.basicCalculator.basicNumberInput()
		answer = calculator.basicCalculator.basicDivision(number1, number2)
		print("Answer:", answer)

	elif (inputn == "aaes"):
		print("You found the secret! :O")
		print("Here's a cookie: \U0001F36A")

	else:
		print("Not a valid command.")
