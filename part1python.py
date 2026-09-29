#1. Say Hello
#Read a name from input and print a greeting.
#def greeting(name):
#    print("Hello!, ",name)
#    
#a = input("Enter your name: ")
#greeting(a)

#2. Celsius to Fahrenheit
#Convert a temperature from Celsius to Fahrenheit
#try:
#    celsius = float(input("Enter your celsius: "))
#    convert = (celsius * 9/5) + 32 
#    print(f"{convert:.2f} F'")
#except ValueError:
#    print("it is invalid")

#3. Even or Odd
#Check if a number is even or odd.
#try:
#    value = int(input("Enter your number: "))
#    if value % 2 == 0:
#        print("it is an EVEN")
#    elif value % 2 == 1:
#        print("it is an ODD")
#    else:
#  #      print("it is wrong")
#except ValueError:
#    print("it is invalid")
#    
#4. Make a Username
#Create a username and initials from a first and last name.
#try:
#    name1 = input("Enter your first name: ")
#    name2 = input("Enter your second name: ")
#    print(f"{name1} {name2}")
#    print(name1[0] + name2[0])
#except ValueError:
#    print("it's invalid")
#    
#5. Voting Age
#Determine if a person is old enough to vote.
#try:
#    age = int(input("Enter your AGE: "))
#    if age >= 18:
#        print("you're are Elligble for Vote")
#    elif age > 0:
#        print("you're not Elligble for Vote")
#    else:
#        print("your are enter negative value")
#except ValueError:
#    print("Enter the value, it's wrong")


#6. Grade Calculator
#Convert a score into a letter grade.

#try:
#    percentage = float(input("Enter your percentage: "))
#    if percentage >= 90:
#        print("Grade: A")
#    elif percentage >= 80:
#        print("Grade: B")
#    elif percentage >= 70:
#        print("Grade: C")
#    elif percentage >= 60:
#        print("Grade: D")
#    elif percentage >= 50:
#        print("Grade: E")
#    elif percentage >= 33:
#        print("Grade: -E")
#    elif percentage <= 0:
#        print("it is negative input: Error")
#    else:
#        print("Grade: Fail")
#except ValueError:
#    print("invalid entered")


#7. #Multiplication Table
#Print the multiplication table for a given number.
#try:
#    num = int(input("Enter your number for table: "))
#    for i in range(1 , 11):
#        print(f"{num} X {i} =  {num*i}")
#except ValueError:
#    print("it is invalid")
#         OR
#def number(num):
#    for i in range(1 , 11):
#        print(f"{num} X {i} = {num*i}")
#try:
#    value = int(input("Enter your number: "))
#    number(value)
#except ValueError:
#    print("it is wrong")   
#8. Factorial
#Create a function that calculates the factorial of a number.

#def factorial(n):
#    result += 1
#n = int(input("Enter your number" ))
#for i in range(1 , n+1):
#    print(n*i)

#def factorial(n):
#    result = 1

#    for i in range(1, n + 1):
#        result = result * i
#    return result
#n = int(input("Enter a number: "))
#print(factorial(n))

#9. Sum of Numbers
#Read a list of numbers and calculate their sum.number

#try:
#    number = list(map(int , input("Enter your number by sepratted space: ").split()))
#    x = sum(number)
#    print(f"sum of: {x}")
#except ValueError:
#    print("It is wrong input")

#10. Area Calculator
#Calculate the area of a rectangle, triangle, or circle.

#print("WRITE THE NUMBER:\n1. Area of Rectangle\n2. Area of Trinangle\n3. Area of Circle")
#try:
#    import math
#    numbers = int(input("Enter your option: "))
#    if numbers == 1:
#        print("Write Base & Height:")
#        info1 = float(input("Enter Base: "))
#        info2 = float(input("Enter Height "))
#        print(f"Area of Rectangle is: {info1*info2:.2f}")
#        
#    elif numbers == 2:
#        print("Write Base & Height:")
#        info1 = float(input("Enter Base: "))
#        info2 = float(input("Enter Height: "))
#        print(f"Area of Triangle is: {(1/2*info1*info2):.2f}")
#    elif numbers == 3: 
#        print("Write Radius:")
#        info1 = float(input("Enter Radius value "))
#        print(f"Area of Circle is: {math.pi*info1**2:.2f}")
#    else:
#        print("Invalid option:")
#except ValueError:
#    print("Invalid number")        

#11. Shopping Receipt
#Read item details from input and print a short receipt.

#try:
#    print("------Recipt------")
#    item = input("Enter your item: ")
#    price = float(input("Enter your price: "))
#    quantity = float(input("Enter your quantity: "))
#except ValueError:
#    print("Here is ValueError, please reenter")
#except NameError:
#    print("Here is Nameerror, please reenter")   
#else:
#    print("-------------")
#    print(f"the item is {item}\nthe total price is {price*quantity}")
#finally:
#    print("done...")

