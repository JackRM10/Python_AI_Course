def show_intro():
    print("Welcome to the Philosopher's Stone Adventure!")
    print("You are Harry Potter, trying to reach the Philosopher's Stone.")
    print("You are in Hogwarts and need to make choices to get past the obstacles.")
    print("You can go left to Fluffy, go right to the Devil's Snare, or go straight ahead to the flying keys.")

def make_choice():
    choice = input("Where would you like to go? (left/right/straight): ").lower()
    return choice

def left_path():
    print("\nYou chose to go left. You encounter Fluffy, the giant three-headed dog!")
    action = input("Do you play music to calm him or try to sneak past? (play/sneak): ").lower()
    if action == "play":
        print("You play music, and Fluffy falls asleep. You pass safely to the next challenge: the giant chessboard.")
        chess_room()
    else:
        print("Fluffy notices you and starts barking. You run back in fear. Game over!")

def right_path():
    print("\nYou chose to go right. You find yourself entangled in the Devil's Snare!")
    action = input("Do you relax to escape or struggle? (relax/struggle): ").lower()
    if action == "relax":
        print("You relax, and the Devil's Snare loosens its grip. You escape safely and move to the room with the potions.")
        potions_room()
    else:
        print("You struggle, and the Devil's Snare tightens. You are trapped. Game over!")

def straight_path():
    print("\nYou chose to go straight. You reach the room with enchanted flying keys.")
    action = input("Do you use a broomstick to catch the key or try to reach it by jumping? (broom/jump): ").lower()
    if action == "broom":
        print("You mount the broomstick, chase the key, and catch it! You unlock the door and move ahead to the potions room.")
        potions_room()
    elif action == "jump":
        print("You try to jump but can't reach the key. The enchanted keys swarm and push you back. Game over!")
    else:
        print("Invalid choice. The keys swarm you, and you retreat. Game over!")

def chess_room():
    print("\nYou are in the room with the giant chessboard. You must play to proceed.")
    action = input("Do you play as a knight or a bishop? (knight/bishop): ").lower()
    if action == "knight":
        print("You play as a knight, moving strategically. Your side wins, and you move on to the potion room.")
        potions_room()
    elif action == "bishop":
        print("You play as a bishop but are trapped in a checkmate. Game over!")
    else:
        print("Invalid choice. The chess pieces turn on you. Game over!")

def potions_room():
    print("\nYou enter the room with a table full of potions and a riddle to solve.")
    action = input("Do you take the potion on the left (safe) or the one on the right (risky)? (left/right): ").lower()
    if action == "left":
        print("You drink the safe potion and feel a sense of calm. You move on to the final room: the Mirror of Erised.")
        mirror_room()
    elif action == "right":
        print("You drink the risky potion, but it was poison. Game over!")
    else:
        print("Invalid choice. The potions disappear before you can act. Game over!")

def mirror_room():
    print("\nYou stand before the Mirror of Erised, and you see yourself holding the Philosopher's Stone.")
    action = input("Do you reach out to take the stone or wait and watch? (take/wait): ").lower()
    if action == "wait":
        print("You realize that only by wanting to find the stone without using it will it appear. The stone appears in your pocket.")
        print("But suddenly, Professor Quirrell enters the room.")
        quirrell_fight()
    elif action == "take":
        print("Quirrell sees you try to grab the stone and attacks. Game over!")
    else:
        print("Invalid choice. The mirror clouds over, and you lose your chance. Game over!")

def quirrell_fight():
    print("\nQuirrell reveals himself as Voldemort's servant and tries to take the stone from you.")
    action = input("Do you fight Quirrell directly or try to stall him by talking? (fight/talk): ").lower()
    if action == "fight":
        print("You touch Quirrell's skin, and it burns him! He screams in pain, but Voldemort's spirit escapes.")
        print("You pass out from exhaustion.")
        hospital_wing()
    elif action == "talk":
        print("Quirrell becomes impatient, and Voldemort orders him to take the stone by force. You lose. Game over!")
    else:
        print("Invalid choice. Quirrell seizes the opportunity and attacks. Game over!")

def hospital_wing():
    print("\nYou wake up in the hospital wing, sunlight streaming through the windows.")
    print("Professor Dumbledore is sitting beside you, smiling.")
    print("\"Ah, Harry, you did very well,\" he says. \"The stone is safe, and Voldemort has been thwarted, for now.\"")
    print("You smile, feeling relief wash over you.")
    print("Congratulations! You have completed the adventure!")

def play_game():
    show_intro()
    choice = make_choice()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "straight":
        straight_path()
    else:
        print("\nInvalid choice. You hesitate and lose your chance. Game over!")

# Start the game
play_game()
