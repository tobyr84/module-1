# print("What would you like to do?")
# all_input = input()
# all_input = all_input.split(" ")
# operator = all_input[0]
# numberA_str = all_input[1]
# numberB_str = all_input[2]
# numberA = int(numberA_str)
# numberB = int(numberB_str)

# print("Okay, you want to calculate " + numberA_str + operator + numberB_str + "?")
# print(calculate(operator, numberA, numberB))

def calculate(operator, numberA, numberB):
    if operator == "+":
        return numberA + numberB
    elif operator == "-":
        return numberA - numberB
    elif operator == "x":
        return numberA * numberB
    elif operator == "/":
        return numberA / numberB
    else: 
        return "You don't want to do anything I know how to do."

with open("text.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        # print(line)
        data = line.split(' ')
        # print(data)
        operator = data[1]
        numberA = int(data[2])
        numberB = int(data[3])
        result = calculate(operator, numberA, numberB)
        print(result)