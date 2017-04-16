#3

math_expression = input("Please enter a mathematical expression using positive integers and spaces in between them: ")

space_1 = math_expression.find(' ')
operand1 = int(math_expression[0:space_1])
operator = math_expression[space_1+1]
sep_operator = math_expression[space_1+1:]
space_2 = sep_operator.find(' ')
operand2 = int(sep_operator[space_2+1:])

if operator == "+":
    answer = operand1 + operand2
    print(operand1, "+",operand2,"=",answer)

if operator == "=":
    answer = operand1 - operand2
    print(operand1, "-", operand2, "=",answer)

if operator == "*":
    answer = operand1 * operand2
    print(operand1, "*", operand2, "=",answer)

if operator == "/":
    answer = operand1 / operand2
    print(operand1, "/", operand2, "=",answer)
