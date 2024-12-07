import random

file = open("names.txt", "r")

selected_name = random.choice(file.readlines())

print(f"Randomly selected name: {selected_name}")