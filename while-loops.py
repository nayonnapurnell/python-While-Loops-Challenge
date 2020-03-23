#Ask the user if they understand Python While loops


answer = "NO"
keepGoing = True

name = input("What's your name? ")
print(f"{name}, do you understand Python while loops?")
comprehensionResponse = input("Enter yes/no: ")
comprehensionResponse = comprehensionResponse.upper()


while comprehensionResponse == answer:
        print(f"Ok, {name}, while loops in Python repeat as long as a certain Boolean condition is met.")
        print(f"{name}, now do you understand Python while loops?")
        comprehensionResponse = input("Enter yes/no: ")
        comprehensionResponse = comprehensionResponse.upper()

        if comprehensionResponse == answer:
            print(f"{name}, now do you understand Python while loops?")
        else:
            print(f"That's great, {name}.  I'm pleased that you understand while loops now.  That was getting repetitive.")

print(f"That's great, {name}.  I'm pleased that you understand while loops now.  That was getting repetitive.")


        
       
       

       



