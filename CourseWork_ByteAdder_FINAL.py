import time  # Imports time function



# SIMPLE CALCULATIONS FUNCTIONS START HERE #
def multiply():  # Multiply function
    binA, binB = binInput()  # Takes value in binary format
    a = binDec(int(binA))  # Converts into decimal
    b = binDec(int(binB))
    print("\nIn Binary format:")
    print("The result of " + binA + "x" + binB + " is: ""{0:0{1}b}".format(a * b, 8))
    print("\nIn Decimal format:")
    print("The result of " + str(a) + "x" + str(b) + " is: " + str(a * b))
    print("")
    simple_calc()


def sub():  # Subtraction function
    binA, binB = binInput()
    a = binDec(int(binA))
    b = binDec(int(binB))
    print("\nIn Binary format:")
    print("The result of " + binA + "-" + binB + " is: ""{0:0{1}b}".format(a - b, 8))
    print("\nIn Decimal format:")
    print("The result of " + str(a) + "-" + str(b) + " is: " + str(a - b))
    print("")
    simple_calc()


def convert():  # Decimal to Binary conversion. Positive or negative numbers
    choice = int(input("Type 1 for positive numbers only\n"
                       "Type 2 for positive and negative numbers\n"
                       "Type 0 to go back\n"))
    if choice == 1:
        dec = int(input("Enter a decimal number between 0 and 255: "))
        while dec < 0 or dec > 255:
            dec = int(input("Number has to be between 0 and 255: "))
        print("\nThe Binary representation of the Decimal", dec, "is:", "{0:0{1}b}".format(dec, 8), "\n")

        choice_inside_converter()

    elif choice == 2:
        dec = int(input("Enter a decimal number between -127 and +127: "))
        while dec < -127 or dec > 127:
            dec = int(input("Number has to be between -127 and +127: "))
        if dec < 0:
            sign = 0
            dec = dec * -1
            print("\nThe Binary representation of the Decimal -" + str(dec) + " is: " + str(sign) + "{0:0{1}b}".format(
                dec, 7), "\n")
        else:
            sign = 1
            print("\nThe Binary representation of the Decimal", dec, "is: " + str(sign) + "{0:0{1}b}".format(dec, 7),
                  "\n")

        choice_inside_converter()

    elif choice == 0:
        simple_calc()
    else:
        print("Invalid choice.")
        convert()


def choice_inside_converter():
    choice = int(input("Would you like to convert another number?\n"
                       "Type 1 to convert another number\n"
                       "Type 2 to go back to main menu\n"))
    if choice == 1:
        convert()
    elif choice == 2:
        start()
    else:
        print("Invalid option, going back to main menu.")
        start()


def bin_add():
    decimal = 0
    first_binary = str(input('Enter the first 8 bit Binary number: '))
    while len(first_binary) > 8:
        first_binary = str(input("Number needs to be less than 8 bits\n"
                                 "Please try again: "))
    if first_binary[1] not in (1, 0):
        print("Only 1s or 0s allowed.")
        bin_add()

    for digit in first_binary:
        decimal = decimal * 2 + int(digit)
    print(decimal)


# SIMPLE CALCULATIONS FUNCTIONS END HERE#

# SIMPLE CALCULATION CHOICES#
def simple_calc():
    choice = int(input("Select an option: \n"
                       "1 to convert Decimal to Binary \n"
                       "2 for Binary subtraction \n"
                       "3 for Binary multiplier \n"
                       "0 to Main Menu \n"))
    if choice == 1:
        convert()  # Converts decimal input, either positive or negative to Binary
    elif choice == 2:
        sub()
    elif choice == 3:
        multiply()
    elif choice == 0:
        start()
    else:
        print("Please choose one of the options")
        simple_calc()


