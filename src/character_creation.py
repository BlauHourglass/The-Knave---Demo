#  entire character creation for both player and companion

import time
import colors


# Player config
class User:
    def __init__(self):
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
                if u_age >= 16:
                    break
                else:
                    print("Please be of at least 16 years of age...")
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
    
        self.u_name = u_name
        self.u_age = u_age
        self.u_gender = u_gender
        self.u_hair_color = u_hair_color
        self.u_eye_color = u_eye_color

    def u_confirm(self):
        print("Are you sure you want this configuration?")
        time.sleep(0.7)
        print(f"Name: {self.u_name}")
        time.sleep(0.7)
        print(f"Age: {self.u_age}")
        time.sleep(0.7)
        print(f"Gender: {self.u_gender.capitalize()}")
        time.sleep(0.7)
        print(f"Hair color: {self.u_hair_color.capitalize()}")
        time.sleep(0.7)
        print(f"Eye color: {self.u_eye_color.capitalize()}")
        time.sleep(0.7)
        print(f"1. Yes\n2. No")

while True:
    player = User()
    time.sleep(1)
    player.u_confirm()
    response = input("")
    match response:
        case "2":
            print("Feel free to reconfigure your choices then.")
            time.sleep(0.5)
            pass
        case _:
            pass
    if response == "1":
        break



# Companion's config
class Companion:
    def __init__(self):
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
                if c_age >= 16:
                    break
                else:
                    print("Please have your companion be at least 16 years old...")
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

        self.c_name = c_name
        self.c_age = c_age
        self.c_hair_color = c_hair_color
        self.c_eye_color = c_eye_color
        self.c_gender = c_gender
    
    def c_confirm(self):
        print("Are you sure you want this configuration?")
        time.sleep(0.7)
        print(f"Companion's name: {self.c_name}")
        time.sleep(0.7)
        print(f"Companion's age: {self.c_age}")
        time.sleep(0.7)
        print(f"Companion's gender: {self.c_gender.capitalize()}")
        time.sleep(0.7)
        print(f"Companion's hair color: {self.c_hair_color.capitalize()}")
        time.sleep(0.7)
        print(f"Companion's eye color: {self.c_eye_color.capitalize()}")
        time.sleep(0.7)
        print(f"1. Yes\n2. No")


while True:
    partner = Companion()
    time.sleep(1)
    partner.c_confirm()
    response = input("")
    match response:
        case "2":
            print("Feel free to reconfigure your choices then.")
            time.sleep(0.5)
            pass
        case _:
            pass
    if response == "1":
        break


# user's possesive pronoun, pronoun, addressed pronoun, and self pronoun
if player.u_gender == 'female':
    user_p_p = 'Her'
    user_p = 'She'
    user_a_p = 'Her'
    user_s_p = 'Herself'

if player.u_gender == 'male':
    user_p_p = 'His'
    user_p = 'He'
    user_a_p = 'Him'
    user_s_p = 'Himself'

# companion's possesive pronoun, pronoun, addressed pronoun, and self pronoun
if partner.c_gender == 'female':
    c_p_p = 'Her'
    c_p = 'She'
    c_a_p = 'Her'
    c_s_p = 'Herself'

if partner.c_gender == 'male':
    c_p_p = 'His'
    c_p = 'He'
    c_a_p = 'Him'
    c_s_p = 'Himself'

u_name = player.u_name
u_age = player.u_age
u_gender = player.u_gender
u_hair_color = player.u_hair_color
u_eye_color = player.u_eye_color

c_name = partner.c_name
c_age = partner.c_age
c_hair_color = partner.c_hair_color
c_eye_color = partner.c_eye_color
c_gender = partner.c_gender

companion_hearts_base = 100
c_hearts = companion_hearts_base
c_heart_level = {"Companion Hearts": c_hearts}