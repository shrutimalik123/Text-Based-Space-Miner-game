import random

def space_miner():
    # 1. Initial State
    credits = 0
    hull_integrity = 100
    drill_power = 1
    fuel = 10
    
    print("--- 🚀 Deep Space Miner 🚀 ---")
    print("Mine minerals to earn 500 credits before your ship breaks!")

    while hull_integrity > 0 and credits < 500:
        print(f"\nCredits: {credits} | Hull: {hull_integrity}% | Fuel: {fuel}")
        action = input("Choose: [M]ine, [R]epair (20c), [U]pgrade Drill (50c), [Q]uit: ").lower().strip()

        if action == 'q':
            break

        # 2. Mining Logic (The Core Mechanic)
        if action == 'm':
            if fuel <= 0:
                print("⚠️ Out of fuel! You must rest to refuel.")
                fuel += 3
                continue
            
            fuel -= 1
            # Random chance of event
            event = random.random() # Generates a float between 0.0 and 1.0

            if event < 0.2: # 20% chance of an asteroid hit
                damage = random.randint(10, 25)
                hull_integrity -= damage
                print(f"💥 Collision! You hit an asteroid. -{damage}% Hull!")
            else:
                found = random.randint(10, 30) * drill_power
                credits += found
                print(f"💎 Success! You mined {found} credits worth of ore.")

        # 3. Repair and Upgrade Logic
        elif action == 'r':
            if credits >= 20:
                credits -= 20
                hull_integrity = min(100, hull_integrity + 30)
                print("🛠️ Hull repaired!")
            else:
                print("❌ Not enough credits!")

        elif action == 'u':
            if credits >= 50:
                credits -= 50
                drill_power += 1
                print(f"⚡ Drill upgraded! Current Power: {drill_power}")
            else:
                print("❌ Not enough credits!")
        
        else:
            print("Invalid input.")

    # 4. Endings
    if credits >= 500:
        print("\n🏆 MISSION COMPLETE! You've retired a wealthy miner.")
    elif hull_integrity <= 0:
        print("\n💀 SHIP DESTROYED! Your journey ends in the stardust.")

space_miner()
