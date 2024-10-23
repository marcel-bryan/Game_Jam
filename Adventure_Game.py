import random
from texttable import Texttable

# Display classes with stats and abilities
print("Welcome to Ascension")
print("You may choose from 1 of 3 classes to start your adventure")

table = Texttable()
table.add_rows([
    ["Class", "Warrior", "Rogue", "Wizard"],
    ["Level", "1", "1", "1"],
    ["Hp", "12", "9", "7"],
    ["Def", "3", "2", "1"],
    ["Pen", "0", "3", "2"],
    ["Abilities",
     "Slash - Deals 4 damage to the creature.\n"
     "Shield Bash - Deals 3 damage and has a 50% chance to stun.\n"
     "Cleave - Deals 3 damage to up to 3 creatures.",
     
     "Backstab - Deals 9 damage on the first attack (backstab). After that, deals 5 damage.\n"
     "Dagger Throw - Deals 7 damage on the first attack to up to 2 enemies. After that, deals 4 damage.",
     
     "Fireball - Deals 5 damage to up to 2 creatures.\n"
     "Wind Blade - Deals 4 damage to up to 3 creatures.\n"
     "Magic Missile - Deals 3 damage to up to 4 creatures."
    ]
])
print(table.draw())

print("Hp = Your total Health, determines how much damage you can take before death.")
print("Def = Your total Defense, reduces the damage you take.")
print("Pen = Penetration, reduces enemy's Defense.")

# Player chooses class
valid_classes = ["Warrior", "Rogue", "Wizard"]
player_class = ""

while player_class not in valid_classes:
    player_class = input("Choose your class (Warrior, Rogue, Wizard): ")

# Initialize player stats based on class
player_stats = {
    "Warrior": {"hp": 12, "def": 3, "pen": 0, "abilities": ["Slash", "Shield Bash", "Cleave"]},
    "Rogue": {"hp": 9, "def": 2, "pen": 3, "abilities": ["Backstab", "Dagger Throw"]},
    "Wizard": {"hp": 7, "def": 1, "pen": 2, "abilities": ["Fireball", "Wind Blade", "Magic Missile"]}
}

player_hp = player_stats[player_class]["hp"]
player_def = player_stats[player_class]["def"]
player_pen = player_stats[player_class]["pen"]

# Descriptions and locations with encounters
locations = {
    "1": {"description": "You enter the cave. The air is thick with mystery and an unnatural chill runs down your spine.", "encountered": False},
    "2": {"description": "As you venture deeper, a growl echoes through the shadows. Something is lurking...", "encountered": True},  # Encounter here
    "3": {"description": "You find yourself in a dimly lit chamber where shadows dance along the walls.", "encountered": True},  # Another encounter
    "4": {"description": "Ancient carvings tell stories of this place, revealing dark secrets long forgotten.", "encountered": False},
    "5": {"description": "Before you stands a statue, a grotesque figure that is half demon and half angel.", "encountered": False},
    "6": {"description": "More growls echo, and you prepare for another encounter!", "encountered": True},  # Encounter here
    "7": {"description": "The cave widens, filled with eerie silence and the distant sound of dripping water.", "encountered": False},
    "8": {"description": "A flicker of light catches your eye, revealing ancient treasure hidden away.", "encountered": False},
    "9": {"description": "The air grows colder as you step deeper into the darkness, senses heightened.", "encountered": True},  # Encounter here
    "10": {"description": "You find yourself in a massive cavern, the ceiling lost in darkness above.", "encountered": False},
    "11": {"description": "The cave seems to shift and change around you, an otherworldly presence felt.", "encountered": False},
    "12": {"description": "You feel the end of your journey approaching. Will you press on?", "encountered": False}  # Final room
}

# Player's current location and previous location tracking
current_location = "1"
explored = set()

# Function to create fresh monster instances
def get_monster_encounter():
    """Creates and returns a new set of monsters for the encounter."""
    return {
        "Orc": {"hp": 5, "damage": 3, "pen": 2, "def": 1},
        "Goblins": [{"hp": 3, "damage": 1, "pen": 3, "def": 0} for _ in range(3)],
        "Kobolds": [{"hp": 4, "damage": 2, "pen": 2, "def": 1} for _ in range(2)]
    }

# Exploration logic
def explore_cave():
    global current_location
    while current_location != "end":
        # Display the current room description
        print(locations[current_location]["description"])

        # Check if there is an encounter
        if locations[current_location]["encountered"]:
            monster_encounter()
        
        # Move to the next location
        next_move()

        # Mark the current location as explored
        explored.add(current_location)

