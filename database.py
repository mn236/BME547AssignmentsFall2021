import blood_calculator as bc

print("This is the database.py module")
print("It's name is {}".format(__name__))

# from blood_calculator import hdl_analysis

answer = bc.hdl_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

answer2 = bc.ldl_analysis(200)
print("The analysis of 200 LDL is {}".format(answer2))
