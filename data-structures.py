# This code demonstrates the use of data structures
# Starting with lists, this shows how to create and append to an existing list

boys = ["olamide", "ayo", "uche"]
boys.append("louise")


# Define a function called to list the name of boys in the class
def boy_names():
   # print("Enter a boy name: ")
    """Created a while loop to come back to the prompt
        if the conditions aren't met"""
    
    while True:
        names = input("Enter a name of any boy in this class: ").lower()
        if names in boys:
            print(f"Yes, {names} is a member of this class")
        
        else:
            print(f"{names} is not a member of this class.")
        confirmation = input("Would you like to enter another name: (yes/no)").lower()

        if confirmation != "yes":
            print("Goodbye")
            break
        # else: return names 

return_value = boy_names()
print(return_value)
