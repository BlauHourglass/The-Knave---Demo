import time
import character_creation
import misc_classes
import pygame


# channel 0 = knave_st
# channel 1 = birds_chirping
# channel 2 = footsteps
# channel 3 = 
# channel 4 = piano_horror
# channel 5 = river
# channel 6 = sicilian_cafe
# channel 7 = cinematic_swell

# initializing pygame module
pygame.init()
pygame.mixer.init()


# "backstory" to demo
prompt = misc_classes.Text("(PRESS ENTER TO CONTINUE AFTER EACH LINE)")
prompt = misc_classes.Text("...")
prompt = misc_classes.Text("You lazily slink to your bed, tossing your jacket onto your desk in the process. You slide under the covers, taking a deep breath.")
prompt = misc_classes.Text("It has been a crazily long day, and all you need is a good night's rest. You close your eyes, letting exhaustion finally take a grasp of your body and mind, and you finally fall asleep.")
prompt = misc_classes.Text("...")
prompt = misc_classes.Text("\"...will no...ive...\"")
prompt = misc_classes.Text("...")
prompt = misc_classes.Text("\"...at's...ough...!\"")
prompt = misc_classes.Text("...")
prompt = misc_classes.Text("\"Welco...avel...\"")
prompt = misc_classes.Text("...")
prompt = misc_classes.Text("\"...Our finest Knave...\"")
prompt = misc_classes.Text("...")
prompt = misc_classes.Text(f"\"Arise, {character_creation.user_name}, arise!\"")
prompt = misc_classes.Text(f"...")

# knave opening soundtrack
knave_st = misc_classes.Music("knave_st", 0, "knave_st_channel", -1, 0, 0)

# birds chirping
birds_chirping = misc_classes.Sound_effect("birds_chirping", 1, "birds_chirping_channel", -1, 0, 0)


# forest path scene
prompt = misc_classes.Text(f"You wake up, blinking wearily in the glaring sunshine.")
prompt = misc_classes.Text(f"The cheery chirping of birds reaches your ears, and you look around, bewildered and hurting.")
prompt = misc_classes.Text(f"\"What in the world? Wh-where am I...?\" you mutter, looking closely at your hands.")
prompt = misc_classes.Text(f"You are wearing tattered white bandages around your wrists and knuckles and tan pants tucked into leather boots. You are also wearing a dark leather tunic that is partially tucked into your belt. The collar is open down to your abdomen, displaying a worn white shirt and a silver chain necklace.")
prompt = misc_classes.Text(f"\"My head hurts,\" you murmur, barely audible even to yourself. Your throat is parched and dry, and you feel as if your head has been socked by a sledgehammer. Perhaps you should find some water and then figure out where you are.")
prompt = misc_classes.Text(f"You sit up and hesitantly touch your head. It really, really hurts. Perhaps there is a cut?")
prompt = misc_classes.Text(f"You give a slight hiss as your fingers graze over a large bump and cut on the back of your head. It throbs, and you realize that it is the largest source of your headache. Dehydration is probably the other cause.")
prompt = misc_classes.Text(f"\"Man, what happened...?\" you ask quietly to no one in particular. You stand up shakily. Your limbs and body feel sore all over, and your head hurts even more when you try to think back to... anything. You only recall the faint image of a pale face.")

# footsteps-walking
footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 2000, 1000)

prompt = misc_classes.Text(f"You walk onto the dirt path, looking both ways. Both are shrouded by the tree limbs and foliage from both sides of the path. Thankfully, however, the sunlight is able to filter through the leaves and shine upon the path and grass in splotchy patches.")



