'''
Mostly Scripts Related to CSGO such as Auto Trigger and Bee Hopping

Do not use these while playing competative matchs or do but at your own risk.
You can get VAC Banned from using this.
This was made for learnig and fun purposes only :D

author: Kaushal Patil
'''



import keyboard
from time import sleep

def main():
    print("Press ESC to exit the script")
    while True:
        # Check for exit key
        if keyboard.is_pressed("esc"):
            print("Exiting script...")
            break

        # Main bhop logic
        if keyboard.is_pressed("left alt"):
            while True:
                keyboard.send("space")
                keyboard.send("a")
                keyboard.send("d")
                
                sleep(0.05)
                if not keyboard.is_pressed("left alt"):
                    break

        sleep(0.01)  # Small delay to prevent CPU overload

