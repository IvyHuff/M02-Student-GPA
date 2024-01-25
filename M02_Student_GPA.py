# Jordan Hufford
# Student GPA
# Program has student enter their name then checks this GPA to see if they have made the Dean's list or Honor Roll

while True:
    #asks for students last name, if "zzz" quits program
    last_name = input("Enter last name: ")
    if last_name == 'ZZZ':
        break

    #asks first name
    first_name = input("Enter first name: ")

    #asks students GPA
    gpa = float(input("Enter GPA: "))

    #checks if students GPA is 3.5 or greater 
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")

    #checks if students GPA is 3.25 or greater
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