# first choice: right or left, ends the same route
while True:
	prompt = misc_classes.Text(f"Which way do you go?")
	enter = input("1: Right\n2: Left\n")
	lower_enter = enter.lower()

	match lower_enter:
		case "1":
			footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 0, 1000)
			prompt = misc_classes.Text(f"Your gut tells you to go right, and so you turn in that direction, hoping that it brings you closer to water and, perhaps, a village where you can heal your wounds.")
			break
		case "2":
			footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 0, 1000)
			prompt = misc_classes.Text(f"You decide to go left and stagger along the dirt path, silently hoping for fresh water and an answer.")
			break
		case _:
			prompt = misc_classes.Text(f"Wrong input. Follow instructions.")

birds_chirping.fade_out(2000)

knave_st.fade_out(2000)

# piano horror
piano_horror = misc_classes.Music("piano_horror", 4, "piano_horror_channel", -1, 0, 4000)

prompt = misc_classes.Text(f"As you walk on, you notice the birds' chirping slowly fading away, and an eerie feeling starts to set in.")

prompt = misc_classes.Text(f"You quicken your pace, but your weakened body and dehydrated state hinder your progress.")
prompt = misc_classes.Text("If anything, the forest is beautiful, but the diminishing sunshine and your growing unease make it difficult to fully appreciate its beauty. The pain, exhaustion, and overall discomfort further dampen your experience.")
prompt = misc_classes.Text(f"\"Where am I, still...?\" you grumble, trying not to be bothered by the growing shadows around you.")

# # river sounds
river = misc_classes.Sound_effect("river", 5, "river_channel", -1, 0, 0)
river.set__volume(0.05)

prompt = misc_classes.Text(f"You continue to walk until you faintly hear the sound of rushing water. Immediately, you feel relieved, and you hurry on. Water — finally!")

# # extra sound effect changing for experience
river.set__volume(0.2)

# # Water is reached, but stranger is sitting on the bank
prompt = misc_classes.Text(f"You run on until you see a river flowing and dashing across rocks and boulders. It is nestled in the forest, creating enough space between the trees to allow a significant amount of light to shine down upon its face.")

piano_horror.fade_out(6000)
footsteps.fade_out(2000)

prompt = misc_classes.Text("You also feel all of the shadows and eeriness fade away from around you, though there are still no birds to be seen or heard.")
prompt = misc_classes.Text(f"You are about to go forward and drink, but you see a person sitting on the bank on a boulder, swinging {character_creation.possessive_pronoun.lower()} shoed foot against the face of the waters and splashing the water.")


