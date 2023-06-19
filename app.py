"""

APP GUI Main interface

LukeLab, 05/2023

"""
import ctypes
import time
import tkinter as tk
from pathlib import Path

from tkinter import Tk, Canvas, Entry, PhotoImage
from tkinter import font as tkfont

from Trader import Trader
from gui.gui_0_DashboardLogin.DashboardLogin import DashboardLogin
from gui.gui_1_DashboardLogged.DashboardLogged import DashboardLogged
from gui.gui_2_StrategyMonitor.StrategyMonitor import StrategyMonitor
from gui.gui_3_TreaderProfile.TreaderProfile import TreaderProfile
from gui.gui_4_TradingList.TradingList import TradingList
from gui.gui_5_Performance.Performance import Performance
from gui.gui_6_APPLog.APPLog import APPLog
from gui.gui_7_Message.Message import Message
from gui.gui_8_DownloadData.DownloadData import DownloadData
from gui.gui_9_SaveExit.SaveExit import SaveExit


class TradingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # init the main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.name = "TradingApp Main Window"
        self.trader = Trader()

        # set app icon
        self.icon_photo = PhotoImage(file="gui/icon.png")
        self.iconphoto(False, self.icon_photo, self.icon_photo)

        # set app window size
        self.geometry("1096x728+200+100")
        self.configure(bg="#FFFFFF")
        self.title("Program Trading Based on Webull")
        self.title_font = tkfont.Font(family="Arial Rounded MT Bold", size=18, weight="bold", slant="italic")
        self.resizable(False, False)

        # set frame dict
        self.frames = {}

        # init frames
        for F in (DashboardLogin, DashboardLogged, StrategyMonitor, TreaderProfile, TradingList,
                  Performance, APPLog, Message, DownloadData, SaveExit):
            page_name = F.__name__
            frame = F(self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # show login frame
        self.show_frame("DashboardLogged")

        # bind window click event
        self.bind("<Button-1>", self.window_clicked)

        # Main window state:
        self.cnt = 0
        self.event_x = -1
        self.event_y = -1
        self.current_frame = self.frames["DashboardLogged"]

        # Trading State:
        self.logged_in = False

        # Database State:
        self.db_connected = False
        self.db_name = "tradingApp.db"

    def print_sth(self):
        print("sth")
        print(f'{self.cnt}')

    def window_clicked(self, event):
        self.event_x = event.x
        self.event_y = event.y
        print(f"{self.name} Clicked, x: {self.event_x} y: {self.event_y}")

    def top_bar_clicked(self, x, y):
        print(f"{self.name} top bar Clicked, x: {x} y: {y}")

    def sidebar_clicked(self, x, y):
        # print(f"{self.name} side bar Clicked, x: {x} y: {y}")
        if 97 <= y <= 147:
            if self.logged_in:
                self.show_frame("DashboardLogged")
            else:
                self.show_frame("DashboardLogin")
        elif 161 <= y <= 211:
            self.show_frame("StrategyMonitor")
        elif 225 <= y <= 275:
            self.show_frame("TreaderProfile")
        elif 289 <= y <= 339:
            self.show_frame("TradingList")
        elif 353 <= y <= 403:
            self.show_frame("Performance")
        elif 417 <= y <= 467:
            self.show_frame("APPLog")
        elif 481 <= y <= 531:
            self.show_frame("Message")
        elif 545 <= y <= 595:
            self.show_frame("DownloadData")
        elif 609 <= y <= 659:
            self.show_frame("SaveExit")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        self.current_frame = frame
        frame.tkraise()


if __name__ == "__main__":
    app = TradingApp()
    app.mainloop()
