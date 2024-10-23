# Ryan Rupp - Created original empty repo, main(), encoder() functions
# Brody Rayhill - Will create decoder() function

# The purpose of this program is take a string of integers as a password and add the ability to encode and decode it.

def main():
    while True:
        displayMenu()
        user_input = input("Please enter an option: ")
        if int(user_input) == 1:
            encoded_password = encode()
        elif int(user_input) == 2:
            decoded_password = decode(encoded_password)
        elif int(user_input) == 3:
            exit()
        else:
            print("Invalid option. Please try again.")
            print()

def displayMenu():
    print("Menu\n-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    return

def encode():
    pw_check = False
    while pw_check == False: # Checks for valid password input
        password = input("Please enter your password to encode: ")
        if len(password) == 8: # Make sure password is 8 chars long
            count = 0
            for i in password:
                if i.isdigit(): # Make sure each digit of password is an integer
                    count += 1
                    if count == 8: pw_check = True
                else:
                    print("Invalid password. Please try again.")
                    count = 0
                    break
        else:
            print("Invalid password. Please try again.")
    password_list = []
    for i in password:
        num = int(i)
        password_list.append(num)
    for i in range(len(password_list)):
        password_list[i] = str(password_list[i] + 3)
    encoded_password = ''.join(password_list)
    print("Your password has been encoded and stored!")
    print()
    return encoded_password

def decode(encoded_password): #Brody Rayhill's Decoder function with encoded password parameter
    
    decoded_list = []
    for i in encoded_password:
        num = int(i)
        decoded_list.append(num)
    for i in range(len(decoded_list)):
        decoded_list[i] = str(decoded_list[i] - 3)
    decoded_password = ''.join(decoded_list)
    print("The encoded password is "+encoded_password+", and the original password is "+decoded_password+".")
    return decoded_password

if __name__ == "__main__":
    main()
