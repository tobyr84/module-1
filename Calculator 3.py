print("what would you like to do?")
operator = input ()
print("First Number?")
numberA_str = input ()
print("Second Number?")
numberB_str = input ()

numberA = int(numberA_str)
numberB = int(numberB_str)

print ("Okay, you want to calculate " + numberA_str + operator + numberB_str + "?")

if operator == "+":
    print(numberA + numberB)
elif operator == "-":
    print(numberA - numberB)
elif operator == "*":
    print(numberA * numberB)
elif operator == "/":
    print (numberA / numberB)

