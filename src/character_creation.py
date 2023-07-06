import time

#  entire character creation for both player and companion

user_bio = []

user_name = input("Name: ")
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
user_hair_color = input("Hair color: ").lower()
user_eye_color = input("Eye color: ").lower()


user_bio.append(user_name)
user_bio.append(user_age)
user_bio.append(user_gender)
user_bio.append(user_hair_color)
user_bio.append(user_eye_color)





companion_bio = []

name = input("Companion's name: ")
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
hair_color = input("Companion's hair color: ").lower()
eye_color = input("Companion's eye color: ").lower()


companion_bio.append(name)
companion_bio.append(age)
companion_bio.append(gender)
companion_bio.append(hair_color)
companion_bio.append(eye_color)

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