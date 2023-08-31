import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, simpledialog, messagebox, END

from utils.dataIO import logging_info
from utils.input_check import is_valid_email, is_valid_phone_number, is_valid_pid

import webbrowser


class DashboardLogin(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)
        self.name = "DashboardLogin"
        self.parent = parent
        self.current = False

        # UI elements：
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("frame0")

        self.canvas = Canvas(
            self,
            bg="#3A59C7",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Load images
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))

        # Create canvas objects
        self.image_1 = self.canvas.create_image(548.0, 364.0, image=self.image_image_1)
        self.image_2 = self.canvas.create_image(645.0, 432.0, image=self.image_image_2)
        self.image_3_msg = self.canvas.create_image(1012.0, 30.0, image=self.image_image_3)
        self.image_4_notify = self.canvas.create_image(971.0, 30.0, image=self.image_image_4)
        self.entry_bg_1 = self.canvas.create_image(817.5, 491.5, image=self.entry_image_1)
        self.entry_bg_2 = self.canvas.create_image(817.5, 397.5, image=self.entry_image_2)
        self.entry_bg_3 = self.canvas.create_image(817.5, 307.0, image=self.entry_image_3)
        self.image_5 = self.canvas.create_image(328.0, 30.0, image=self.image_image_5)
        self.image_6 = self.canvas.create_image(534.0, 30.0, image=self.image_image_6)
        self.image_7 = self.canvas.create_image(534.0, 30.0, image=self.image_image_7)
        self.image_8 = self.canvas.create_image(328.0, 30.0, image=self.image_image_8)

        self.entry_3_email = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial Rounded MT Bold", 10)
        )
        self.entry_3_email.place(x=688.0, y=287.0, width=259.0, height=38.0)

        self.entry_2_password = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_2_password.place(x=688.0, y=380.0, width=259.0, height=33.0)

        self.entry_1_PID = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_1_PID.place(x=688.0, y=474.0, width=259.0, height=33.0)

        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.frame_clicked)
        self.canvas.bind("<Return>", self.login_clicked)

        self.canvas.tag_bind(self.image_3_msg, "<Button-1>", self.msg_clicked)
        self.canvas.tag_bind(self.image_4_notify, "<Button-1>", self.notify_clicked)
        self.entry_1_PID.bind("<Return>", lambda event: self.login_clicked())

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
            if 712 <= x <= 936 and 529 <= y <= 564:
                self.login_clicked()
            elif 667 <= x <= 727 and 605 <= y <= 630:
                self.setup_did_clicked()
            elif 735 <= x <= 805 and 605 <= y <= 630:
                self.setup_uuid_clicked()
            elif 778 <= x <= 858 and 637 <= y <= 661:
                self.instruction_clicked()
            elif 814 <= x <= 894 and 605 <= y <= 630:
                self.access_token_clicked()
            elif 902 <= x <= 982 and 605 <= y <= 630:
                self.device_name_clicked()

    def update_data(self):
        if self.parent.trader.username:
            self.entry_3_email.delete(0, END)
            self.entry_3_email.insert(0, self.parent.trader.username)
            self.entry_2_password.focus()
        else:
            self.entry_3_email.focus()

    def msg_clicked(self, event):
        self.parent.show_info_message("Message example")

    def notify_clicked(self, event):
        self.parent.show_info_message("Message example")

    def device_name_clicked(self):
        input_value = simpledialog.askstring("Setup device name",
                                             "Enter the device name (click instruction for help) :",
                                             initialvalue=self.parent.db.get_device_name())
        if input_value is not None:
            self.parent.set_device_name(input_value)

    def access_token_clicked(self):
        input_value = simpledialog.askstring(
            "Setup access token",
            "Enter the access token from the web, keep it safe (click instruction for help) :",
            initialvalue=self.parent.db.get_access_token())
        if input_value is not None:
            self.parent.set_access_token(input_value)

    def setup_did_clicked(self):
        input_value = simpledialog.askstring("Setup _did value", "Enter the _did value (click instruction for help) : ",
                                             initialvalue=self.parent.db.get_did())
        if input_value is not None:
            self.parent.setup_did(input_value)

    def setup_uuid_clicked(self):
        input_value = simpledialog.askstring("Setup uuid value", "Enter the uuid value (click instruction for help) : ",
                                             initialvalue=self.parent.db.get_uuid())
        if input_value is not None:
            self.parent.setup_uuid(input_value)

    def instruction_clicked(self):
        # print(f"{self.name}: Instruction clicked")
        webbrowser.open("https://github.com/LukeWang01/Program-Trading-Based-on-Webull/blob/main/docs/first_run_setup.md")

    def login_clicked(self):
        logging_info("Login triggered")
        email = self.entry_3_email.get()
        password = self.entry_2_password.get()
        pid = self.entry_1_PID.get()
        if (is_valid_email(email) or is_valid_phone_number(email)) and is_valid_pid(pid):
            self.parent.login(email, password, pid)
        else:
            messagebox.showinfo("Oops something went wrong", "incorrect email, phone number, or PID format")
