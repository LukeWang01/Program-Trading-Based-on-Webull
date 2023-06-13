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
        for F in (DashboardLogin, DashboardLogged):
            page_name = F.__name__
            frame = F(self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # show login frame
        self.show_frame("DashboardLogin")

        # other settings
        self.bind("<Button-1>", self.window_clicked)
        self.cnt = 0

    def window_clicked(self, event):
        print("clicked")
        print(event.x, event.y)
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
