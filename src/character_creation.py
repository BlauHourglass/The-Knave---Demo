#  entire character creation for both player and companion

import time
import colors
import datetime

current_time = datetime.datetime.now()
redo = False
move_on = False

try:
    # Player config
    while True:
        while True:
            try:
                u_name = input("Name: ").capitalize()
            except:
                pass
            if u_name == "":
                print("Pick an actual name.")
            else:
                break

        while True:
            try:
                u_age = int(input("Age: "))
                if u_age >= 18:
                    break
                else:
                    print("Age must be at least 18.")
            except ValueError:
                print("Please input an actual integer as an age.")

        while True:
            u_gender = input("Gender: ").lower()
            if u_gender == 'male':
                break
            elif u_gender == 'female':
                break
            else:
                print("Casshu! Male or female!")


        while True:
            u_hair_color = input("Hair color: ").lower()
            if u_hair_color not in colors.colors:
                print("Choose an actual color.")
            else:
                break

        while True:
            u_eye_color = input("Eye color: ").lower()
            if u_eye_color not in colors.colors:
                print("Choose an actual color.")
            else:
                break


        while True:
            time.sleep(1)
            print("Are you sure you want this configuration?")
            time.sleep(0.7)
            print(f"Name: {u_name}")
            time.sleep(0.7)
            print(f"Age: {u_age}")
            time.sleep(0.7)
            print(f"Gender: {u_gender.capitalize()}")
            time.sleep(0.7)
            print(f"Hair color: {u_hair_color.capitalize()}")
            time.sleep(0.7)
            print(f"Eye color: {u_eye_color.capitalize()}")
            time.sleep(0.7)
            while True:
                print(f"1. Yes\n2. No")
                response = input("")
                match response:
                    case "1":
                        move_on = True
                        break
                    case "2":
                        print("Feel free to reconfigure your choices then.")
                        time.sleep(0.5)
                        redo = True
                        break
                    case _:
                        print("Invalid input. '1' or '2'.")
                        break

            if move_on:
                break
            if redo:
                break

        if move_on:
            break


    redo = False
    move_on = False
    
    # Companion's config
    while True:
        while True:
            try:
                c_name = input("Companion's name: ").capitalize()
            except:
                pass
            if c_name == "":
                print("Pick an actual name.")
            else:
                break

        while True:
            try:
                c_age = int(input("Companion's age: "))
                if c_age >= 18:
                    break
                else:
                    print("Age must be at least 18.")
            except ValueError:
                print("Please input an actual integer as an age.")

        while True:
            c_gender = input("Companion's gender: ").lower()
            if c_gender == 'male':
                break
            elif c_gender == 'female':
                break
            else:
                print("Casshu! Male or female!")


        while True:
            c_hair_color = input("Companion's hair color: ").lower()
            if c_hair_color not in colors.colors:
                print("Choose an actual color.")
            else:
                break

        while True:
            c_eye_color = input("Companion's eye color: ").lower()
            if c_eye_color not in colors.colors:
                print("Choose an actual color.")
            else:
                break

        while True:
            time.sleep(1)
            print("Are you sure you want this configuration?")
            time.sleep(0.7)
            print(f"Companion's name: {c_name}")
            time.sleep(0.7)
            print(f"Companion's age: {c_age}")
            time.sleep(0.7)
            print(f"Companion's gender: {c_gender.capitalize()}")
            time.sleep(0.7)
            print(f"Companion's hair color: {c_hair_color.capitalize()}")
            time.sleep(0.7)
            print(f"Companion's eye color: {c_eye_color.capitalize()}")
            time.sleep(0.7)
            while True:
                print(f"1. Yes\n2. No")
                response = input("")
                match response:
                    case "1":
                        move_on = True
                        break
                    case "2":
                        print("Feel free to reconfigure your choices then.")
                        time.sleep(0.5)
                        redo = True
                        break
                    case _:
                        print("Invalid input. '1' or '2'.")
                        break

            if move_on:
                break
            if redo:
                break

        if move_on:
            break


    # user's possesive pronoun, pronoun, addressed pronoun, and self pronoun
    if u_gender == 'female':
        user_p_p = 'Her'
        user_p = 'She'
        user_a_p = 'Her'
        user_s_p = 'Herself'

    if u_gender == 'male':
        user_p_p = 'His'
        user_p = 'He'
        user_a_p = 'Him'
        user_s_p = 'Himself'

    # companion's possesive pronoun, pronoun, addressed pronoun, and self pronoun
    if c_gender == 'female':
        c_p_p = 'Her'
        c_p = 'She'
        c_a_p = 'Her'
        c_s_p = 'Herself'

    if c_gender == 'male':
        c_p_p = 'His'
        c_p = 'He'
        c_a_p = 'Him'
        c_s_p = 'Himself'
    
    companion_hearts_base = 100
    c_hearts = companion_hearts_base
    c_heart_level = {"Companion Hearts": c_hearts}

except (Exception, KeyboardInterrupt) as e:
	try:
		error_log = open("error_log.txt", "a")
		error_log.close()
	except:
		error_log = open("error_log.txt", "x")
		error_log.close()
	with open("error_log.txt", "a") as error_log:
		error_log.write(f"{current_time}: Character Creation: {e}\n")
	error_message = input("Something has gone wrong with the main program. Please press \"enter\" to quit.")