"""

APP GUI Main interface

LukeLab, 05/2023

"""
import tkinter as tk

from tkinter import PhotoImage, messagebox
from tkinter import font as tkfont

from trader.Trader import Trader
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
from utils.SQLiteHelper import SQLiteHelper


class TradingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # init the main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.name = "TradingApp Main Window"
        self.trader = Trader()

        # set app icon
        # self.icon_photo = PhotoImage(file="gui/icon.png")
        # self.iconphoto(False, self.icon_photo, self.icon_photo)
        self.iconbitmap(default="gui/icon.ico")

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
        self.db = SQLiteHelper(self.db_name)
        self.read_trader_info()

        # show first frame
        self.show_frame("DashboardLogged")

    # Frontend functions:
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
        frame.update_data()
        frame.tkraise()

    # Back-end functions:
    # Trader:
    def read_trader_info(self):
        self.trader.set_device_name(self.db.get_device_name())
        self.trader.set_auth_access_token(self.db.get_access_token())
        self.trader.set_auth_did(self.db.get_did())
        self.trader.set_auth_uuid(self.db.get_uuid())
        self.trader.set_user_name(self.db.get_email())

    # DashboardLogin
    def setup_did(self, did):
        self.trader.set_auth_did(did)
        self.db.update_did(did)

    def setup_uuid(self, uuid):
        self.trader.set_auth_uuid(uuid)
        self.db.update_uuid(uuid)

    def set_access_token(self, access_token):
        self.trader.set_auth_access_token(access_token)
        self.db.update_access_token(access_token)

    def set_device_name(self, device_name):
        self.trader.set_device_name(device_name)
        self.db.update_device_name(device_name)

    def login(self, email, password, pid):
        print(f"email: {email}, parent login called")
        self.db.update_email(email)
        self.trader.set_trader_info(email, password, pid)
        res = self.trader.log_in()
        if res:
            self.logged_in = True
            self.show_frame("DashboardLogged")
        else:
            self.logged_in = False
            messagebox.showinfo("Oops something went wrong", "please check username or password.              ")


if __name__ == "__main__":
    app = TradingApp()
    app.mainloop()
