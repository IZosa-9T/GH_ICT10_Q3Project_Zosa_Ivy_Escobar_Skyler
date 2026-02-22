
from pyscript import display, document

def confirm_validity(e):
    document.getElementById('validity_message').innerHTML = ' ' # clears existing content in the element with that specific id
    username = document.getElementById('viewer_username').value # collects data input by the user
    password = document.getElementById('viewer_password').value

    # if-elif-else + nested statements
    # len is used to distinguish the length of the password and username
    # isalpha and isdigit is to ensure the input meets the requirements
    if not len(username) >= 7:
        if len(username) == 6:
            display(f'error 1, username lacks 1 more character', target='validity_message')
        elif len(username) == 5:
            display(f'error 1, username lacks 2 more characters', target='validity_message')
        elif len(username) == 4:
            display(f'error 1, username lacks 3 more characters', target='validity_message')
        elif len(username) == 3:
            display(f'error 1, username lacks 4 more characters', target='validity_message')
        elif len(username) == 2:
            display(f'error 1, username lacks 5 more characters', target='validity_message')
        elif len(username) == 1:
            display(f'error 1, username lacks 6 more characters', target='validity_message')
        elif len(username) == 0:
            display(f'error 1, username lacks 7 more characters', target='validity_message')

    elif not len(password) >= 10:
        if len(password) == 9:
            display(f'error 2, password lacks 1 more character', target='validity_message')
        elif len(password) == 8:
            display(f'error 2, password lacks 2 more characters', target='validity_message')
        elif len(password) == 7:
            display(f'error 2, password lacks 3 more characters', target='validity_message')
        elif len(password) == 6:
            display(f'error 2, password lacks 4 more characters', target='validity_message')
        elif len(password) == 5:
            display(f'error 2, password lacks 5 more characters', target='validity_message')
        elif len(password) == 4:
            display(f'error 2, password lacks 6 more characters', target='validity_message')
        elif len(password) == 3:
            display(f'error 2, password lacks 7 more characters', target='validity_message')
        elif len(password) == 2:
            display(f'error 2, password lacks 8 more characters', target='validity_message')
        elif len(password) == 1:
            display(f'error 2, password lacks 9 more characters', target='validity_message')
        elif len(password) == 0:
            display(f'error 2, password lacks 10 more characters', target='validity_message')

    elif not password.isalpha():
        if password.isdigit():
            display(f'error 3, password requires at least 1 letter', target='validity_message')
        else:
            display(f'account successfully created', target='validity_message')

    elif password.isalpha():
        display(f'error 3, password requires at least 1 digit', target='validity_message')

# the values of different sections are numbers, which is why "int" is used before getting the value of the user's selection
# grade levels are disregarded when it comes to assigning teams, which is why or is used (as any level is valid as long as it is selected)
def Signup(e):
    document.getElementById('output').innerHTML = " "

    RegistrationConfirmation = int(document.querySelector('input[name="Registration"]:checked').value)
    ClearanceConfirmation = int(document.querySelector('input[name="Clearance"]:checked').value)
    SectionConfirmation = int(document.querySelector('input[name="Section"]:checked').value)
    GradeLevelConfirmation = int(document.querySelector('input[name="Grade"]:checked').value)

    if RegistrationConfirmation == 1 and ClearanceConfirmation == 1 and SectionConfirmation == 3 and (GradeLevelConfirmation == 7 or GradeLevelConfirmation == 8 or GradeLevelConfirmation == 9 or GradeLevelConfirmation == 10):
        display(f'Congratulations! You are in team Yellow Tigers.', target='output')
    elif RegistrationConfirmation == 1 and ClearanceConfirmation == 1 and SectionConfirmation == 4 and (GradeLevelConfirmation == 7 or GradeLevelConfirmation == 8 or GradeLevelConfirmation == 9 or GradeLevelConfirmation == 10):
        display(f'Congratulations! You are in team Blue Bears.', target='output')
    elif RegistrationConfirmation == 1 and ClearanceConfirmation == 1 and SectionConfirmation == 5 and (GradeLevelConfirmation == 7 or GradeLevelConfirmation == 8 or GradeLevelConfirmation == 9 or GradeLevelConfirmation == 10):
        display(f'Congratulations! You are in team Red Bulldogs.', target='output')
    elif RegistrationConfirmation == 1 and ClearanceConfirmation == 1 and SectionConfirmation == 6 and (GradeLevelConfirmation == 7 or GradeLevelConfirmation == 8 or GradeLevelConfirmation == 9 or GradeLevelConfirmation == 10):
        display(f'Congratulations! You are in team Green Hornets.', target='output')
    elif RegistrationConfirmation == 2 and ClearanceConfirmation == 1:
        display(f'Please complete your registration form first, proceed to the OBMC Digital Platform.', target='output')
    elif RegistrationConfirmation == 1 and ClearanceConfirmation == 2:
        display(f'Please proceed to the OBMC Clinic to confirm if you are of good health.', target='output')
    elif RegistrationConfirmation == 2 and ClearanceConfirmation == 2:
        display(f'(01) Please complete your registration form first, proceed to the OBMC Digital Platform. (02) Please proceed to the OBMC Clinic to confirm if you are of good health.', target='output')
    else:
        display(f'Invalid input, please complete the form.', target='output')

# lists to iterate the people in the class
# count to easily identify number of players
def player_list(e):
    document.getElementById('outputplayer').innerHTML = ''
    
    topaz = ["Abdullah", "Abeleda", "Arce", "Arias", "Bonzon", "Cajucom", "Catimbang", "Choi", "Cotioco", "Daradal", "Enriquez", "Escobar", "Espina", "Gano", "Garcia", "Kaur", "Ong", "Rufo", "Santos", "Sanchez", "Tan", "Vilale", "Yao", "Zosa"]

    count = 1

    for index in range(len(topaz)):
        display(f'({count:02d}) {topaz[index]}', target='outputplayer')
        if count == 24:
            break

        count += 1


