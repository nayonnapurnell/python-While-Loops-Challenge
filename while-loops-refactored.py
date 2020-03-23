#Ask the user for their name
name = input("What's your name? ")

#Ask the user if they understand Python While loops.  
#Print the users input to the screen
comprehension = print(input(f"{name}, do you understand Python while loops?\n(Enter yes or no:)"))


#Create a while statement that checks if the user doesn't understand while loops

while comprehension.lower()== 'no':
    #If the user doesn't understand Python loops, explain them.
    print(f"Ok, {name}, while loops in Python repeat as long as a certain Boolean condition is met.")

    #Ask the user again, by name, if they understand Python loops.
    comprehension =input(print(f"{name}, now do you understand Python while loops?"))

#Outside the while loop, congratulate the user for understanding while loops.
print(f"That's great, {name}.  I'm pleased that you understand while loops now.  That was getting repetitive.")

      

