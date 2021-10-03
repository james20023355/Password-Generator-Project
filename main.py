import random

def GeneratePassword(passwordLength, uppercase, lowercase, digit, special ):

    minPassLen = 0
    maxPassLen = 50
    password = ""

    if minPassLen < passwordLength <= maxPassLen:
        for n in range(passwordLength):

            while len(password) != passwordLength:
                setToChoose = random.randint(1, 4)
                if setToChoose == 1:
                    if uppercase.upper() == 'Y': # Uppercase
                        password += chr(random.randint(65, 90))
                elif setToChoose == 2:
                    if lowercase.upper() == 'Y':  # Lowercase
                        password += chr(random.randint(97, 122))
                elif setToChoose == 3:
                    if digit.upper() == 'Y':  # Digits
                        password += chr(random.randint(48, 57))
                elif setToChoose == 4:
                    if special.upper() == 'Y':  # Special
                        setNumber = random.randint(1,4)
                        if setNumber == 1:
                            password += chr(random.randint(33, 47))
                        elif setNumber == 2:
                            password += chr(random.randint(58, 64))
                        elif setNumber == 3:
                            password += chr(random.randint(91, 96))
                        else:
                            password += chr(random.randint(123, 126))

        return password
    else:
        print("> Invalid password length, Please enter a number between 1-50")
        return


def main():
    print("> Hello, Welcome to: Password Generator ")

    passwordLength = int(input("> Enter a Password Length [1-50]: "))
    containsUpper = input("> Do you want any uppercase Letters in your password? [Y/N]: ")
    containsLower = input("> Do you want any lowercase Letters in your password? [Y/N]: ")
    containsDigit = input("> Do you want any digits in your password? [Y/N]: ")
    containsSpecial = input("> Do you want any special Letters in your password? [Y/N]: ")
    Password = GeneratePassword(passwordLength, containsUpper, containsLower, containsDigit, containsSpecial)

    if Password  != None:
        print(Password)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

