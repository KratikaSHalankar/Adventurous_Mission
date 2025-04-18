from playsound import playsound
import random

def play_sound(file):
    """Play a sound file from the specified location."""
    # Change this path to where your sound files are stored
    playsound(f"C:/Users/krati/OneDrive/Desktop/PY_mini/MINI_PROJECTS/{file}")

def haunted_mansion():
    """Start the haunted house adventure game."""
    print("\n🏰 Welcome to Ravenwood Manor!")
    play_sound("Thunder.mp3")  

    print("\n🌫️ It's windy and thunder rumbles in the sky.")
    print("You find yourself on the dusty floor of a big, old house.")
    print("The doors behind you are locked tight.")
    print("The paintings on the walls seem to be watching you.")
    print("The clock is ticking, but its hands don't move.")

    print("\n🎭 You hear a voice saying: 'Choose carefully... not all choices lead to safety.'")
    print("\nWhat do you want to do?")
    
    # Using if/elif statements instead of dictionaries
    choice = input("1. Look around the study 📜\n2. Go into the dark hallway 🚶\n3. Go up to the attic 🏚️\n\nType your choice (1, 2, or 3): ")
    
    if choice == "1":
        study()
    elif choice == "2":
        hallway()
    elif choice == "3":
        Top_room()
    else:
        invalid_choice()

def invalid_choice():
    """Handle incorrect user inputs."""
    print("\n❌ That's not a valid choice! Try again...")
    haunted_mansion()

def study():
    """Player explores the study room."""
    print("\n📜 You open the study doors. The room feels cold.")
    print("There are books on shelves and a big desk in the middle of the room.")

    sub_choice = input("\nWhat would you like to do?\n1. Read the book on the desk 📖\n2. Look inside the desk drawers 🔑\n\nType your choice (1 or 2): ")
    
    if sub_choice == "1":
        print("\n⚠️ The book says: 'No one ever leaves this house.'")
        puzzle_riddles()
    elif sub_choice == "2":
        print("\n🔑 You found a small iron key. It might be useful later.")
        hallway()
    else:
        print("\n❌ That's not a valid choice. Try again.")
        study()

def hallway():
    """Player enters the hallway."""
    play_sound("footsteps.mp3")  
    print("\n🚶 You're now in a long hallway. You feel like something is watching you.")
    
    choice = input("\nWhat would you like to do?\n1. Look at the painting on the wall 🎨\n2. Go down to the basement 🕳️\n3. Open a small box with puzzles 🧩\n4. Try to solve a hidden riddle 🔮\n\nType your choice (1, 2, 3, or 4): ")
    
    # Using if/elif statements instead of dictionary
    if choice == "1":
        painting()
    elif choice == "2":
        basement()
    elif choice == "3":
        puzzle_box()
    elif choice == "4":
        puzzle_riddles()
    else:
        print("\n❌ That's not a valid choice. Try again.")
        hallway()

def painting():
    """Player examines the painting."""
    print("\n👁️ The eyes in the painting blink! You hear whispers around you...")
    play_sound("whispers.mp3")
    puzzle_riddles()

def Top_room():
    """Player explores the attic."""
    play_sound("door_creak.mp3")
    print("\n🏚️ You slowly open the attic door. The air is dusty.")
    print("There's a rocking chair moving by itself - nobody is sitting in it!")
    
    choice = input("\nWhat would you like to do?\n1. Open the old trunk in the corner 📦\n2. Look in the mirror on the wall 🪞\n3. Leave the attic 🚪\n\nType your choice (1, 2, or 3): ")

    if choice == "1":
        print("\n📦 You found a diary that warns about a secret in the house.")
        puzzle_riddles()
    elif choice == "2":
        play_sound("mirror_crack.mp3")
        print("\n🪞 The mirror cracks and you see a hidden box behind it!")
        puzzle_box()
    elif choice == "3":
        hallway()
    else:
        print("\n❌ That's not a valid choice. Try again.")
        Top_room()

def puzzle_riddles():
    """ Player solves riddles. Must answer all correctly to move forward. """
    riddles = [
        {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
        {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
        {"question": "I am always running but never move. What am I?", "answer": "clock"},
        {"question": "I have cities but no houses, forests but no trees, and rivers but no water. What am I?", "answer": "map"},
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "What has words but never speaks?", "answer": "book"},
        {"question": "What begins with T, ends with T, and has T in it?", "answer": "teapot"},
        {"question": "I am not alive, but I grow. I don’t have lungs, but I need air. What am I?", "answer": "fire"},
        {"question": "The more you have of me, the less you see. What am I?", "answer": "darkness"},
        
    ]

    for riddle in riddles:
        print(f"\n📜 A puzzle appears: '{riddle['question']}'")
        answer = input("\nEnter your answer: ").lower()

        if answer == riddle["answer"]:
            print("\n✅ Correct! The shadows retreat...")
        else:
            print("\n❌ Wrong answer! Try again.")
            return bad_ending()

    print("\n🎭 You solved all riddles! A hidden path appears...")
    final_encounter()

def puzzle_box():
    """Player finds a puzzle box."""
    print("\n🧩 You found an old box with strange symbols on it.")
    choice = input("\nWhat would you like to do?\n1. Try to open it 🔓\n2. Leave it alone 🚶\n\nType your choice (1 or 2): ")

    if choice == "1":
        print("\n🔮 You managed to open the box! Inside is a map showing a secret way out.")
        escape_ending()
    else:
        hallway()

def basement():
    """Player explores the basement."""
    print("\n🕳️ The basement is cold and wet. There's a strange door in front of you.")
    
    print("\n🔒 To open the door, you need to solve this riddle:")
    print("'What walks on four legs in the morning, two legs in the afternoon, and three legs at night?'")
    answer = input("\nType your answer: ").lower()

    if answer == "human" or answer == "person" or answer == "man":
        print("\n✅ That's correct! The door opens and you find a secret tunnel.")
        escape_ending()
    else:
        print("\n❌ That's not right! The door won't open.")
        bad_ending()

def final_encounter():
    """The final challenge before escaping."""
    print("\n🩸 You see a dark shadow blocking the exit door.")
    choice = input("\nWhat will you do?\n1. Run quickly through the door 🚪\n2. Try to talk to the shadow 💀\n\nType your choice (1 or 2): ")

    if choice == "1":
        escape_ending()
    else:
        play_sound("scream.mp3")
        bad_ending()

def escape_ending():
    """Player successfully escapes - winning ending."""
    print("\n🔥 You made it out just as the clock strikes twelve!")
    play_sound("whispers.mp3")
    print("\n🎮 Congratulations! You survived the haunted house!")
    print("Thanks for playing!")

def bad_ending():
    """Player fails to escape - losing ending."""
    print("\n🕛 The clock strikes midnight and the whole house shakes.")
    play_sound("laugh.mp3")
    print("\n💀 You are now trapped in Ravenwood Manor forever!")
    print("Game over! Try again?")

# Start the game when the program runs
haunted_mansion()