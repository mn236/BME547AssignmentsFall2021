# Make a branch
# Use it
# Push to GitHub
# Merge to Main on Git Hub
# Locally Checkout main
# Pull from Github
# Repeat

print("This is the database.py module")
print("It's name is {}".format(__name__))


def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("3 - Total Cholesterol Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            hdl_driver()
        elif choice == 2:
            ldl_driver()
        elif choice == 3:
            total_driver()

        print(choice)
    return choice


# *****************HDL********************
def hdl_driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)


def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))  # type: int
    return hdl_value


def hdl_analysis(HDL_value):
    if HDL_value > + 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"


def hdl_output(HDL_value, HDL_character):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_character))
    return


# *****************LDL******************
def ldl_driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)


def ldl_input():
    ldl_value = int(input("Enter LDL value :"))
    return ldl_value


def ldl_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 159:
        return "Borderline High"
    elif 160 <= LDL_value < 189:
        return "High"
    else:
        return "Very High"


def ldl_output(LDL_value, LDL_character):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_character))
    return


# ************Total Cholesterol***********


def total_driver():
    total_value = ldl_input() + hdl_input()
    total_character = total_analysis(total_value)
    total_output(total_value, total_character)


def total_analysis(total_value):
    if total_value < 200:
        return "Normal"
    elif 200 <= total_value < 240:
        return "Borderline High"
    else:
        return "High"


def total_output(total_value, total_answer):
    print("The total cholesterol value of {} is considered {}".format(total_value, total_answer))
    return


if __name__ == "__main__":
    interface()

hdl_driver()  # Runs code for hdl calculations
ldl_driver()  # Runs code for ldl calculations
