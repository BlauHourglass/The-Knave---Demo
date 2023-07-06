#  entire character creation for both player and companion

import time
import colors


# Player config
while True:
    user_name = input("Name: ")
    if user_name == "":
        print("Pick an actual name.")
    else:
        break

while True:
    try:
        user_age = int(input("Age: "))
        if user_age >= 16:
            break
        else:
            print("Please be of at least 16 years of age...")
    except ValueError:
        print("Please input an actual integer as an age.")

while True:
    user_gender = input("Gender: ").lower()
    if user_gender == 'male':
        break
    elif user_gender == 'female':
        break
    else:
        print("Casshu! Male or female!")


while True:
    user_hair_color = input("Hair color: ").lower()
    if user_hair_color not in colors.colors:
        print("Choose an actual color.")
    else:
        break

while True:
    user_eye_color = input("Eye color: ").lower()
    if user_eye_color not in colors.colors:
        print("Choose an actual color.")
    else:
        break



# Companion's config
while True:
    name = input("Companion's name: ")
    if name == "":
        print("Pick an actual name.")
    else:
        break

while True:
    try:
        age = int(input("Companion's age: "))
        if age >= 16:
            break
        else:
            print("Please have your companion be at least 16 years old...")
    except ValueError:
        print("Please input an actual integer as an age.")

while True:
    gender = input("Companion's gender: ").lower()
    if gender == 'male':
        break
    elif gender == 'female':
        break
    else:
        print("Casshu! Male or female!")

while True:
    hair_color = input("Companion's hair color: ").lower()
    if hair_color not in colors.colors:
        print("Choose an actual color.")
    else:
        break

while True:
    eye_color = input("Companion's eye color: ").lower()
    if eye_color not in colors.colors:
        print("Choose an actual color.")
    else:
        break


companion_hearts_base = 100
companion_hearts = {"Companion Hearts": companion_hearts_base}


if user_gender == 'female':
    user_possessive_pronoun = 'Her'
    user_pronoun = 'She'
    user_addressed_pronoun = 'Her'
    user_self_pronoun = 'Herself'

if user_gender == 'male':
    user_possessive_pronoun = 'His'
    user_pronoun = 'He'
    user_addressed_pronoun = 'Him'
    user_self_pronoun = 'Himself'

if gender == 'female':
    possessive_pronoun = 'Her'
    pronoun = 'She'
    addressed_pronoun = 'Her'
    self_pronoun = 'Herself'

if gender == 'male':
    possessive_pronoun = 'His'
    pronoun = 'He'
    addressed_pronoun = 'Him'
    self_pronoun = 'Himself'


class User:
    def __init__(self, name, age, hair_color, eye_color, gender):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.gender = gender

user = User(user_name, user_age, user_hair_color, user_eye_color, user_gender)