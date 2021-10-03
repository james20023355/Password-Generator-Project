import random


def GeneratePassword():
    password = ""
    for n in range(10):
        password += chr(random.randint(48, 126))
    return password


def main():
   Password = GeneratePassword()

   print(Password)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

