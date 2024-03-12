import keyboard
import os
import pymem
import time
from offsets import *


handle = False
pmprocess = None

while not handle:
    try:
        pmprocess = pymem.Pymem('csgo.exe')
        handle = True
    except pymem.exception.ProcessNotFound:
        os.system("cls")
        print("Ожидание запуска процесса csgo.exe")
        time.sleep(0.3)


client_dll = pymem.process.module_from_name(pmprocess.process_handle, "client.dll")
if client_dll is not None:
    client_dll = client_dll.lpBaseOfDll

    os.system("cls")
    print("BigBunny работает.")

    while True:
        local_player = pmprocess.read_int(client_dll + dw_local_player)
        if keyboard.is_pressed('space'):
            force_jump = client_dll + dw_force_jump
            if local_player:
                player_on_ground = pmprocess.read_int(local_player + m_fFlags)
                if player_on_ground and player_on_ground in [257, 263]:
                    pmprocess.write_int(force_jump, 5)
                    time.sleep(0.02)
                    pmprocess.write_int(force_jump, 4)
        time.sleep(0.004)



