import random
import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load rarities and weights from JSON file
with open("rarities.json") as file:
    possible = json.load(file)

def roll():
    simulation = int(input("How many rolls? "))
    returns = random.choices(list(possible.keys()), weights=possible.values(), k=simulation)

    print("Rolled, counting...")

    # Count occurrences of each rarity
    counts = {rarity: returns.count(rarity) for rarity in possible.keys()}

    # Sort rarities by their weights to find the rarest drop
    sorted_rarities = sorted(possible.keys(), key=lambda k: possible[k])

    # Find the rarest drop
    rarest_drop = next((rarity for rarity in sorted_rarities if counts[rarity] > 0), None)

    clear()

    for rarity, count in counts.items():
        print(f"Counted {rarity}: {count}")
    
    if rarest_drop:
        print(f"Your rarest drop is: {rarest_drop}, with a rarity of {possible[rarest_drop]}!")
    else:
        print("No drops occurred.")

    input("Press enter to spin again, or type 'exit' to leave.")

def main():
    clear()
    print("Welcome to Gambling Sim 2")
    print("Press enter to spin, type 'exit' to leave.")
    
    while True:
        choice = input().strip().lower()
        if choice == 'exit':
            break
        clear()
        roll()
        clear()

if __name__ == "__main__":
    main()
