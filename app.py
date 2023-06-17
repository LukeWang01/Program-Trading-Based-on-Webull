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
        tk.Tk.__init__(self, *args, **kwargs)

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
        self.show_frame("SaveExit")

        # other settings
        self.bind("<Button-1>", self.window_clicked)
        self.cnt = 0

    def print_sth(self):
        print("sth")
        print(f'{self.cnt}')

    def window_clicked(self, event):
        print(f"Main Window Clicked, x: {event.x} y: {event.y}")
        if event.x < 50 and event.y < 50:
            self.cnt += 1
            if self.cnt % 2 == 0:
                self.show_frame("DashboardLogged")
            else:
                self.show_frame("DashboardLogin")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = TradingApp()
    app.mainloop()
