print("Hello, world!")
name=input("What is your name?").title().strip()
print("Hello ",name,sep="!!!",end=" ") #there is a space automatically added between these two arguments in print function
#the comment
#parameter is the variable in the function
#argument is the value passed to the function
#positional parameters follows sequence
#named parameters are optional eg sep='',end='' in print function 


"""
The bigger comment

"""
print(f"Hello , {name}")

#remove whitespace from string
name=name.strip()

#capitalize  the first letter of the string
name=name.capitalize()

#capitalize title
name=name.title()

name=name.strip().title()

#split user's name into first middle and last name 

first,middle,last=name.split()
print(f"first name = {first} Middle name={middle}")

#interactive mode in terminal type python

#explain round(number[, ndigits])  n is till number of places to round off

print(f"{round(1.9835,3)}")
print(f"{1.9835:.3f}")

# Numeric formatting US 000
print(f"{9999+1:,}")





