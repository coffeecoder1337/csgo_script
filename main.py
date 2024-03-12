from bs4 import BeautifulSoup as BS
from design import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import json
import keyboard
import pymem
import requests
import time
import threading
import sys



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.run = False
        self.clicked = False
        self.pm = None
        self.setupUi(self)
        self.check_update()
        self.offsets = self.get_offests()
        self.pushButton.clicked.connect(self.test)


    def check_update(self):
        self.label.setText("Проверка обновлений cs:go")
        page = requests.get("https://github.com/frk1/hazedumper/blob/master/csgo.hpp").content
        bs = BS(page, 'lxml')
        tds = bs.find_all('td', class_="blob-code-inner")
        signatures = dict()
        for td in tds:
            signature = td.text.split()
            if len(signature) == 5:
                signatures[signature[2]] = int(signature[4][:-1], 16)
        with open("offsets.json", "w") as f:    
            json.dump(signatures, f, indent=4)
        self.label.setText("Данные обновлены")


    def get_offests(self):
        with open("offsets.json", "r") as f:
            return json.load(f)


    # def start(self):
    #     self.pushButton.setText(u"остановить")
    #     self.clicked = True
    #     self.inject()
    #     print("started")


    # def stop(self):
    #     self.pushButton.setText(u"начать")
    #     self.clicked = False
    #     self.run = False
    #     self.pm = None
    #     print("stopped")
    #     self.label.setText(u"Выключено")


    def test(self):
        if not self.clicked:
            self.pushButton.setText(u"остановить")
            self.clicked = True
            self.run = True
            self.inject()
            print("started")
            return

        if self.clicked:
            self.pushButton.setText(u"начать")
            self.clicked = False
            self.run = False
            self.pm = None
            print("stopped")
            self.label.setText(u"Выключено")
            return


    def bhop(self):
        if keyboard.is_pressed('space'):
            force_jump = self.clientdll + self.offsets['dwForceJump']
            if self.local_player:
                on_ground = self.pm.read_int(self.local_player + self.offsets['m_fFlags'])
                if on_ground and on_ground in [257, 263]:
                    self.pm.write_int(force_jump, 5)
                    time.sleep(0.04)
                    self.pm.write_int(force_jump, 4)


    def wallhack(self):
        for i in range(1, 64):
            entity = self.pm.read_int(self.clientdll + self.offsets['dwEntityList'] + i * 0x10)
            # print(self.offsets['dwEntityList'])
            # print(pm.read_int(entity + m_iHealth))
            if entity:
                team_id = self.pm.read_int(entity + self.offsets['m_iTeamNum'])
                #team_id = None
                entity_glow = self.pm.read_int(entity + self.offsets['m_iGlowIndex'])
                if team_id:
                    if team_id == self.local_team:

                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0x4, float(0)) # red
                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0x8, float(1)) # green
                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0xC, float(0)) # blue
                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0x10, float(1)) # alpha
                        self.pm.write_int(self.glow_manager + entity_glow * 0x38 + 0x24, 1) # enable/disable (1/0)
                
                    else:
                        # entity_glow = pm.read_int(entity + glow_index)

                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0x4, float(1)) # red
                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0x8, float(0)) # green
                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0xC, float(0)) # blue
                        self.pm.write_float(self.glow_manager + entity_glow * 0x38 + 0x10, float(1)) # alpha
                        self.pm.write_int(self.glow_manager + entity_glow * 0x38 + 0x24, 1) # enable/disable (1/0)


    def inject(self):
        if self.pm is None:
            try:
                self.pm = pymem.Pymem("csgo.exe")
                print("handle csgo.exe")
                self.clientdll = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
                print("handle client.dll")
            except:
                # self.stop()
                self.label.setText(u"Запустите csgo и повторите попытку")
            else:
                # self.start()
                self.label.setText(u"Успешно")
        self.thread = threading.Thread(target=self.loop)
        self.thread.setDaemon(True)
        self.thread.start()

    def loop(self):
        while self.run:
            try:
                self.local_player = self.pm.read_int(self.clientdll + self.offsets['dwLocalPlayer'])
                self.glow_manager = self.pm.read_int(self.clientdll + self.offsets['dwGlowObjectManager'])
                self.local_team = self.pm.read_int(self.local_player + self.offsets['m_iTeamNum'])

                self.bhop()
                self.wallhack()  

                time.sleep(0.002)
            except:
                pass

    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
    # window.thread.join()

