import keyboard
import pymem
import pymem.process
import pyautogui
import time

dwEntityList = (0x4D04A74)
dwForceAttack = (0x313618C)
dwLocalPlayer = (0xCF2A3C)
m_fFlags = (0x104)
m_iCrosshairId = (0xB3AC)
m_iTeamNum = (0xF4)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll


def main():
    
    while True:
        player = pm.read_int(client + dwLocalPlayer)

        
        entity = pm.read_int(player + m_iCrosshairId)
        
             
       
        if entity > 0 and entity <= 64:
            entity = pm.read_int(client + dwEntityList + (entity -1) * 0x10)
            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)
                    
            if player_team != entity_team:
                if keyboard.is_pressed("left shift") or keyboard.is_pressed("left ctrl") or(keyboard.is_pressed("a") and keyboard.is_pressed("d")):
                    pyautogui.click()
                    time.sleep(0.015)
                    

                # shooting = True
                # pm.write_int(client + dwForceAttack, 5)
        
            
        # if not keyboard.is_pressed(trigger_key) and shooting == True:
        #     pm.write_int(client + dwForceAttack, 4)
        #     shooting = False

def a():
    main()

if __name__ == '__main__':
    a()

    
            
            
