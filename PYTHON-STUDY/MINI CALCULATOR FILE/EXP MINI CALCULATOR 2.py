def CALCULATOR():
    print("WELCOME TO THE MINI CALCULATOR!")
    print("SELECT THE OPERATION:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")

    # TAKE USER INPUT FOR OPERATION CHOICE
    CHOICE = int(input("ENTER CHOICE (1/2/3/4): "))

    # TAKE THE NUMBER OF CALCULATIONS USER WANTS TO PERFORM
    NUM_OPERATIONS = int(
        input("HOW MANY NUMBERS DO YOU WANT TO USE IN THIS OPERATION? "))

    # INITIALIZE THE RESULT WITH THE FIRST NUMBER
    RESULT = float(input("ENTER THE FIRST NUMBER: "))

    # PERFORM THE CALCULATION BASED ON USER INPUT
    for i in range(1, NUM_OPERATIONS):
        NUM = float(input(f"ENTER NUMBER {i + 1}: "))
        if CHOICE == 1:
            RESULT += NUM
        elif CHOICE == 2:
            RESULT -= NUM
        elif CHOICE == 3:
            RESULT *= NUM
        elif CHOICE == 4:
            if NUM != 0:
                RESULT /= NUM
            else:
                print("ERROR! DIVISION BY ZERO IS NOT ALLOWED.")
                return

    print(f"THE RESULT IS: {RESULT}")


# CALL THE CALCULATOR FUNCTION
CALCULATOR()
