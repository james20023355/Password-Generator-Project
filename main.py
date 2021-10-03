import random


def GeneratePassword(passwordLength):
    password = ""

    if 0 < passwordLength < 50:
        for n in range(passwordLength):
            password += chr(random.randint(48, 126))
        return password
    else:
        print("> Invalid password length, Please enter a number between 1-50")
        return




def main():
    print("> Hello, Welcome to: Password Generator ")

    passwordLength = int(input("> Enter a Password Length [1-50]: "))
    Password = GeneratePassword(passwordLength)

    if Password  != None:
        print(Password)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

