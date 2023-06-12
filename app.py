"""

APP GUI Main interface

LukeLab, 05/2023

"""

import tkinter as tk
from pathlib import Path

from tkinter import Tk, Canvas, Entry, PhotoImage

from gui.gui_0_DashboardLogin.DashboardLogin import DashboardLogin


# import gui frame classes:
# from gui.gui_0_DashboardLogin.DashboardLogin import DashboardLogin
# from gui.gui_1_DashboardLogged.DashboardLogged import DashboardLogged
# from gui.gui_2_StrategyMonitor.StrategyMonitor import StrategyMonitor
# from gui.gui_3_TreaderProfile.TreaderProfile import TreaderProfile
# from gui.gui_4_TradingList.TradingList import TradingList
# from gui.gui_5_Performance.Performance import Performance
# from gui.gui_6_APPLog.APPLog import APPLog
# from gui.gui_7_Message.Message import Message
# from gui.gui_8_DownloadData.DownloadData import DownloadData
# from gui.gui_9_SaveExit.SaveExit import SaveExit


class TradingApp:
    def __init__(self, *args, **kwargs):
        # init app window
        self.window = tk.Tk()

        # set app icon
        icon_photo = PhotoImage(file="gui/icon.png")
        self.window.iconphoto(False, icon_photo)

        # set app window size
        self.window.geometry("1096x728+50+50")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Program Trading Based on Webull")
        self.window.resizable(False, False)

        # set frame 0, DashboardLogin
        self.frame_0 = DashboardLogin(self)


if __name__ == "__main__":
    app = TradingApp()
    app.window.mainloop()