#12. Personal Info
#Read personal details from input and display them.

#try:
#    print("---Inforamtion---")
#    name = input("Enter your name: ")
#    contact = input("Enter your mobile number: ")
#    age = int(input("Enter your AGE: "))
#    if age < 0:
#        print("negative input")
#    elif len(contact) != 10:
#        print("it is wrong mobile number")
#        
#    else:
#        print("-----------")
#        print(name)
#        print(contact)
#        print(age)
#except ValueError:
#    print("It is Valueerror")
#except NameError:
#    print("It is NameError")
#finally:
#    print("----------")

#13. Swap Values
#Read two values and print them in swapped order.

#first_value = input("Enter your first value: ")
#second_value = input("Enter your second value: ")

#print(f"First value is: {second_value}")
#print(f"second value is: {first_value}")

#14. Rectangle Border
#Print a rectangle border made of stars.

#for i in range(1 , 6):
#    if i == 1:
#        print("*" * 5)
#    e" * 5)
#    else:
#        print("*   *")

#15. Repeat Message
#Read a message and a number, then print the message that many times.

#def names(message,number):
#    for i in range(number):
#        print(message)
#        
#name = input("Enter your name: ")
#num = int(input("Enter your number for Repeat: "))

#names(name,num)

#16. Currency Exchange
#Calculate a currency exchange from an amount and rate.

#try:
#    def currency(amount,rate):
#        rtod = amount / rate
#        print(f"{rtod:.2f}")
#        return rtod
#    currency(100,95)
#except ZeroDivsionError:
#    print("it's can't accept 0")
#except ValueError:
#    print("it's value error")
 
#17. BMI Calculator
#Calculate Body Mass Index from weight and height.
#    
#def bmi(weight,height):
#    calculate = weight / (height/100)**2
#    print(f"{calculate:.2f}")
#    return calculate
#a = float(input("Enter your weight(KG): "))
#b = float(input("Enter your height(CM): "))   
#bmi(a,b)

#18. Circle Properties
#Calculate the circumference and area of a circle.
#import math
#def circle(radius):
#    circumference = 2 * math.pi * radius
#    area = math.pi * radius**2 
#    print(f"The circumference of circle is: {circumference:.2f} and The Area of circle is: {area:.2f}")
#    return circumference
#    
#try:
#    a = float(input("Enter your radius: "))
#    circle(a)
#except ZeroDivisionError:
#    print("it is a zero, change the radius value")

#19. Simple Calculator
#Perform basic arithmetic on two numbers.

#def calculator(first_num,second_num,sign):
#    if sign == 1:
#        return first_num + second_num
#    elif sign == 2:
#        return first_num - second_num
#    elif sign == 3:
#        return first_num * second_num
#    elif sign == 4:
#        if second_num == 0:
#            return "Can't devide by 0, Reenter"
#        else:      
#            return first_num / second_num
#    return "Choose right number"
#try:
#    print("Enter number what do you want:\n1. addition\n2. subtraction\n3. muliplication\n4. devision ")
#    sign = int(input("Enter what do you want: "))
#    num1 = float(input("Enter your first value: "))
#    num2 = float(input("Enter your second value: "))
#    a = calculator(num1,num2,sign)
#    print(f"Total: {a:.2f}")
#except ValueError:
#    print("Please Enter number")

#20. Discount Price
#Calculate a discounted price from a price and discount percentage.

#def discount(price,discount):
#    total = price * discount/100
#    return price - total
#    
#try:
#    price_ = float(input("Enter your price: "))
#    discount_ = float(input("Enter your discount: "))
#    call = discount(price_,discount_)
#    print(call)
#except ValueError:
#    print("only numbers availble ")

#21. Split the Bill
#Split a total amount equally among a group of people.

#def split_bill(amount,people):
#    return amount/people
#try:
#    bill = float(input("Enter your bill amount: "))
#    person = int(input("Enter your person: "))
#    a = split_bill(bill,person)
#    print(F"per person give: {a}")
#except ValueError:
#    print("it is invalid")
#except ZeroDivisionError:
#    print("can not devided by 0")

#22. Digit Extractor
#Extract the individual digits of a 3-digit number.

#try:
#    digit = input("Enter your 3 digits: ")
#    if len(digit) == 3:
#        print(f"first number: {digit[0]}")
#        print(f"second number: {digit[1]}")
#        print(f"third number: {digit[2]}")
#    else:
#        print("Enter only 3 digit")
#except ValueError:
#    print("Enter digits only")

#23. Word Counter
#Count the number of words in a sentence.

#def count(word):
#    return len(word.split())

#word_num = input("Enter your word: ")
#print(f"the number of word is: {count(word_num)}")

