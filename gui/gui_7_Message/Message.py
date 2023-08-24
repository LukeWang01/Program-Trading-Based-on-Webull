import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Text, PhotoImage, messagebox

from utils.dataIO import logging_info, logging_warning
from utils.input_check import is_valid_email


class Message(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)
        self.name = "Message"
        self.parent = parent
        self.current = False

        self.enable_notification = 1    # matches with the default value in the database

        # UI elements：
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./frame7")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg="#F1F5F9",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            548.0,
            364.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            648.0,
            385.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3_msg = self.canvas.create_image(
            1012.0,
            30.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4_notify = self.canvas.create_image(
            971.0,
            30.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            328.0,
            30.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            534.0,
            30.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            534.0,
            30.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            328.0,
            30.0,
            image=self.image_image_8
        )

        self.dji = self.canvas.create_text(
            536.0,
            707.0,
            anchor="nw",
            text="placeholder for dji",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.spx = self.canvas.create_text(
            273.0,
            707.0,
            anchor="nw",
            text="placeholder for spx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.ixic = self.canvas.create_text(
            404.0,
            707.0,
            anchor="nw",
            text="placeholder for ndx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.account_type = self.canvas.create_text(
            411.0,
            166.0,
            anchor="nw",
            text="1 or 2, email or phone",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.account_id = self.canvas.create_text(
            411.0,
            135.0,
            anchor="nw",
            text="88888888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            491.0,
            409.5,
            image=self.entry_image_1
        )
        self.entry_1_receiver_email_bcc = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1_receiver_email_bcc.place(
            x=415.0,
            y=397.0,
            width=152.0,
            height=23.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            491.0,
            252.5,
            image=self.entry_image_2
        )
        self.entry_2_sender_email = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2_sender_email.place(
            x=415.0,
            y=240.0,
            width=152.0,
            height=23.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            491.0,
            295.5,
            image=self.entry_image_3
        )
        self.entry_3_sender_password = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_3_sender_password.place(
            x=415.0,
            y=283.0,
            width=152.0,
            height=23.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            491.0,
            339.5,
            image=self.entry_image_4
        )
        self.entry_4_receiver_email = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4_receiver_email.place(
            x=415.0,
            y=327.0,
            width=152.0,
            height=23.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            840.0,
            380.0,
            image=self.entry_image_5
        )
        self.entry_5_message_list = Text(
            self.canvas,
            bd=0,
            bg="#EFF4FB",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5_message_list.place(
            x=669.0,
            y=180.0,
            width=342.0,
            height=398.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9_check_box_0 = self.canvas.create_image(
            441.0,
            448.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10_check_box_1 = self.canvas.create_image(
            441.0,
            448.0,
            image=self.image_image_10
        )

        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.frame_clicked)

        self.canvas.tag_bind(self.image_3_msg, "<Button-1>", self.msg_clicked)
        self.canvas.tag_bind(self.image_4_notify, "<Button-1>", self.notify_clicked)

    def frame_clicked(self, event):
        x = event.x
        y = event.y
        if x <= 200:
            # Sidebar area clicked
            self.parent.sidebar_clicked(x, y)
        elif 200 <= x <= 1096 and y <= 60:
            # Top bar area clicked
            self.parent.top_bar_clicked(x, y)
        else:
            # frame area clicked
            if 374 <= x <= 524 and 600 <= y <= 635:
                self.update_settings_clicked()
            elif 430 <= x <= 453 and 439 <= y <= 465:
                self.enable_notification_clicked()

    def update_data(self):
        self.update_market_status()

        self.set_account_id(self.parent.trader.account_id)
        self.set_account_type(self.parent.trader.account_type)

        self.set_sender_email(self.parent.sender_email)
        self.set_sender_password(self.parent.sender_password)
        self.set_receiver_email_1(self.parent.receiver_email_1)
        self.set_receiver_email_2_bcc(self.parent.receiver_email_2_bcc)
        self.enable_notification = self.parent.enable_email_notify
        if self.enable_notification:
            self.canvas.itemconfig(self.image_9_check_box_0, state="hidden")
            self.canvas.itemconfig(self.image_10_check_box_1, state="normal")
        else:
            self.canvas.itemconfig(self.image_9_check_box_0, state="normal")
            self.canvas.itemconfig(self.image_10_check_box_1, state="hidden")
        self.update_message_list()

    def update_settings_clicked(self):
        sender_email = self.entry_2_sender_email.get()
        sender_password = self.entry_3_sender_password.get()
        receiver_email_1 = self.entry_4_receiver_email.get()
        receiver_email_2_bcc = self.entry_1_receiver_email_bcc.get()
        enable_email_notify = self.enable_notification
        if is_valid_email(sender_email) and is_valid_email(receiver_email_1) and is_valid_email(receiver_email_2_bcc):
            self.parent.set_email_notification_state(sender_email, sender_password, receiver_email_1,
                                                     receiver_email_2_bcc, enable_email_notify)
            logging_info("Email notification settings updated")
        else:
            messagebox.showerror("Oops something went wrong", "Invalid email address")

    def enable_notification_clicked(self):
        if self.enable_notification:
            self.enable_notification = 0
            self.canvas.itemconfig(self.image_9_check_box_0, state="normal")
            self.canvas.itemconfig(self.image_10_check_box_1, state="hidden")
            # print(self.enable_notification)
        else:
            self.enable_notification = 1
            self.canvas.itemconfig(self.image_9_check_box_0, state="hidden")
            self.canvas.itemconfig(self.image_10_check_box_1, state="normal")
            # print(self.enable_notification)

    def msg_clicked(self, event):
        # print(f"{self.name}: Message clicked")
        # not core functionality, implement later
        pass

    def notify_clicked(self, event):
        # print(f"{self.name}: Notify clicked")
        # not core functionality, implement later
        pass

    def update_message_list(self):
        message_list = self.read_message_list()
        self.entry_5_message_list.delete(1.0, tk.END)
        self.entry_5_message_list.insert(1.0, message_list)
        self.entry_5_message_list.see(tk.END)

    def read_message_list(self):
        try:
            with open("message_list.txt", "r") as file:
                message_list = file.read()
            return message_list
        except FileNotFoundError:
            logging_warning("message_list.txt not found, returning empty string")
            return ""

    def set_sender_email(self, sender_email):
        self.entry_2_sender_email.delete(0, tk.END)
        self.entry_2_sender_email.insert(0, sender_email)

    def set_sender_password(self, sender_password):
        self.entry_3_sender_password.delete(0, tk.END)
        self.entry_3_sender_password.insert(0, sender_password)

    def set_receiver_email_1(self, receiver_email_1):
        self.entry_4_receiver_email.delete(0, tk.END)
        self.entry_4_receiver_email.insert(0, receiver_email_1)

    def set_receiver_email_2_bcc(self, receiver_email_2_bcc):
        self.entry_1_receiver_email_bcc.delete(0, tk.END)
        self.entry_1_receiver_email_bcc.insert(0, receiver_email_2_bcc)

    def update_market_status(self):
        self.canvas.itemconfig(self.spx, text=self.parent.spx_price)
        self.canvas.itemconfig(self.dji, text=self.parent.dji_price)
        self.canvas.itemconfig(self.ixic, text=self.parent.ixic_price)

    def set_account_id(self, account_id):
        self.canvas.itemconfig(self.account_id, text=account_id)

    def set_account_type(self, account_type):
        self.canvas.itemconfig(self.account_type, text=account_type)

