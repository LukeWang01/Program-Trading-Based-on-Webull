import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage


class DashboardLogin(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # self.controller = controller

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
        self.image_3 = self.canvas.create_image(1012.0, 30.0, image=self.image_image_3)
        self.image_4 = self.canvas.create_image(971.0, 30.0, image=self.image_image_4)
        self.entry_bg_1 = self.canvas.create_image(817.5, 491.5, image=self.entry_image_1)
        self.entry_bg_2 = self.canvas.create_image(817.5, 397.5, image=self.entry_image_2)
        self.entry_bg_3 = self.canvas.create_image(817.5, 307.0, image=self.entry_image_3)
        self.image_5 = self.canvas.create_image(328.0, 30.0, image=self.image_image_5)
        self.image_6 = self.canvas.create_image(534.0, 30.0, image=self.image_image_6)
        self.image_7 = self.canvas.create_image(534.0, 30.0, image=self.image_image_7)
        self.image_8 = self.canvas.create_image(328.0, 30.0, image=self.image_image_8)

        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_1.place(x=688.0, y=474.0, width=259.0, height=33.0)

        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_2.place(x=688.0, y=380.0, width=259.0, height=33.0)

        self.entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial Rounded MT Bold", 10)
        )
        self.entry_3.place(x=688.0, y=287.0, width=259.0, height=38.0)

        self.canvas.pack(fill="both", expand=True)

