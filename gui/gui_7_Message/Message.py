import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class Message(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)
        self.name = "Message"
        self.parent = parent
        self.current = False

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
            703.0,
            anchor="nw",
            text="placeholder for dji",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.spx = self.canvas.create_text(
            273.0,
            704.0,
            anchor="nw",
            text="placeholder for spx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.ndx = self.canvas.create_text(
            404.0,
            704.0,
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
        self.entry_1_receiver_email = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1_receiver_email.place(
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
            highlightthickness=0
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

        # self.canvas.create_rectangle(
        #     423.0,
        #     441.0,
        #     443.0,
        #     461.0,
        #     fill="#FFFFFF",
        #     outline="")
        #
        # self.canvas.create_rectangle(
        #     423.0,
        #     441.0,
        #     443.0,
        #     461.0,
        #     fill="#FFFFFF",
        #     outline="")

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
            elif 423 <= x <= 443 and 441 <= y <= 461:
                self.enable_notification_clicked()

    def update_data(self):
        pass

    def update_settings_clicked(self):
        print(f"{self.name}: Update settings clicked")

    def enable_notification_clicked(self):
        print(f"{self.name}: Enable notification clicked")

    def msg_clicked(self, event):
        print(f"{self.name}: Message clicked")

    def notify_clicked(self, event):
        print(f"{self.name}: Notify clicked")

