import json

# Load dataset
with open("data/dataset.json", "r") as file:
    data = json.load(file)

# Print data
print("Missions:", data["missions"])
print("Satellites:", data["satellites"])
print("Resources:", data["resources"])
print("Time Window:", data["time_window"])

# Test success
print("Program ran successfully 🚀")
import json

# Load dataset
with open("data/dataset.json", "r") as file:
    data = json.load(file)

# Print data
print("Missions:", data["missions"])
print("Satellites:", data["satellites"])
print("Resources:", data["resources"])
print("Time Window:", data["time_window"])

# Test success
print("Program ran successfully 🚀")


# ==============================
# ADD YOUR CODE HERE 👇
# ==============================

# Simple assignment logic
print("\n--- Mission Assignment ---")

missions = data["missions"]
satellites = data["satellites"]

for mission in missions:
    assigned = False

    for sat in satellites:
        if sat["energy"] >= mission["duration"]:
            print(f"Mission {mission['id']} assigned to {sat['id']}")

            # 🔥 reduce energy
            sat["energy"] -= mission["duration"]

            assigned = True
            break

    if not assigned:
        print(f"Mission {mission['id']} could NOT be assigned")