def calculator():
     num = float(input("enter num: "))
     num2 = float(input("enter num2: "))
     operator = input("enter operator: ")

     if operator == "+":
         result = num + num2
         print(result)
     elif operator == "-":
         if num <= num2:
             result = num2 - num
             print(result)
         else:
             result = num - num2
             print(result)
     elif operator == "/":
         result = num / num2
         print(result)
     elif operator == "*":
         result = num * num2
         print(result)
     else:
         print("wrong operator")


def nem():
    for every_calculation in calculator():
        print(every_calculation)

