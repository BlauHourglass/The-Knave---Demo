import time
import pygame
import datetime
import character_creation
import misc_classes

# channel 0 = knave_st
# channel 1 = birds_chirping
# channel 2 = footsteps
# channel 3 = 
# channel 4 = piano_horror
# channel 5 = river
# channel 6 = sicilian_cafe
# channel 7 = cinematic_swell
current_time = datetime.datetime.now()

# initializing pygame module
pygame.init()
pygame.mixer.init()

try:
	Text = misc_classes.Text
	Music = misc_classes.Music
	SoundEffect = misc_classes.Sound_effect

	u_name = character_creation.u_name
	u_age = character_creation.u_age
	u_gender = character_creation.u_gender
	u_hair_color = character_creation.u_hair_color
	u_eye_color = character_creation.u_eye_color

	c_name = character_creation.c_name
	c_age = character_creation.c_age
	c_hair_color = character_creation.c_hair_color
	c_eye_color = character_creation.c_eye_color
	c_gender = character_creation.c_gender

	user_p_p = character_creation.user_p_p
	user_p = character_creation.user_p
	user_a_p = character_creation.user_a_p
	user_s_p = character_creation.user_s_p

	c_p_p = character_creation.c_p_p
	c_p = character_creation.c_p
	c_a_p = character_creation.c_a_p
	c_s_p = character_creation.c_s_p
	c_hearts = character_creation.c_hearts
except:
	pass

