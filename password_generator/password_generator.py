import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range (length):
        password += random.choice(characters)

    return password
#program entry point outside the characters 
print("============== SALOH PASSWORD GENERATOR ===============")
length = int(input("Enter password length:"))
if length < 6:
    print("password should be at least 6  characters ")
else:
    password = generate_password(length)
    print("Generated password:",password)