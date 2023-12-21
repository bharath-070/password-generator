#password generator
#import the random module for using choice and shuffle
import random # or from random , u can import only choice and shuffle
#declare the letters , numbers and sysmbols
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","^","&","*","(",")","-","_"]
print("welcome to the py_passoword generator !")
#ask the user to enter the length of the password
pass_letters=int(input("how many letters do you want in your password? "))
pass_numbers=int(input("how many numbers do you want in your password? "))
pass_symbols=int(input("how many symbols do you want in your password? "))
#declare the password as a string
password=''
#using for loop and .choice function to add the letters, numbers and symbols to 
#the password
for i in range(pass_letters):
  random_letters=random.choice(letters)
  #use the end="" for concatination of the next line
  password+=random_letters
for i in range(pass_numbers):
  random_numbers=random.choice(numbers)
  password+=random_numbers
for i in range(pass_symbols):
  random_symbols=random.choice(symbols)
  password+=random_symbols
  #the password is been generated but not shuffled
#to shuffle the password , it should be converted into the list
password=list(password)
#use the random.shuffle function to shuffle the password
random.shuffle(password)
#the password is in the list , needs to be converted into the string
#but if str() is used for conversion then there will be brackets([]) present in 
#the end ,that should be removed using .join are other methods
#here i have used for loop for conversion
final_password=''#declare the final_password as a string
for char in password:
  final_password+=char
print(f"the generated password is : {final_password}")#fstring is used
