# Python calculator

#Taking first number from user.
num1 = float(input("Enter any number:"))

#Taking operator from user like (+,-,*,/)  
operator = input("Enter operator number(+,-,*,/):" )
 

#Taking second number from user.
num2 = float(input("Enter any number:"))

  # If opreator equal to "+" .
if operator == "+":
 print (num1 + num2)
 
 # Elif opreator equal to "-" .
elif operator == "-":
 print(num1-num2)
 
 # Elif opreator equal to "*" .
elif operator =="*":
 print(num1*num2)
 
 # Elif number2 == 0 .
elif num2 == 0:
 
 #Cannot divide by zero .
 print ("cannot divide by zero")

 # Elif operator equal to "/" .
elif operator == "/" :
 
 # Number1 / Number2 .
 print(num1/num2)