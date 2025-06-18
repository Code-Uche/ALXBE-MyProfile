class People: # This is a class used to list different races
    name = ""   # This are attributes inherited by all objects within the class
    age = 30
    hobbies = []

black = People()    # These are objects within the class
asian = People()
hispanic = People()
arab = People()
caucasian = People()

print(id(black))
print(asian)
print(id(hispanic))
print(arab)
print(id(caucasian))


# Lets define functions and how to call them

def myFunction():
    """This is the formula for defining a function"""
    # code block
    # code block
    return  # A function must return something 

# Now lets define our function for a login page
def login(email, password):
    return "This is the right credentials" if email == "preciousueze@gmail.com" and password == "password123"\
          else "Enter the correct credentials"
    print(f"Can user login: {login('preciousueze@gmail.com', 'password123')}")
    # Not passing a value to return automatically sets it to None.

return_value = login("example@example.com", "kjsvnkjsn")

if return_value is login("djkfdndk@example.com", "pasanfjsknd"):
    print("access denied")
else:
    print("Access granted")


