def update(a):
    # a = a + 2
    a[0] = a[0] + 2
    return a


def main():
    # b = 5
    b = [5]
    x = update(b)
    print(b)
    print(x)


if __name__ == "__main__":
    main()


#******************* NOTES ******************
# In python, lists are mutable but integers are NOT
# List values can be changed and modified but integers cant
# If parameters is a str, int, float, boolean
# If it is a list, it is a dictionary