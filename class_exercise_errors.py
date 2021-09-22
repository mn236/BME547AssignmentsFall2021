# a = "The sky is blue"
# print(a)

#for letter in a:
#    print(letter)

def function_name():

    try:
        int("hello5")
    except ValueError:
        str("hello5")

    x = str("hello5")
    print(x)

def main():
    function_name()

if __name__ == "__main__":
    main