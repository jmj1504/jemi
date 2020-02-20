print("Please select operation -\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
select = input("Select operations form 1, 2, 3, 4 : ")

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if(select == 1):
    print str(number_1), "+", str(number_2), "=", str(sum.add(number_1, number_2))
  
elif select == 2:
    print(str(number_1), "-", str(number_2), "=", str(diff.subtract(number_1, number_2)))

elif select == 3:
    print(str(number_1), "*", str(number_2), "=", str(pro.multiply(number_1, number_2)))

elif select == 4:
    print(str(number_1), "/", str(number_2), "=", str(quo.divide(number_1, number_2)))
	
else:
    print("Invalid input")
