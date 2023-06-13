import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage


class DashboardLogged(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("frame1")

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

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(548.0, 364.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(648.0, 385.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(1012.0, 30.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(971.0, 30.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(328.0, 30.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(534.0, 30.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(534.0, 30.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(328.0, 30.0, image=self.image_image_8)

        self.canvas.create_text(
            536.0,
            703.0,
            anchor="nw",
            text="placeholder for dji",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.create_text(
            273.0,
            704.0,
            anchor="nw",
            text="placeholder for spx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.create_text(
            404.0,
            704.0,
            anchor="nw",
            text="placeholder for ndx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.create_text(
            395.0,
            326.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            468.0,
            521.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            469.0,
            559.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            469.0,
            599.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            395.0,
            399.0,
            anchor="nw",
            text="888.88",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            395.0,
            444.0,
            anchor="nw",
            text="888.88",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            469.0,
            399.0,
            anchor="nw",
            text="8.88%",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            469.0,
            444.0,
            anchor="nw",
            text="8.88%",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            395.0,
            281.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            392.0,
            242.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            392.0,
            184.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.canvas.create_text(
            317.0,
            135.0,
            anchor="nw",
            text="emailplaceholder@gmail.com",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(839.0, 399.5, image=entry_image_1)
        self.entry_1 = Text(
            self.canvas,
            bd=0,
            bg="#EFF4FB",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=670.0, y=194.0, width=338.0, height=409.0)

        self.canvas.pack(fill="both", expand=True)
