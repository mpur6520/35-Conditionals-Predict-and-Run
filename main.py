#maru puran
#october 23, 2023
#analyze and predict code in order to familiarize ourselves with boolean values and if statements, as well as how they work and can be used

# Example code 1

age = 18 #set age variable (create it) and assign it the numerical value 18
 
if age > 18: #check for if the age variable is equal to a value greater than 18 (it's not, it's equal to 18)
 print("You are old enough to drive") #if age is greater than 18, print this message

#the message isn't printed because the conditional statement isn't true

# Example code 2

num1 = 1337 #set and create the num1 variable to numerical value 1337
 
if num1 == 10: #check if num1 is equal to 10, it is not 
  print("This text is output because the condition was true") #print this message if the conditional is true, it is not so this message isn't printed
else: #code that runs if the condition is false
  print("This text is output because the condition was false") #this message is printed because the conditional is false

#print the message "this text is output because the condition was false"

# Example code 3

number = 5 #create variable number and set the value numerical equal to 5
print("I have thought of a number between 1 and 10") #print this message "I have thought of a number between 1 and 10"
guess = int(input("Can you guess what it is?")) #create a variable "guess" to store a numerical value of which the user inputs; user is asked to guess the number and inputs it

#i noticed that if the user inputs "two" instead of "2" after I run the program, the error called is "Traceback (most recent call last):
  #File "main.py", line 29, in <module>
    #guess = int(input("Can you guess what it is?"))
#ValueError: invalid literal for int() with base 10: 'two'"
#this is a value error because it can't translate a string into an integer if it's not a numerical value

if guess == number: #checks if the user's number is equal to the number stored, 5; 
  print("Correct!") #if the user guesses the correct number 5 then tell them they're correct
if guess < number: #checks if the user's number is less than the number stored, 5
  print("Too Low!") #if the user's number is less than 5 then print the words "too low"
if guess > number: #checks if the user's number is greater than the number stored, 5
  print("Too High!") #if the user's number is greater than 5 then tell them their number is "too high"

#create a program for the user to guess a number between 1 and 10, prints messages depending on what number they input using booleans and if statements

#if the user is bigger than 10 or smaller than 0 the program will run; an improvement would be to make the user unable to enter something over 10 or smaller than 0. You can put a code using boolean values to check for this, and alert the user if the number is over 10 or smaller than 0. For example!!: 

#if guess > 10 or guess < 1:
  #print("Your number is invalid >:( !")