# Next movement options
def next_move():
    global current_location

    # Allow only forward movement
    move = ""

    while move != "Forward":
        move = input("Which direction would you like to go (Forward): ").capitalize()

    # Update the current location to the next location
    if current_location == "1":
        current_location = "2"  # Move to the next room with an encounter
    elif current_location == "2":
        current_location = "3"  # Move to another encounter
    elif current_location == "3":
        current_location = "4"  # Move to the description room
    elif current_location == "4":
        current_location = "5"  # Move to the statue room
    elif current_location == "5":
        current_location = "6"  # Move to another encounter
    elif current_location == "6":
        current_location = "7"  # Move to a quiet room
    elif current_location == "7":
        current_location = "8"  # Move to treasure room
    elif current_location == "8":
        current_location = "9"  # Move to another encounter
    elif current_location == "9":
        current_location = "10"  # Move to a cavern
    elif current_location == "10":
        current_location = "11"  # Move to a mysterious room
    elif current_location == "11":
        current_location = "12"  # Move to the final room
    else:
        print("You've reached the end of your adventure. Thank you for playing!")
        exit()

# Combat encounters
def monster_encounter():
    print("You sense danger ahead. Suddenly, you come across a group of monsters!")

    # Get a fresh set of monsters for each encounter
    monsters = get_monster_encounter()
    monster_type = random.choice(list(monsters.keys()))
    
    if monster_type == "Orc":
        print(f"An Orc appears! It has {monsters['Orc']['hp']} HP and {monsters['Orc']['def']} defense.")
        combat([monsters['Orc']])
    elif monster_type == "Goblins":
        print(f"A group of 3 Goblins appear! Each has {monsters['Goblins'][0]['hp']} HP.")
        combat(monsters['Goblins'])
    elif monster_type == "Kobolds":
        print(f"A group of 2 Kobolds appear! Each has {monsters['Kobolds'][0]['hp']} HP.")
        combat(monsters['Kobolds'])

# Combat system
def combat(enemy_group):
    global player_hp
    print(f"Combat initiated with {len(enemy_group)} enemy(s)!")

    while player_hp > 0 and any(enemy["hp"] > 0 for enemy in enemy_group):
        # Player's turn to attack
        ability = input(f"Choose an ability to use ({', '.join(player_stats[player_class]['abilities'])}): ")

        if ability == "Cleave":
            print("You cleave at the enemies!")
            for i in range(min(3, len(enemy_group))):  # Hit up to 3 enemies
                if enemy_group[i]["hp"] > 0:  # Check if enemy is alive
                    damage = 3  # Cleave damage
                    enemy_group[i]["hp"] -= max(0, damage - enemy_group[i]["def"])
                    print(f"You deal {max(0, damage - enemy_group[i]['def'])} damage to enemy {i + 1}. Enemy HP: {enemy_group[i]['hp']}")
        else:
            damage = 0
            if player_class == "Wizard":
                if ability == "Fireball":
                    print("You cast Fireball!")
                    for i in range(min(2, len(enemy_group))):  # Hit up to 2 enemies
                        if enemy_group[i]["hp"] > 0:  # Check if enemy is alive
                            damage = 5  # Fireball damage
                            enemy_group[i]["hp"] -= max(0, damage - enemy_group[i]["def"])
                            print(f"You deal {max(0, damage - enemy_group[i]['def'])} damage to enemy {i + 1}. Enemy HP: {enemy_group[i]['hp']}")
                elif ability == "Wind Blade":
                    print("You cast Wind Blade!")
                    for i in range(min(3, len(enemy_group))):  # Hit up to 3 enemies
                        if enemy_group[i]["hp"] > 0:  # Check if enemy is alive
                            damage = 4  # Wind Blade damage
                            enemy_group[i]["hp"] -= max(0, damage - enemy_group[i]["def"])
                            print(f"You deal {max(0, damage - enemy_group[i]['def'])} damage to enemy {i + 1}. Enemy HP: {enemy_group[i]['hp']}")
                elif ability == "Magic Missile":
                    print("You cast Magic Missile!")
                    for i in range(min(4, len(enemy_group))):  # Hit up to 4 enemies
                        if enemy_group[i]["hp"] > 0:  # Check if enemy is alive
                            damage = 3  # Magic Missile damage
                            enemy_group[i]["hp"] -= max(0, damage - enemy_group[i]["def"])
                            print(f"You deal {max(0, damage - enemy_group[i]['def'])} damage to enemy {i + 1}. Enemy HP: {enemy_group[i]['hp']}")
            else:
                damage = 4 if ability == "Slash" else 3 if ability == "Shield Bash" else 0

                for enemy in enemy_group:  # Hit only the first enemy
                    if enemy["hp"] > 0:
                        enemy["hp"] -= max(0, damage - enemy["def"])
                        print(f"You deal {max(0, damage - enemy['def'])} damage to the enemy. Enemy HP: {enemy['hp']}")
                        break  # Exit after hitting one enemy

        # Enemy's turn to attack
        for enemy in enemy_group:
            if enemy["hp"] > 0:  # Only attack if still alive
                effective_defense = max(0, player_def - enemy["pen"])
                damage_taken = max(0, enemy["damage"] - effective_defense)
                player_hp -= damage_taken
                print(f"The enemy attacks! You take {damage_taken} damage. Your HP: {player_hp}")

    # End combat if player is defeated
    if player_hp <= 0:
        print("You have been defeated. Game Over.")
        exit()
    else:
        print("All enemies defeated! You can now proceed.")

# Start the exploration process
explore_cave()
