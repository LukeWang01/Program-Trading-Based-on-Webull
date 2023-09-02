"""
APP GUI Main interface
LukeLab, 05/2023
"""
import threading
import time
import tkinter as tk

from tkinter import messagebox
from tkinter import font as tk_font

import schedule

import quoter.Quoter as Quoter

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
from utils.dataIO import logging_info


class TradingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # init the main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.name = "TradingApp"

        # set app icon
        self.iconbitmap("gui/icon.ico")

        # set app window size
        self.geometry("1096x728+200+100")
        self.configure(bg="#FFFFFF")
        self.title("Program Trading Based on Webull")
        self.title_font = tk_font.Font(family="Arial Rounded MT Bold", size=18, weight="bold", slant="italic")
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
        self.bind("<Button-1>", self.window_clicked)    # bind window click event
        logging_info("GUI frames initialized.")

        # Main window state:
        self.cnt = 0
        self.event_x = -1
        self.event_y = -1
        self.current_frame = self.frames["DashboardLogin"]

        # Trading State:
        self.trader = Trader()
        self.logged_in = False

        # Email Notification State:
        self.sender_email = ""
        self.sender_password = ""
        self.receiver_email_1 = ""
        self.receiver_email_2_bcc = ""
        self.enable_email_notify = 1

        # Trader Profile State:
        self.save_user_email = 1
        self.PID_timeout = 15

        # Database State:
        self.db_connected = False
        self.db_name = "tradingApp.db"
        self.db = SQLiteHelper(self.db_name)
        self.read_trader_info()
        self.read_email_notification_state()
        self.read_trader_profile_state()

        # show first frame
        self.show_frame("DashboardLogin")

        # App variables:
        # 1. set real-time Index Price:
        self.spx_price = 0
        self.dji_price = 0
        self.ixic_price = 0
        self.update_market_price(Quoter.get_market_index_real_time_price())

    # Frontend functions:
    def window_clicked(self, event):
        self.event_x = event.x
        self.event_y = event.y

    def top_bar_clicked(self, x, y):
        # Not core funtion of the app, implement later
        pass

    def sidebar_clicked(self, x, y):
        if 97 <= y <= 147:
            if self.logged_in:
                # check login status, or using webull api to do hard check
                self.show_frame("DashboardLogged")
            else:
                self.show_frame("DashboardLogin")
        elif 161 <= y <= 211:
            self.show_frame("StrategyMonitor")
        elif 225 <= y <= 275:
            if self.logged_in:
                self.show_frame("TreaderProfile")
            else:
                messagebox.showinfo("Oops", "Sensitive Info, Please login first!")
        elif 289 <= y <= 339:
            if self.logged_in:
                self.show_info_message("Fetching trading list...")
                self.show_frame("TradingList")
            else:
                messagebox.showinfo("Oops", "Sensitive Info, Please login first!")
        elif 353 <= y <= 403:
            if self.logged_in:
                self.show_frame("Performance")
            else:
                messagebox.showinfo("Oops", "Sensitive Info, Please login first!")
        elif 417 <= y <= 467:
            self.show_frame("APPLog")
        elif 481 <= y <= 531:
            self.show_frame("Message")
        elif 545 <= y <= 595:
            self.show_frame("DownloadData")
        elif 609 <= y <= 659:
            result = messagebox.askyesno("Confirmation", "Do you want to exit?")
            if result:
                self.show_frame("SaveExit")
                self.save_app_state()
            else:
                pass

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        self.current_frame = frame
        frame.tkraise()
        frame.update_data()

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
        logging_info('set did successfully')

    def setup_uuid(self, uuid):
        self.trader.set_auth_uuid(uuid)
        self.db.update_uuid(uuid)
        logging_info('set uuid successfully')

    def set_access_token(self, access_token):
        self.trader.set_auth_access_token(access_token)
        self.db.update_access_token(access_token)
        logging_info('set access token successfully')

    def set_device_name(self, device_name):
        self.trader.set_device_name(device_name)
        self.db.update_device_name(device_name)
        logging_info('set device name successfully')

    def login(self, email, password, pid):
        # print(f"email: {email}, parent login called")
        self.db.update_email(email)
        self.trader.set_trader_info(email, password, pid)
        if self.trader.login_preparation():
            res = self.trader.log_in()
            if res:
                self.logged_in = True
                self.show_frame("DashboardLogged")
                logging_info(f"User: {email} logged in successfully.")
            else:
                messagebox.showerror("Oops something went wrong", "please check username or password.              ")
                logging_info(f"User: {email} failed to log in.")
        else:
            messagebox.showerror("Oops something went wrong", "Please setup UUID/DID/ACCESS_TOKEN.              ")

    def save_app_state(self):
        pass

    def set_email_notification_state(self, sender_email, sender_password, receiver_email_1, receiver_email_2_bcc,
                                     enable_email_notify):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email_1 = receiver_email_1
        self.receiver_email_2_bcc = receiver_email_2_bcc
        self.enable_email_notify = enable_email_notify

        self.db.update_sender_email(sender_email)
        self.db.update_sender_password(sender_password)
        self.db.update_receiver_email_1(receiver_email_1)
        self.db.update_receiver_email_2_bcc(receiver_email_2_bcc)
        self.db.update_enable_email_notify(enable_email_notify)
        logging_info("Email notification state update to DB")

    def read_email_notification_state(self):
        self.sender_email = self.db.get_sender_email()
        self.sender_password = self.db.get_sender_password()
        self.receiver_email_1 = self.db.get_receiver_email_1()
        self.receiver_email_2_bcc = self.db.get_receiver_email_2_bcc()
        self.enable_email_notify = self.db.get_enable_email_notify()

    def is_email_setup(self):
        if self.sender_email == "" or self.sender_password == "" or self.receiver_email_1 == "":
            return False
        else:
            return True

    def exit_app(self):
        self.show_info_message("Exiting...")
        logging_info("APP exited")
        # sys.exit()
        self.destroy()

    def show_info_message(self, message, duration=2000):
        # Create a Toplevel window for the info message
        info_window = tk.Toplevel()
        info_window.wm_overrideredirect(True)  # Remove window decorations
        info_window.attributes("-topmost", True)  # Keep the window on top
        info_window.configure(bg="#333333")  # Set background color
        info_window.attributes("-alpha", 0.9)  # Set transparency

        # Create a Label widget to display the message
        label = tk.Label(info_window, text=message, fg="white", bg="#333333", padx=10, pady=5)
        label.pack()

        # Calculate the position of the info window to be centered within the main window
        root_x = self.winfo_rootx() + self.winfo_width() // 2 - info_window.winfo_reqwidth() // 2 + 100
        root_y = self.winfo_rooty() + self.winfo_height() // 2 - info_window.winfo_reqheight() // 2 + 300
        info_window.geometry(f"+{root_x}+{root_y}")

        # After the specified duration, close the info window
        info_window.after(duration, info_window.destroy)

    def update_market_price(self, latest_prices):
        self.spx_price = f'SPX: {round(latest_prices["^GSPC"], 2)}'
        self.dji_price = f'DJI: {round(latest_prices["^DJI"], 2)}'
        self.ixic_price = f'IXIC: {round(latest_prices["^IXIC"], 2)}'
        if self.current_frame.name != 'DashboardLogin':
            self.current_frame.update_market_status()

    def read_trader_profile_state(self):
        self.save_user_email = self.db.get_save_user_email()
        self.PID_timeout = self.db.get_PID_expired()
        if self.PID_timeout != self.trader.PID_timeout:
            self.trader.set_PID_expiry(self.PID_timeout)

    def set_trader_profile_state(self, sender_email, sender_password, receiver_email_1, save_user_email, pid_expire):
        # email notification:
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email_1 = receiver_email_1

        # trader profile:
        self.save_user_email = save_user_email
        self.PID_timeout = pid_expire
        self.trader.set_PID_expiry(pid_expire)

        # update database:
        self.db.update_sender_email(sender_email)
        self.db.update_sender_password(sender_password)
        self.db.update_receiver_email_1(receiver_email_1)
        self.db.update_save_user_email(save_user_email)
        self.db.update_PID_expired(pid_expire)
        logging_info('Trader profile update to DB.')


# Global Functions:
def bkg_scheduled_fun(app_obj):
    """
    task can be scheduled later in the main thread
    """
    # refresh market price every 30 seconds:
    schedule.every(30).seconds.do(get_real_time_idx_price, app_obj)
    logging_info('Background job scheduled.')
    # continuously run all scheduled background job, until stop flag is set:
    while not bkg_thread_stop_flag.is_set():
        schedule.run_pending()
        time.sleep(1)


def get_real_time_idx_price(app_obj):
    latest_prices = Quoter.get_market_index_real_time_price()
    app_obj.update_market_price(latest_prices)


if __name__ == "__main__":
    # main thread:
    print('TradingApp starting...')
    app = TradingApp()
    logging_info('TradingApp started.')
    # new a thread to run background job:
    bkg_thread_stop_flag = threading.Event()
    bkg_thread = threading.Thread(target=bkg_scheduled_fun, args=(app,))
    bkg_thread.start()
    app.mainloop()

    # closing App:
    bkg_thread_stop_flag.set()
    bkg_thread.join()
    logging_info('TradingApp closed, bkg_thread closed, App terminated successfully.')
    print('TradingApp closed, bkg_thread closed, App terminated successfully.')
