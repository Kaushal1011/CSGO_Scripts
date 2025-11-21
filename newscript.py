'''
Mostly Scripts Related to CSGO such as Auto Trigger and Bee Hopping

Do not use these while playing competitive matches or do but at your own risk.
You can get VAC Banned from using this.
This was made for learning and fun purposes only :D

author: Kaushal Patil
'''

import time

import keyboard
import pyautogui
import pymem
import pymem.process

# Memory addresses for CSGO (Note: These may be outdated and require updating)
dwEntityList = (0x4D04B04)
dwForceAttack = (0x313618C)
dwLocalPlayer = (0xCF2A3C)
m_fFlags = (0x104)
m_iCrosshairId = (0xB3AC)
m_iTeamNum = (0xF4)

try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle,
                                            "client_panorama.dll").lpBaseOfDll
except Exception as e:
    print(f"Error: Could not attach to CSGO process. {e}")
    print("Make sure CSGO is running.")
    exit(1)


def main():
    while True:
        try:
            player = pm.read_int(client + dwLocalPlayer)

            entity = pm.read_int(player + m_iCrosshairId)

            if entity > 0 and entity <= 64:
                entity = pm.read_int(client + dwEntityList + (entity - 1) * 0x10)
                entity_team = pm.read_int(entity + m_iTeamNum)
                player_team = pm.read_int(player + m_iTeamNum)

                if player_team != entity_team:
                    if keyboard.is_pressed("shift") or keyboard.is_pressed(
                            "ctrl") or (keyboard.is_pressed("a")
                                         and keyboard.is_pressed("d")):
                        pyautogui.click()
                        time.sleep(0.015)

            # Press ESC to exit the script
            if keyboard.is_pressed("esc"):
                print("Exiting script...")
                break

        except Exception as e:
            print(f"Error reading memory: {e}")
            print("CSGO process may have closed.")
            break

                # shooting = True
                # pm.write_int(client + dwForceAttack, 5)

        # if not keyboard.is_pressed(trigger_key) and shooting == True:
        #     pm.write_int(client + dwForceAttack, 4)
        #     shooting = False


if __name__ == '__main__':
    print("Trigger Bot Script Running")
    print("Press SHIFT/CTRL/A+D to trigger, ESC to exit")
    main()
