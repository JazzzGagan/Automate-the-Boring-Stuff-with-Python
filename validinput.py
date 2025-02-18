while True:
    print("Enter you Age")
    age = input()
    if age.isdecimal():
        break
    print('Please Enter valid Age')

while True:
    print('Select a password (letters and number only)')
    password = input()
    if password.isalnum():
          break
    print("Passwords can only have letters and numbers")
