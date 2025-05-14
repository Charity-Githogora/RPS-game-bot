# main.py
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

# Playing the game against the bots
print("Playing against Quincy...")
play(player, quincy, 1000, verbose=True)

print("\nPlaying against Abbey...")
play(player, abbey, 1000, verbose=True)

print("\nPlaying against Kris...")
play(player, kris, 1000, verbose=True)

print("\nPlaying against Mrugesh...")
play(player, mrugesh, 1000, verbose=True)

# Uncomment below to play interactively
# Uncomment the following to play with the human bot:
# play(human, abbey, 20, verbose=True)

# Uncomment the following to play against a random player:
# play(human, random_player, 1000)
