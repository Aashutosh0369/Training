    import csv
from datetime import datetime
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_password(password, key):
    cipher_text = Fernet(key)
    return cipher_text.encrypt(password.encode())


def decrypt_password(encrypted_password, key):
    cipher_text = Fernet(key)
    return cipher_text.decrypt(encrypted_password).decode()


def answer(line, line2):
    selected_option = input("Enter Your answer in A,B,C,D:")
    selected_option = selected_option.upper()

    if selected_option == 'A':
        print("selected option is:", line[0])
    elif selected_option == 'B':
        print("selected option is:", line[1])
    elif selected_option == 'C':
        print("selected option is:", line[2])
    elif selected_option == 'D':
        print("selected option is:", line[3])
    else:
        print("INVALID INPUT")

    split_list = [item.split(':') for item in line2]

    for inner_list in split_list:
        key = inner_list[0]
        if f'[{selected_option}]' == key:
            return True


def mcq_question(score, list_, all_marks):
    with open("Questions.csv", 'r') as csv_file, open("Option.csv", 'r') as csv_file2:
        csv_reader = csv.reader(csv_file)
        csv_reader2 = csv.reader(csv_file2)

        for line1, line2 in zip(csv_reader, csv_reader2):
            print(line1)
            modified_line = [element.replace('[', '').replace(']', '') for element in line2]
            print(modified_line)
            all_marks += 10
            if answer(modified_line, line2):
                score += 10

        percentage = (score / all_marks) * 100
        if percentage >= 50:
            print(f'Your result : {percentage}% Passed')
            list_.append(f'score is : {percentage}% Passed')
        else:
            print(f'Your result : {percentage}% Failed')
            list_.append(f'score is : {percentage}% Failed')


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    list_ = []
    list_.append(username)

    login_successfull = False

    with open("user_login_details.csv", 'r') as csv_file:
        csv_reader1 = csv.reader(csv_file)

        for line in csv_reader1:

            if line[0] == username:
                key = line[3].encode()
                encrypted_password = line[2][2:-1].encode()
                decrypted_password = decrypt_password(encrypted_password, key)
                if decrypted_password == password:
                    list_.append(line[1])
                    score = 0
                    all_marks = 0
                    login_successfull = True
                    mcq_question(score, list_, all_marks)

                    current_datetime = datetime.now()
                    formatted_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    list_.append(formatted_date_time)

                    with open("result_data.csv", 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(list_)

    if not login_successfull:
        print("Login Unsuccessfull \n Please do registration.")


def register():

    def reg_login_signup():
        start = input("Press 'y' to register again or Press 'l' to login :").lower()
        if start == 'y':
            register()
        elif start == 'l':
            login()
        else:
            print("Invalid input please enter again!")
            reg_login_signup()

    def user_name(username):

        with open("user_login_details.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == username:
                    print("Username is already register, Please try again with another Username")
                    register()

            return True

    register_list = []
    print("To register Enter required details...")
    Name = input("Enter your Name :")
    Username = input("Enter desired username :")
    if user_name(Username):
        register_list.append(Username)
        register_list.append(Name)

    Password = input("Enter desired passwrod :")
    key = generate_key()
    encrypted_password = encrypt_password(Password, key)
    register_list.append(encrypted_password)
    register_list.append(key.decode())
    print("Please remember your username and password.")

    with open("user_login_details.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(register_list)
    reg_login_signup()


def login_signup():
    print("'s' --> for Signup and 'l' --> for Login : ")
    start = input()
    start = start.lower()

    if start == 's':
        register()
    elif start == 'l':
        login()
    else:
        print("Invalid input please enter again!")
        login_signup()


print("SignUp", "    Login")
print("What do you wish Signup or Login")
login_signup()
