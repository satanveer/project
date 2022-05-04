import random 
characters="1234567890()abcdefghijklmnopqrstuvwxyz"
while 1:
    password_len=int(input("what would you like your length to be:"))
    password_count=int(input("how many passwords do you like:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char =random.choice(characters)
            password=password+password_char
            print("here is your pw",password)

     

    
    

