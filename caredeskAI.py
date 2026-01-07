import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    engine.setProperty('rate',160)
    engine.setProperty('volume',1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak('Hello!! Welcome to ABC Care Clinic')
print(' Welcome to ABC Care Clinic\n------------------------------')
speak('I am CareDesk AI.')
speak('Your virtual receptionist.')


while True:
    speak('How can I help you today?')
    speak('Please choose one of the following actions')
    speak('Press 1 for Registration, press 2 for Book an appointment, press 3 for Enquiry, press 4 for emergency assistance')
    print('Main Menu')
    print('_________')
    print('1.Registration\n2.Book an appointment\n3.Enquiry\n4.Emergency')
    ch = int(input('Your choice:'))
    if ch == 1:
        speak('You have selected patient registration. Let us begin.')
        print('\n Registration\n_________________')
        speak('Please Enter your full name.')
        name = input('Patient name : ')
        speak(f'Thank you {name}')
        speak('Please enter your age in years.')
        age = int(input('Age : '))
        speak('Noted.')
        speak('Please say your gender. Male. Female. Or Other')
        gender = input('Gender : ')
        speak('Thank you. Please enter your phone number')
        phone = int(input('Contact : '))
        speak('Recorded. Your registration is complete. Your registration ID is one zero two three nine')
        print('Registration ID :10239')
        speak('Is there anything else I can help you with? Say Yes or No.')
        choice = input('\nEnter yes/no : ').lower()
        if choice == 'yes':
            continue
        else:
            break

    elif ch == 2:
        speak('You have selected appointment services.')
        print('\n Book an Appointment\n_________________________')
        speak('Please enter your registration ID')
        id = input('Registration ID : ')
        speak(f'Your registration id is {id}')
        speak('Please enter your preferred date.')
        date = input('Preferred Date : ')
        speak('Please enter your preferred time.')
        time = input('Preferred Time : ')
        speak('Based on the selected date and time, your appointment will be with Doctor Indira. Is this okay? Please say Yes or No.')
        choice = input('Enter yes/no : ').lower()
        if choice == 'yes':
            speak('Thank you. Your appointment has been confirmed with Doctor Indira.. Please arrive ten minutes early.')
            print('Doctor available : Indira')
        else:
            speak('Apologies. No doctor is available at the chosen date and time. Would you like to cancel the appointment? Say Yes or No.')
            choice = input('Enter yes/no : ').lower()
            if choice == 'yes':
                break
            else:
                speak('Thank you. Your appointment has been confirmed with Doctor Indira.. Please arrive ten minutes early.')
                print('Doctor available : Indira')
        speak('Is there anything else I can help you with? Say Yes or No.')
        choice = input('Enter yes/no : ').lower()
        if choice == 'yes':
            continue
        else:
            break

    elif ch == 3:
        speak('You have selected basic enquiries.')
        while True:
            print('\n Enquiry\n_____________')
            speak('What would you like to know? Please choose one option. Press 1 for working hours. Press 2 for consultation fee. Press 3 for doctor list. Press 4 for clinic location.')
            print('1 : working hours. \n2 : Consultation fee.\n3 : Doctor list. \n4 : Clinic location.')
            c = int(input('Enter your choice:'))
            if c == 1:
                speak('Our clinic is open from nine a.m. to eight p.m. Monday to Saturday. We are closed on Sundays.')
                speak('Is there anything else I can help you with? Say Yes or No.')
                choice = input('Enter yes/no : ').lower()
                if choice == 'yes':
                    continue
                else:
                    break
            elif c == 2:
                speak('The consultation fee is two hundred rupees. Please contact the reception desk for specialist fees.')
                speak('Is there anything else I can help you with? Say Yes or No.')
                choice = input('Enter yes/no : ').lower()
                if choice == 'yes':
                    continue
                else:
                    break
            elif c == 3:
                speak('Our clinic has experienced doctors available. Please visit the reception desk for the complete doctor list and schedules.')
                speak('Is there anything else I can help you with? Say Yes or No.')
                choice = input('Enter yes/no : ').lower()
                if choice == 'yes':
                    continue
                else:
                    break
            elif c == 4:
                speak('Our clinic is located at Main Road, near City Hospital. Please ask the reception desk for directions if needed.')
                speak('Is there anything else I can help you with? Say Yes or No.')
                choice = input('Enter yes/no : ').lower()
                if choice == 'yes':
                    continue
                else:
                    break
            else:
                speak('Sorry. That option is not available. Please visit the reception desk for further assistance.')
                break
        break

    elif ch == 4:
        speak('This appears to be an emergency. Please proceed to the emergency ward immediately. Or call one zero eight.')
        break
    else:
        speak('Sorry. That option is not available. Please visit the reception desk for further assistance.')
        break

speak('Thank you for visiting our clinic. Take care. Goodbye.')