while True:
	prompt = misc_classes.Text(f"Do you approach the stranger, wait until {character_creation.pronoun.lower()} leaves, or just ignore {character_creation.addressed_pronoun.lower()} and access the water?")
	demo_stranger_choice = input("1: Approach\n2: Wait\n3: Ignore\n")

	match demo_stranger_choice:
		case "1":
			# friendly and mysterious companion, plus heart points, probably too ru-ish 😭
			
			knave_st.fade_out(2000)

			sicilian_cafe = misc_classes.Music("sicilian_cafe", 6, "sicilian_cafe_channel", -1, 0, 0)

			footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 3000, 1000)

			prompt = misc_classes.Text(f"After a moment of consideration, you stagger over to the stranger. \"E-excuse me,\" you say, barely audible, and {character_creation.pronoun.lower()} turns, turning {character_creation.eye_color} eyes upon you.")
			prompt = misc_classes.Text(f"\"Yes? Can I help you? You look quite haggard,\" {character_creation.pronoun.lower()} hums, ceasing {character_creation.possessive_pronoun.lower()} foot from swinging. {character_creation.pronoun} brings it up to rest on the dry bank, gazing up at you expectantly.")
			prompt = misc_classes.Text(f"You reflexively reach up to hold your head, feeling a sudden shock of pain shoot through your ugly welt. You wince visibly, but you try to speak again. \"W-water,\" you manage.")
			footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 5000, 2000)
			prompt = misc_classes.Text(f"The stranger blinks before giving a short sigh. \"That's obvious,\" {character_creation.pronoun.lower()} mutters, rising to {character_creation.possessive_pronoun.lower()} feet and walking over to you. {character_creation.pronoun} hastens to your side and helps you hobble to the side of the river.")
			prompt = misc_classes.Text(f"{character_creation.pronoun} lowers you gently to the water's edge and supports you while you take a refreshing drink.")
			prompt = misc_classes.Text(f"Relief and vigor surges through your body as you take another drink, and the stranger laughs. \"One would think you were starved from water for days if they saw you drinking like this,\" {character_creation.pronoun.lower()} grins.")
			prompt = misc_classes.Text(f"Despite your slight annoyance at {character_creation.possessive_pronoun.lower()} laughter and teasing about your horrible condition, you can't help but feel very grateful as you dip your stinging hands once more into the rushing water.")
			prompt = misc_classes.Text(f"\"Y-yeah, I guess so,\" you reply, taking your fifth swig before leaning back slightly. Even though the water is terribly refreshing and re-energizing, you still felt weak from dehydration.")
			prompt = misc_classes.Text(f"{character_creation.pronoun} looks at you carefully, anaylzing your countenance before silently taking {character_creation.possessive_pronoun.lower()} pouch from {character_creation.possessive_pronoun.lower()} hip and unlacing the lid.")
			prompt = misc_classes.Text(f"\"Well, traveler, you're in luck today,\" {character_creation.pronoun.lower()} muses, taking out a bandage and soaking it in the water. You glance at {character_creation.addressed_pronoun.lower()}, watching {character_creation.possessive_pronoun.lower()} hands wring out the cloth.")
			prompt = misc_classes.Text(f"You think about it a moment before nodding slowly and raising a hand to your cut. \"Considering you graciously helped me get water and quench my thirst, I suppose I am. For which I thank you for,\" you say. You watch as the stranger takes the wrap and gently applies it to your wound.")
			character_creation.companion_hearts_base + 10
			prompt = misc_classes.Text(f"\"No need to thank me, friend. But not only that, had you gotten here any sooner, you would've been swarmed by a group of bandits. And I daresay, you are in no position of taking them out,\" {character_creation.pronoun.lower()} hums.")
			prompt = misc_classes.Text(f"You pause, looking at {character_creation.addressed_pronoun.lower()} in slight bewilderment. No traces...anywhere...? \"Oh...you took them out?\"")
			prompt = misc_classes.Text(f"\"Well, yes. They were easy ruffians - just punks.\"")
			prompt = misc_classes.Text(f"You aren't sure how to feel, wondering who exactly this stranger is. {character_creation.pronoun} really must've done a good job taking out those thugs. But where are the bodies? A quick glance proves that a scuffle had ensued, but no bodies... Did {character_creation.pronoun.lower()} throw them down the river? Well, nevermind that for now - maybe {character_creation.pronoun.lower()} can tell you where you were.")
			prompt = misc_classes.Text(f"\"Where am I?\" you finally ask, trying to ignore the throbbing of your head.")
			prompt = misc_classes.Text(f"{character_creation.pronoun} gives a slight smile, turning {character_creation.possessive_pronoun.lower()} eyes to the sky. \"You don't know, hm? Well, you're in the world where nothing makes sense and the more you think of it, the less you know.\"")
			prompt = misc_classes.Text(f"{character_creation.pronoun} leans towards you slightly, looking at you with a sly look in {character_creation.possessive_pronoun.lower()} {character_creation.eye_color} orbs. \"A world where you are nothing but a pawn - nay, a dustspeck on the chessboard.\"")
			
			cinematic_swell = misc_classes.Sound_effect("cinematic_swell", 7, "cinematic_swell_channel", 0, 0, 0)

			prompt = misc_classes.Text(f"\"Welcome, my friend, to the Mirror!\" And with that, {character_creation.pronoun.lower()} gives a light laugh and disappears in {character_creation.eye_color} wisps.")
			break

		case "2":
			# rather disinterested and nonchalant companion, less heart points
			knave_st.fade_out(2000)
			
			sicilian_cafe = misc_classes.Music("sicilian_cafe", 6, "sicilian_cafe_channel", -1, 0, 0)

			prompt = misc_classes.Text(f"You hesitate a moment before squatting down on the ground and trying to nurse your headache. However, the stranger doesn't seem like {character_creation.pronoun.lower()} is going to leave, so you wait in silent agony.")
			prompt = misc_classes.Text(f"One minute passes by.")
			prompt = misc_classes.Text(f"Two minutes pass by.")
			prompt = misc_classes.Text(f"Three minutes pass by...")
			prompt = misc_classes.Text(f"...And all throughout, the stranger never turns or even moves from {character_creation.possessive_pronoun.lower()} position.")
			prompt = misc_classes.Text(f"It seems like an eternity before {character_creation.pronoun.lower()} actually changes {character_creation.possessive_pronoun.lower()} position, tilting {character_creation.possessive_pronoun.lower()} head back slightly. \"Well, it seems like we have quite the visitor. Care to introduce yourself, rude one?\" {character_creation.pronoun.lower()} says, turning around slightly to peer through {character_creation.eye_color} eyes at you.")
			prompt = misc_classes.Text(f"You feel your cheeks redden and you internally slap yourself. Of course you'll seem like a wierdo, just watching and waiting. Also stupid. Also - wait, how does {character_creation.pronoun.lower()} know that you were even there?")
			character_creation.companion_hearts_base - 10
			prompt = misc_classes.Text(f"\"Rude and dumb too, I suppose,\" the stranger comments dryly. {character_creation.pronoun} sighs and stretches {character_creation.possessive_pronoun.lower()} arms above {character_creation.possessive_pronoun.lower()} head.")
			prompt = misc_classes.Text(f"\"S-sorry, I just - can't speak v-very well,\" you manage, staggering to your feet and making your way to the waterside. You drop to your knee and dip your hands into the cold, rushing waves, feeling very embaressed. How a mere stranger could elict such mortification was new to you. Man.")
			prompt = misc_classes.Text(f"\"That's clear enough,\" the person scoffs, turning away. {character_creation.possessive_pronoun} {character_creation.eye_color} orbs narrows as they pass over your form again.")
			prompt = misc_classes.Text(f"You silently gulp down the water, letting relief and energy surge through you. However, even with all that, you still feel extremely weary. After taking your sixth draught, you sit back and glance at your hands, wet with the water. \"Yeah, sorry about that,\" you say.")
			prompt = misc_classes.Text(f"The stranger waves {character_creation.possessive_pronoun.lower()} hand dismissively. \"I suppose don't worry about it.\" {character_creation.pronoun} stands up, rearranging {character_creation.possessive_pronoun.lower()} cuffs and beginning to walk away.")
			footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 5000, 0)
			prompt = misc_classes.Text(f"You realize that this person probably knows where you are, and maybe - well, should you get {character_creation.possessive_pronoun.lower()} name too? \"H-hey, before you go, where am I?\" you ask, turning around to look at the person.")
			prompt = misc_classes.Text(f"With a sigh, {character_creation.pronoun.lower()} pauses and turns around just enough to settle {character_creation.pronoun.lower()} {character_creation.eye_color} orbs upon you, seemingly searching your very being.\"So you're also amnesiac, hm?\" {character_creation.pronoun.lower()} shoots with a not-so-kind laugh.")
			prompt = misc_classes.Text(f"\"Very well, stranger. You're in the world where absolutely nothing makes sense, and the more you think of it, the less your poor brain knows,\" {character_creation.pronoun.lower()} continues.")

			cinematic_swell = misc_classes.Sound_effect("cinematic_swell", 7, "cinematic_swell_channel", 0, 0, 0)

			prompt = misc_classes.Text(f"\"Welcome, traveler, to the Mirror.\" And with that, the person gives a slight smirk and disappears in a {character_creation.eye_color} light.")
			break

		case "3":
			# kind and quiet companion, no change in hearts
			knave_st.fade_out(2000)
			
			sicilian_cafe = misc_classes.Music("sicilian_cafe", 6, "sicilian_cafe_channel", -1, 0, 0)

			footsteps = misc_classes.Sound_effect("footsteps", 2, "footsteps_channel", -1, 3000, 1000)

			prompt = misc_classes.Text(f"You blink before walking to the side of the river and ignoring the stranger completely. You walk upstream of {character_creation.addressed_pronoun.lower()}, crouching down by the rushing water.")
			prompt = misc_classes.Text(f"You slip off the bandages on your hands, glancing at the cuts and bruises lining your skin. Man, they look awful. They kinda sting too.")
			prompt = misc_classes.Text(f"You dip your hands into the frigid water, hissing under your breath at the sharp pain that spreads over your hands through the partially open wounds.")
			prompt = misc_classes.Text(f"You don't notice it, but the stranger has been watching you for the past minute and {character_creation.possessive_pronoun.lower()} foot has ceased to swing.")
			prompt = misc_classes.Text(f"\"Well, you don't look too good,\" {character_creation.pronoun.lower()} murmurs after another moment passes, sliding off of the boulder and walking over to you. \"Tell me - do you need help?\" Looking up, you see {character_creation.eye_color} eyes gaze down at you, a bit of sympathy nestled deep within.")
			prompt = misc_classes.Text(f"\"Yeah, sure. That'll actually be great,\" you mutter. Your parched throat hurts as you speak, and you hesitantly take a drink from the river.")
			prompt = misc_classes.Text(f"{character_creation.pronoun} lowers {character_creation.self_pronoun.lower()} to your side, pulling out a leather pouch from {character_creation.possessive_pronoun.lower()} side. {character_creation.pronoun} unlaces the cover and pulls out a white, clean bandage while you continue to drink.")
			prompt = misc_classes.Text(f"The stranger hums quietly as {character_creation.pronoun.lower()} dips the cloth into the water and squeezes it of its excess water, gesturing towards your head.")
			prompt = misc_classes.Text(f"\"Allow me,\" {character_creation.pronoun.lower()} says, and you glance at {character_creation.addressed_pronoun.lower()} for a gauging moment before nodding slowly.")
			prompt = misc_classes.Text(f"The person gently mops up the blood from your wound, washing it out once more(downstream of where you were drinking) and then wrapping it around your crown. \"What befell you, traveler?\" {character_creation.pronoun.lower()} questions, looking at you curiously.")
			prompt = misc_classes.Text(f"You shrug, taking your fourth drink of the water and leaning back slightly. \"I'm not sure,\" you reply, smiling ironically. \"Thanks for the help, though,\" you add.")
			prompt = misc_classes.Text(f"The stranger nods, closing the pouch and straightening up. \"Of course - I saw your plight and wished to help. But how do you not know what happened? Where you ambushed?\"")
			prompt = misc_classes.Text(f"You shrug again, taking your eyes off of the stranger and touching your head. \"I don't know. I don't even know where I am.\" You pause, thinking. But before you can say anything, the stranger speaks up again, an amused ring in {character_creation.possessive_pronoun.lower()} voice.")
			prompt = misc_classes.Text(f"\"In that case, traveler, then I welcome you to the world of confusion and puzzles. A world where you're constantly in a race through a labyrinth, running for your life and sanity.\" The stranger smiles slightly at you, {character_creation.eye_color} orbs peering at you kindly.")

			cinematic_swell = misc_classes.Sound_effect("cinematic_swell", 7, "cinematic_swell_channel", 0, 0, 0)

			prompt = misc_classes.Text(f"\"Welcome, friend, to the Mirror.\" And with that, the stranger bursts into {character_creation.eye_color} flames, disappearing completely.")
			break

		case _:
			enter = input("Wrong input. Follow instructions.")


pygame.mixer.fadeout(2000)

prompt = misc_classes.Text("-")
prompt = misc_classes.Text("(END OF DEMO, \"The Knave\")")