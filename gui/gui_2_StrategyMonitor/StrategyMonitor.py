import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage


class StrategyMonitor(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)
        self.name = "StrategyMonitor"
        self.parent = parent
        self.current = False

        # UI elements：
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./frame2")

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

        # Load images
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        self.entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))

        # Create canvas objects
        self.image_1 = self.canvas.create_image(548.0, 364.0, image=self.image_image_1)
        self.image_2 = self.canvas.create_image(648.0, 385.0, image=self.image_image_2)
        self.image_3_msg = self.canvas.create_image(1012.0, 30.0, image=self.image_image_3)
        self.image_4_notify = self.canvas.create_image(971.0, 30.0, image=self.image_image_4)
        self.image_5 = self.canvas.create_image(328.0, 30.0, image=self.image_image_5)
        self.image_6 = self.canvas.create_image(534.0, 30.0, image=self.image_image_6)
        self.image_7 = self.canvas.create_image(534.0, 30.0, image=self.image_image_7)
        self.image_8 = self.canvas.create_image(328.0, 30.0, image=self.image_image_8)

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

        self.strategy_status = self.canvas.create_text(
            405.0,
            176.0,
            anchor="nw",
            text="running",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.current_strategy = self.canvas.create_text(
            405.0,
            135.0,
            anchor="nw",
            text="strategy01",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.entry_bg_1 = self.canvas.create_image(840.0, 547.0, image=self.entry_image_1)
        self.entry_1_strategy_stream = Text(self.canvas, bd=0, bg="#EFF4FB", fg="#000716", highlightthickness=0)
        self.entry_1_strategy_stream.place(x=669.0, y=472.0, width=342.0, height=148.0)

        self.entry_bg_2 = self.canvas.create_image(840.0, 314.0, image=self.entry_image_2)
        self.entry_2_quoter_stream = Text(self.canvas, bd=0, bg="#EFF4FB", fg="#000716", highlightthickness=0)
        self.entry_2_quoter_stream.place(x=669.0, y=204.0, width=342.0, height=218.0)

        self.entry_bg_3 = self.canvas.create_image(445.0, 364.0, image=self.entry_image_3)
        self.entry_3_imported_list = Text(self.canvas, bd=0, bg="#EFF4FB", fg="#000716", highlightthickness=0)
        self.entry_3_imported_list.place(x=274.0, y=304.0, width=342.0, height=118.0)

        self.entry_bg_4 = self.canvas.create_image(485.0, 473.5, image=self.entry_image_4)
        self.entry_4_strategy_quoter = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_4_strategy_quoter.place(x=409.0, y=461.0, width=152.0, height=23.0)

        self.entry_bg_5 = self.canvas.create_image(485.0, 509.5, image=self.entry_image_5)
        self.entry_5_monitor_ticker = Entry(self.canvas, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_5_monitor_ticker.place(x=409.0, y=497.0, width=152.0, height=23.0)

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
            if 427 <= x <= 551 and 234 <= y <= 259:
                self.select_strategy()
            elif 285 <= x <= 409 and 596 <= y <= 626:
                self.run_strategy()
            elif 444 <= x <= 568 and 596 <= y <= 626:
                self.cancel_strategy()

    def update_data(self):
        pass

    def select_strategy(self):
        print(f"{self.name}: Select strategy clicked")

    def run_strategy(self):
        print(f"{self.name}: Run strategy clicked")

    def cancel_strategy(self):
        print(f"{self.name}: Cancel strategy clicked")

    def msg_clicked(self, event):
        print(f"{self.name}: Message clicked")

    def notify_clicked(self, event):
        print(f"{self.name}: Notify clicked")