#24. Shout It Out
#Convert a string to uppercase and print its length.

#def lenght_count(string):
#    return len(string)
#    
#word = input("Enter your sentences: ")
#print(f"the sentence: {word.upper()} and lenght of sentences is:  {lenght_count(word)}")     


#25. First and Last
#Print the first and last character of a word.
#word = input("Enter your Word: ")
#print(f"This is first word: {word[0]}\nThis is last word: {word[-1]}")

#26. Repeat String
#Read a string and a iber, then print the string repeated that many times.

#def repeat(string,iber):
#    for i in range(1,iber+1):
#        print(string) 
#word = input("Enter your word: ")
#i = int(input("Enter iber: "))
#repeat(word,i)        

#27. Range Checker
#Check if a iber falls within a given range.

#def range_cheker(i,first_i,last_i):
#    if first_i <= i <= last_i:
#        print("It is in the range")
#    else:
#        print("It is not in the range")
#try:
#    a = int(input("Enter your first iber: "))
#    b = int(input("Enter your last iber: "))
#    c = int(input("Enter your iber for check: "))
#    range_cheker(c,a,b)
#except ValueError:
#    print("Enter right value")    

#28. Password Check
#Check if a password is long enough.

#def password(word):
#    if len(word) >= 8:
#        return print("paasword is long enough")
#    else:
#        return print("password is short, Reenter plz")

#i = input("Enter your password: ")
#password(i)

#29. Ticket Price
#Determine the ticket type and price based on age.

#def ticket_price(age):
#    if age <= 0:
#        print("your age is wrong")
#    elif age <= 6:
#        print("It's kid ticket\nthe price is: 0")
#    elif age <= 18:
#        print("it's minor ticket\nthe price is: $120")
#    elif age <= 50:
#        print("you are young\nthe price is: $200")
#    elif age <= 100:
#        print("you are an old\nthe price is: $180")
#    else:
#        print("you can not enter, you are overaged")
#try:
#    age_i = int(input("Enter your Age: "))
#    ticket_price(age_i)
#except ValueError:
#    print("Enter ibers only")

#30. Positive Negative Zero
#Check if a iber is positive, negative, or zero.
#def i_checker(i):
#    if i < 0:
#        return "It's Negstive"
#    elif i > 0:
#        return "It's Postitive"
#    else:
#        return "It's Zero"
#try:
#    iber = float(input("Enter your iber: "))
#    print(i_checker(iber))
#except ValueError:
#    print("Only for ibers")

#31. Smallest of Three
#Find the smallest of three ibers.

#def smallest_i(a,b,c):
#    if a <= b and a <= c:
#        return a
#    elif b <= a and b <= c:
#        return b
#    else:
#        return c
#try:
#    first_i = float(input("Enter your first name: "))
#    second_i = float(input("Enter your second name: "))        
#    third_i = float(input("Enter your third name: "))       
#    print(f"it is smallest iber: {smallest_i(first_i,second_i,third_i)}")
#except ValueError:
#    print("it is invalid, enter ibers only")   

#32. Countdown
#Count down from a iber to 1 and print Go!

#def countdown(i):
#    for i in range(i,0,-1):
#        print(i)
#        print("Go!e numbers")
#    for i in range(1,num+1):
#        if i % 3 == 0 and i % 5 == 0:
#            print("fizzbuzz")
#        elif i % 3 == 0:
#            print("fizz")
#        elif i % 5 == 0:
#            print("buzz")
#        else:
#            print(i)
#try: 
#    number = int(input("Enter your number: "))
#    game(number)    
#except ValueError:
#    print("Enter only numbers")    

#34. Sum 1 to N
#Calculate the sum of all numbers from 1 to N.

#def sum(n):
#    result = 0
#    for i in range(1,n+1):
#        result += i
#    return result        
#num = int(input("Enter your number: "))
#print(sum(num))

#35. Star Triangle
#Print a right triangle made of stars.

#for i in range(1,6):
#    print("*" * i)

#36. Tip Calculator
#Create a tip calculator function for a restaurant bill.

#def tip_calculator(bill,tip_per):
#    a = bill * tip_per/100
#    return bill + a
#try:         
#    bill_amount = float(input("Enter your bill amount: "))
#    tip = float(input("Enter your tip percentage: "))
#    print(f"The total amount of bill: {tip_calculator(bill_amount,tip):.2f}")
#except ValueError:
#    print("Enter numbers only")

#37. Power Function
#Write a function that calculates the power of a number.

#def power_calculator(num,power):
#    return num ** power
#try:
#    number = float(input("Enter your number: "))
#    exponent = float(input("Enter your power: "))
#    print(f"This is the Total: {power_calculator(number,exponent):.2f}")
#except ValueError:
#    print("Enter numbers only")
                                                                                                                                                                                                                          