# BINARY TO DECIMAL CONVERTER
def binDec(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# GATES FUNCTIONS
def OR(A, B):
    return A | B


def AND(A, B):
    return A & B


def XOR(A, B):
    return A ^ B


def option_1():  # This is the choice 1 from start menu
    choice = int(input("\nHow would you like to proceed?\n"
                       "Type 1 for Binary input\n"
                       "Type 2 for Decimal input\n"))
    if choice == 1:
        print("\nEntering Byte Adder...\n"
              "\nThis Byte Adder will take two inputs as a byte binary number(8-bit) each,\n"
              "and it will select each bit of each byte and pass through the byte adder\n"
              "showing you the result of each bit adder,\n"
              "and give you the sum of the bytes at the end.\n"
              "Enjoy!\n")
        input("Type Enter to proceed.")
        print("Loading...\n")
        byte_adder("a", "b")  # This will load the byte adder straight, the "a" and "b" string is to make sure
        # it will load the binary input.

    elif choice == 2:
        print("\nEntering Byte Adder...\n"
              "\nThis Byte Adder will take two inputs as a Decimal number each,\n"
              "it will convert you numbers into binary,\n"
              "then select each bit of each byte and pass through the byte adder\n"
              "showing you the result of each bit adder,\n"
              "and give you the sum of the bytes at the end.\n"
              "Enjoy!\n")
        input("Type Enter to proceed.")
        print("Loading...\n")
        decInput()  # This will load the decimal input, and it will throw into the byte adder straight

    else:
        print("Please select one of the options provided.\n")
        option_1()

        ############## PROGRAM STARTS HERE ##################


# MAIN MENU FUNCTION STARTS HERE#
def start():
    print("\nWelcome to Byte Adders Two Thousand! \n"  # Little welcoming for the program
          "Your favorite Byte Adder Program!\n"
          "\nPlease follow the instructions provided \n"
          "")
    choice = int(input("Select an option: \n"  # User has 3 choices
                       "Type 1 for Byte Adder \n"
                       "Type 2 for Simple Calculations \n"
                       "Type 3 to Quit \n"))
    # if else statement to select one of the options and call its function
    if choice == 1:
        option_1()
    elif choice == 2:
        print("Entering Simple Calculations...")
        simple_calc()
    elif choice == 3:
        print("Exiting the Program...")
        exit()
    else:
        print("Please select one of the options provided.\n"
              "")
        start()


# MAIN MENU FUNCTION ENDS HERE#

def decInput():  # DECIMAL INPUT FUNCTION
    a = int(input("Enter the first decimal number up to 255: "))  # Gets the first input
    while a < 0 or a > 255:  # Make sure it is in the standards
        a = int(input("The number has to be between 0 and 255: "))
    a = "{0:0{1}b}".format(a,
                           8)  # Transform the decimal into 8 digits binary, if the user type a decimal that contains less than 8-bits it will add leading zeros to the number.

    b = int(input("Enter the second decimal number up to 255: "))  # Exactly the same as input "a"
    while b < 0 or b > 255:
        b = int(input("The number has to be between 0 and 255: "))
    b = "{0:0{1}b}".format(b, 8)

    byte_adder(a, b)  # Call to the byte_adder functions, adding "a" and "b"


def binInput():  # BINARY INPUT FUNCTION
    # Takes the first input and checks if it is not more than 8 characters
    a = str(input("Please enter the first binary number (8-bit, only 1s or 0s): "))
    while len(a) > 8:
        a = str(input("\nThere was an error on your input,\nPlease try only 0s or 1s, and 8-bit maximum: "))
    all_binary_a = all(
        d in '01' for d in a)  # If is less than 8 digits, it checks if it is only 0s and 1s as in a binary number

    # If the number is all zero and ones then it will skip the next loop
    # If it is not then it will enter the next "while" loop and check for only 0s and 1s and if it is up to 8 digits.
    while all_binary_a is False:
        a = input("\nThere was an error on your input, \nplease try only 0s or 1s, and 8-bit maximum\n"
                  "\nEnter the first binary number again(8-bit, only 1s or 0s): ")
        if len(a) > 8:
            continue
        all_binary_a = all(d in '01' for d in a)
    a = a.zfill(8)  # This code will add leading zeros to the number if is less than 8 digits.

    # And we have the exactly same checks for the second input.
    b = str(input("Please enter the second binary number(8-bit, only 1s or 0s): "))
    while len(b) > 8:
        b = str(input("\nThere was an error on your input,\nPlease try only 0s or 1s, and 8-bit maximum: "))
    all_binary_b = all(e in '01' for e in b)

    while all_binary_b is False:
        b = input("\nThere was an error on your input, \nplease try only 0s or 1s, and 8-bit maximum\n"
                  "\nEnter the second binary number again(8-bit, only 1s or 0s): ")
        if len(b) > 8:
            continue
        all_binary_b = all(e in '01' for e in b)
    b = b.zfill(8)  # Again it adds leading zeros so the number is an 8-bit binary number.
    return a, b


# BYTE ADDER FUNCTION STARTS HERE#
def byte_adder(a, b):
    if a == "a" and b == "b":
        a, b = binInput()
    c = list()  # Starts an empty list which will be the binary result
    prev = 0  # Carryout from previous column starts at zero
    s = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
         "eighth"]  # This list contains the header for each bit adder on the loop
    reverseA = a[::-1]  # This two codes reverse the inputs
    reverseB = b[::-1]
    print("Loading...\n")
    time.sleep(2)  # 2 sec delay was added just to make it more interesting and suspenseful :)
    print("________________________________________________________________________________")
    print("\nByte adder starts here")  # Indicates where the byte adder starts

    ####### BYTE ADDER LOOP STARTS HERE ######
    for A, B, S in zip(reverseA, reverseB, s):
        A = int(
            A)  # For each character of the inputs, it changes them from string to integer and add it to each function bellow
        B = int(B)

        print(
            "\nGenerating " + S + " bit adder...")  # This is the header for each bit adder, it takes the values of the "s" list above

        # Functions of the adder
        output_1 = AND(A, B)  # First AND gate
        output_2 = XOR(A, B)  # First XOR gate
        output_3 = AND(output_2, prev)  # Second AND gate
        sum = XOR(output_2, prev)  # Sum between A and B inputs
        next_column = OR(output_1, output_3)  # Next column carrier

        # This next few if statements it is just to show the user the individual results of each gates in the bit adders
        # First AND gate output
        if output_1 == 1:
            print("\nThe first AND gate output is: 1")
        else:
            print("\nThe first AND gate output is: 0")

        # XOR gate output
        if output_2 == 1:
            print("The XOR gate output is: 1")
        else:
            print("The XOR gate output is: 0")

        # Previous column
        print("The previous column output is:", prev)

        # Second AND gate
        if output_3 == 1:
            print("The second AND gate output is: 1")
        else:
            print("The second AND gate output is: 0")

        # Second XOR gate / SUM of the bits
        if sum == 1:  # Depends on what inputs A and B are
            print("The second XOR gate and the sum of the entered bits \"" + str(A) + "\" and \"" + str(B) + "\" is: 1")
        else:
            print("The second XOR gate and the sum of the entered bits \"" + str(A) + "\" and \"" + str(B) + "\" is: 0")

        c.append(sum)  # Append the sum to the list previously created

        # OR gate / Next column
        if next_column == 1:  # Depends on what inputs A and B are
            prev = 1
            print("The OR gate and the next column output is: 1")
        else:
            prev = 0
            print("The OR gate and the next column output is: 0")

        ############### BYTE ADDER LOOP ENDS HERE ###################

    print("________________________________________________________________________________")
    print("\nEnd of the byte adder, you can scroll up to see the result of each bit adder.\n")

    listToStr = "".join(map(str, c))  # Makes the list "c" into a string
    inversedStr = listToStr[::-1]  # Reverse the "c" string back to its original form

    if next_column == 1:  # If the last result of OR gate/next column is 1, then is an overflow.
        result = str(next_column) + str(
            inversedStr)  # Add the result to the front of the number, that makes it possible to have a result more than 8-bit
    else:
        result = inversedStr

    # Prints the result in Binary and Decimal using the binDec() function to convert the numbers
    print("Binary format: \n"
          "The SUM of", a, "and", b, "is:", result)
    print("\nDecimal format: \n"
          "The SUM of", binDec(int(a)), "and", binDec(int(b)), "is:", binDec(int(result)))

    # End of the FULL BYTE ADDER and back to the choices.

    choice = None  # Define our input with nothing first of all
    while choice not in (1, 2):  # loop the program each time we haven't entered either 1 or 0
        choice = int(input("\nSelect an option: \n"
                           "Type 1 to generate another Byte Adder \n"
                           "Type 2 to go back to main menu \n"))
        if choice == 1:
            option_1()
        elif choice == 2:
            start()
    ##### BYTE ADDER FUNCTION ENDS HERE #####


start()
