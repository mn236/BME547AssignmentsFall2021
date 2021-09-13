def create_database_entry(patient_name, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient


# Prints each entry on a new line
def print_database(db):
    for patient in db:
        print(patient[0])  # print just names
        print(patient[0][0])  # print first initials


# Print numbered list of entries in the database
def print_numbered_database(db):
    for i in range(len(db)):
        print("{} - {}".format(i, db[i]))


# Print numbered list of entries in the database, "zip" command can also be used to do this
def print_numbered_and_indexed_database(db):
    locations = ["Room1", "Room 4", "ER", "Post-op"]
    for i, patient in enumerate(db):
        print("{} - {} - {}".format(i, patient,
                                    locations[i]))

# Print patient names with ages over specified age
def print_patients_over_age(age, db):
    for patient in db:
        if patient[2] > age:
            print(patient[0])


def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient


def main():
    db = []
    x = create_database_entry("Ann Ables", 120, 30)
    # Append command will save each entry into db list. Can also be written as
    # db.append(create_database_entry("Ann Ables", 1, 30))
    db.append(x)
    x = create_database_entry("Bob Boyles", 24, 31)
    db.append(x)
    x = create_database_entry("Chris Chou", 33, 33)
    db.append(x)
    x = create_database_entry("David Dickins", 14, 34)
    db.append(x)

    y = db[1]  # access second entry in database
    q = db[-1]  # access last entry in database, -2 takes to second to the last etc
    j = db[1:3]  # access the 1st and 2nd entries
    # names = db[]
    # print(j)

    # print_database(db)
    # print_patients_over_age(32, db)
    # found_patient = get_patient(db, 4)
    # print(found_patient)
    # print_numbered_and_indexed_database(db)

    patient_id_tested = 24
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    #Add data to the end of a list
    patient[3].append(test_done)

    print_numbered_and_indexed_database(db)
    print(patient)


if __name__ == "__main__":
    main()