try:
	# "backstory" to demo
	Text("(PRESS ENTER TO CONTINUE AFTER EACH LINE)")
	Text("...")
	Text("You lazily slink to your bed, tossing your jacket onto your desk in the process. You slide under the covers, taking a deep breath.")
	Text("It has been a crazy long day, and all you need is a good night's rest. You close your eyes, letting exhaustion finally take a grasp of your body and mind, and you finally fall asleep.")
	Text("...")
	Text("\"...will no...ive...\"")
	Text("...")
	Text("\"...at's...ough...!\"")
	Text("...")
	Text("\"Welco...avel...\"")
	Text("...")
	Text("\"...Our finest Knave...\"")
	Text("...")
	Text(f"\"Arise, {u_name}, arise!\"")
	Text(f"...")

	# knave opening soundtrack
	knave_st = Music("knave_st", 0, "knave_st_channel", -1, 0, 0)

	# birds chirping
	birds_chirping = SoundEffect("birds_chirping", 1, "birds_chirping_channel", -1, 0, 0)


	# forest path scene
	Text(f"You wake up, blinking wearily in the glaring sunshine.")
	Text(f"The cheery chirping of birds reaches your ears, and you look around, bewildered and hurting.")
	Text(f"\"What in the world? Wh-where am I...?\" you mutter, looking closely at your hands.")
	Text(f"You are wearing tattered white bandages around your wrists and knuckles and tan pants tucked into leather boots. You are also wearing a dark leather tunic that is partially tucked into your belt. The collar is open down to your abdomen, displaying a worn white shirt and a silver chain necklace.")
	Text(f"\"My head hurts,\" you murmur, barely audible even to yourself. Your throat is parched and dry, and you feel as if your head has been socked by a sledgehammer. Perhaps you should find some water and then figure out where you are.")
	Text(f"You sit up and hesitantly touch your head. It really, really hurts. Perhaps there is a cut?")
	Text(f"You give a slight hiss as your fingers graze over a large bump and cut on the back of your head. It throbs, and you realize that it is the largest source of your headache. Dehydration is probably the other cause.")
	Text(f"\"Man, what happened...?\" you ask quietly to no one in particular. You stand up shakily. Your limbs and body feel sore all over, and your head hurts even more when you try to think back to... anything. You only recall the faint image of a pale face.")

	# footsteps-walking
	footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 2000, 1000)

	Text(f"You walk onto the dirt path, looking both ways. Both are shrouded by the tree limbs and foliage from both sides of the path. Thankfully, however, the sunlight is able to filter through the leaves and shine upon the path and grass in splotchy patches.")



	# first choice: right or left, ends the same route
	while True:
		print(f"Which way do you go?")
		l_or_r = input("1: Right\n2: Left\n")

		match l_or_r:
			case "1":
				footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 0, 1000)
				Text(f"Your gut tells you to go right, and so you turn in that direction, hoping that it brings you closer to water and, perhaps, a village where you can heal your wounds.")
				break
			case "2":
				footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 0, 1000)
				Text(f"You decide to go left and stagger along the dirt path, silently hoping for fresh water and an answer.")
				break
			case _:
				Text(f"Wrong input. Follow instructions.")

	birds_chirping.fade_out(2000)

	knave_st.fade_out(2000)

	# piano horror
	piano_horror = Music("piano_horror", 4, "piano_horror_channel", -1, 0, 4000)

	Text(f"As you walk on, you notice the birds' chirping slowly fading away, and an eerie feeling starts to set in.")

	Text(f"You quicken your pace, but your weakened body and dehydrated state hinder your progress.")
	Text("If anything, the forest is beautiful, but the diminishing sunshine and your growing unease make it difficult to fully appreciate its beauty. The pain, exhaustion, and overall discomfort further dampen your experience.")
	Text(f"\"Where am I, still...?\" you grumble, trying not to be bothered by the growing shadows around you.")

	# # river sounds
	river = SoundEffect("river", 5, "river_channel", -1, 0, 0)
	river.set__volume(0.1)

	Text(f"You continue to walk until you faintly hear the sound of rushing water. Immediately, you feel relieved, and you hurry on. Water — finally!")

	# # extra sound effect changing for experience
	river.set__volume(0.2)

	# # Water is reached, but stranger is sitting on the bank
	Text(f"You run on until you see a river flowing and dashing across rocks and boulders. It is nestled in the forest, creating enough space between the trees to allow a significant amount of light to shine down upon its face.")

	piano_horror.fade_out(6000)
	footsteps.fade_out(2000)

	Text("You also feel all of the shadows and eeriness fade away from around you, though there are still no birds to be seen or heard.")
	Text(f"You are about to go forward and drink, but you see a person sitting on the bank on a boulder, swinging {c_p_p.lower()} shoed foot against the face of the waters and splashing the water.")


	while True:
		print(f"Do you approach the stranger, wait until {c_p.lower()} leaves, or just ignore {c_a_p.lower()} and access the water?")
		demo_stranger_choice = input("1: Approach\n2: Wait\n3: Ignore\n")

		match demo_stranger_choice:
			case "1":
				# friendly and mysterious companion, plus heart points, probably too ru-ish 😭
				
				knave_st.fade_out(2000)

				sicilian_cafe = Music("sicilian_cafe", 6, "sicilian_cafe_channel", -1, 0, 0)

				footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 3000, 1000)

				Text(f"After a moment of consideration, you stagger over to the stranger. \"E-excuse me,\" you say, barely audible, and {c_p.lower()} turns, turning {c_eye_color} eyes upon you.")
				Text(f"\"Yes? Can I help you? You look quite haggard,\" {c_p.lower()} hums, ceasing {c_p_p.lower()} foot from swinging. {c_p} brings it up to rest on the dry bank, gazing up at you expectantly.")
				Text(f"You reflexively reach up to hold your head, feeling a sudden shock of pain shoot through your ugly welt. You wince visibly, but you try to speak again. \"W-water,\" you manage.")
				footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 5000, 2000)
				Text(f"The stranger blinks before giving a short sigh. \"That's obvious,\" {c_p.lower()} mutters, rising to {c_p_p.lower()} feet. {c_p} hastens to your side and helps you hobble to the side of the river.")
				Text(f"{c_p} lowers you gently to the water's edge and supports you while you take a refreshing drink.")
				Text(f"Relief and vigor surges through your body as you take another drink, and the stranger laughs. \"One would think you were starved from water for days if they saw you drinking like this,\" {c_p.lower()} grins.")
				Text(f"Despite your slight annoyance at {c_p_p.lower()} laughter and teasing about your horrible condition, you can't help but feel very grateful as you dip your stinging hands once more into the rushing water.")
				Text(f"\"Y-yeah, I guess so,\" you reply, taking your fifth swig before leaning back slightly. Even though the water is terribly refreshing and re-energizing, you still feel weak from dehydration.")
				Text(f"{c_p} looks at you carefully, anaylzing your countenance before silently taking {c_p_p.lower()} pouch from {c_p_p.lower()} hip and unlacing the lid.")
				Text(f"\"Well, traveler, you're in luck today,\" {c_p.lower()} muses, taking out a bandage and soaking it in the water. You glance at {c_a_p.lower()}, watching {c_p_p.lower()} hands wring out the cloth.")
				Text(f"You think about it a moment before nodding slowly and raising a hand to your cut. \"Considering you graciously helped me get water and quench my thirst, I suppose I am. For which I thank you for,\" you say. You watch as the stranger takes the wrap and gently applies it to your wound.")
				c_hearts + 10
				Text(f"\"No need to thank me, friend. But not only that, had you gotten here any sooner, you would've been swarmed by a group of bandits. And I daresay, you are in no position of taking them out,\" {c_p.lower()} hums.")
				Text(f"You pause, looking at {c_a_p.lower()} in slight bewilderment. No traces...anywhere...? \"Oh...you took them out?\"")
				Text(f"\"Well, yes. They were easy ruffians - just punks.\"")
				Text(f"You aren't sure how to feel, wondering who exactly this stranger is. {c_p} really must've done a good job taking out those thugs. But where are the bodies? A quick glance proves that a scuffle had ensued, but no bodies... Did {c_p.lower()} throw them down the river? Well, nevermind that for now - maybe {c_p.lower()} can tell you where you were.")
				Text(f"\"Where am I?\" you finally ask, trying to ignore the throbbing of your head.")
				Text(f"{c_p} gives a slight smile, turning {c_p_p.lower()} eyes to the sky. \"You don't know, hm? Well, you're in the world where nothing makes sense and the more you think of it, the less you know.\"")
				Text(f"{c_p} leans towards you slightly, looking at you with a sly look in {c_p_p.lower()} {c_eye_color} orbs. \"A world where you are nothing but a pawn - nay, a dustspeck on the chessboard.\"")
				
				cinematic_swell = SoundEffect("cinematic_swell", 7, "cinematic_swell_channel", 0, 0, 0)

				Text(f"\"Welcome, my friend, to the Mirror!\" And with that, {c_p.lower()} gives a light laugh and disappears in {c_eye_color} wisps.")
				break

			case "2":
				# rather disinterested and nonchalant companion, less heart points
				knave_st.fade_out(2000)
				
				sicilian_cafe = Music("sicilian_cafe", 6, "sicilian_cafe_channel", -1, 0, 0)

				Text(f"You hesitate a moment before squatting down on the ground and trying to nurse your headache. However, the stranger doesn't seem like {c_p.lower()} is going to leave, so you wait in silent agony.")
				Text(f"One minute passes by.")
				Text(f"Two minutes pass by.")
				Text(f"Three minutes pass by...")
				Text(f"...And all throughout, the stranger never turns or even moves from {c_p_p.lower()} position.")
				Text(f"It seems like an eternity before {c_p.lower()} actually changes {c_p_p.lower()} position, tilting {c_p_p.lower()} head back slightly. \"Well, it seems like we have quite the visitor. Care to introduce yourself, rude one?\" {c_p.lower()} says, turning around slightly to peer through {c_eye_color} eyes at you.")
				Text(f"You feel your cheeks redden and you internally slap yourself. Of course you'll seem like a wierdo, just watching and waiting. Also stupid. Also - wait, how does {c_p.lower()} know that you were even there?")
				c_hearts - 10
				Text(f"\"Rude and dumb too, I suppose,\" the stranger comments dryly. {c_p} sighs and stretches {c_p_p.lower()} arms above {c_p_p.lower()} head.")
				Text(f"\"S-sorry, I just - can't speak v-very well,\" you manage, staggering to your feet and making your way to the waterside. You drop to your knee and dip your hands into the cold, rushing waves, feeling very embaressed. How a mere stranger could elict such mortification was new to you. Man.")
				Text(f"\"That's clear enough,\" the person scoffs, turning away. {c_p_p} {c_eye_color} orbs narrows as they pass over your form again.")
				Text(f"You silently gulp down the water, letting relief and energy surge through you. However, even with all that, you still feel extremely weary. After taking your sixth draught, you sit back and glance at your hands, wet with the water. \"Yeah, sorry about that,\" you say.")
				Text(f"The stranger waves {c_p_p.lower()} hand dismissively. \"I suppose don't worry about it.\" {c_p} stands up, rearranging {c_p_p.lower()} cuffs and beginning to walk away.")
				footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 5000, 0)
				Text(f"You realize that this person probably knows where you are, and maybe - well, should you get {c_p_p.lower()} name too? \"H-hey, before you go, where am I?\" you ask, turning around to look at the person.")
				Text(f"With a sigh, {c_p.lower()} pauses and turns around just enough to settle {c_p.lower()} {c_eye_color} orbs upon you, seemingly searching your very being.\"So you're also amnesiac, hm?\" {c_p.lower()} shoots with a not-so-kind laugh.")
				Text(f"\"Very well, stranger. You're in the world where absolutely nothing makes sense, and the more you think of it, the less your poor brain knows,\" {c_p.lower()} continues.")

				cinematic_swell = SoundEffect("cinematic_swell", 7, "cinematic_swell_channel", 0, 0, 0)

				Text(f"\"Welcome, traveler, to the Mirror.\" And with that, the person gives a slight smirk and disappears in a {c_eye_color} light.")
				break

			case "3":
				# kind and quiet companion, no change in hearts
				knave_st.fade_out(2000)
				
				sicilian_cafe = Music("sicilian_cafe", 6, "sicilian_cafe_channel", -1, 0, 0)

				footsteps = SoundEffect("footsteps", 2, "footsteps_channel", -1, 3000, 1000)

				Text(f"You blink before walking to the side of the river and ignoring the stranger completely. You walk upstream of {c_a_p.lower()}, crouching down by the rushing water.")
				Text(f"You slip off the bandages on your hands, glancing at the cuts and bruises lining your skin. Man, they look awful. They kinda sting too.")
				Text(f"You dip your hands into the frigid water, hissing under your breath at the sharp pain that spreads over your hands through the partially open wounds.")
				Text(f"You don't notice it, but the stranger has been watching you for the past minute and {c_p_p.lower()} foot has ceased to swing.")
				Text(f"\"Well, you don't look too good,\" {c_p.lower()} murmurs after another moment passes, sliding off of the boulder and walking over to you. \"Tell me - do you need help?\" Looking up, you see {c_eye_color} eyes gaze down at you, a bit of sympathy nestled deep within.")
				Text(f"\"Yeah, sure. That'll actually be great,\" you mutter. Your parched throat hurts as you speak, and you hesitantly take a drink from the river.")
				Text(f"{c_p} lowers {c_s_p.lower()} to your side, pulling out a leather pouch from {c_p_p.lower()} side. {c_p} unlaces the cover and pulls out a white, clean bandage while you continue to drink.")
				Text(f"The stranger hums quietly as {c_p.lower()} dips the cloth into the water and squeezes it of its excess water, gesturing towards your head.")
				Text(f"\"Allow me,\" {c_p.lower()} says, and you glance at {c_a_p.lower()} for a gauging moment before nodding slowly.")
				Text(f"The person gently mops up the blood from your wound, washing it out once more(downstream of where you were drinking) and then wrapping it around your crown. \"What befell you, traveler?\" {c_p.lower()} questions, looking at you curiously.")
				Text(f"You shrug, taking your fourth drink of the water and leaning back slightly. \"I'm not sure,\" you reply, smiling ironically. \"Thanks for the help, though,\" you add.")
				Text(f"The stranger nods, closing the pouch and straightening up. \"Of course - I saw your plight and wished to help. But how do you not know what happened? Where you ambushed?\"")
				Text(f"You shrug again, taking your eyes off of the stranger and touching your head. \"I don't know. I don't even know where I am.\" You pause, thinking. But before you can say anything, the stranger speaks up again, an amused ring in {c_p_p.lower()} voice.")
				Text(f"\"In that case, traveler, then I welcome you to the world of confusion and puzzles. A world where you're constantly in a race through a labyrinth, running for your life and sanity.\" The stranger smiles slightly at you, {c_eye_color} orbs peering at you kindly.")

				cinematic_swell = SoundEffect("cinematic_swell", 7, "cinematic_swell_channel", 0, 0, 0)

				Text(f"\"Welcome, friend, to the Mirror.\" And with that, the stranger bursts into {c_eye_color} flames, disappearing completely.")
				break

			case _:
				enter = input("Wrong input. Follow instructions.")


	pygame.mixer.fadeout(2000)

	Text("-")
	Text("(END OF DEMO, \"The Knave\")")
	time.sleep(1)

except Exception as e:
	try:
		error_log = open("error_log.txt", "a")
		error_log.close()
	except:
		error_log = open("error_log.txt", "x")
		error_log.close()
	with open("error_log.txt", "a") as error_log:
		error_log.write(f"{current_time}: Main Script: {e}\n")
	error_message = input("\nSomething has gone wrong with the main program. Please press \"enter\" to quit.")

except KeyboardInterrupt:
	try:
		error_log = open("error_log.txt", "a")
		error_log.close()
	except:
		error_log = open("error_log.txt", "x")
		error_log.close()
	with open("error_log.txt", "a") as error_log:
		error_log.write(f"{current_time}: Main Script: User has interrupted program with a keyboard shortcut.\n")
	error_message = input("\nSomething has gone wrong with the main program. Please press \"enter\" to quit.")

exit()