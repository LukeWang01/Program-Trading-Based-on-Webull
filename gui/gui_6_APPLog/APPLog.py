import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Text, PhotoImage


class APPLog(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.name = "APPLog"
        self.parent = parent

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./frame6")

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

        self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(548.0, 364.0, image=self.image_1)

        self.image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.canvas.create_image(648.0, 385.0, image=self.image_2)

        self.image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.canvas.create_image(1012.0, 30.0, image=self.image_3)

        self.image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.canvas.create_image(971.0, 30.0, image=self.image_4)

        self.image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.canvas.create_image(328.0, 30.0, image=self.image_5)

        self.image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.canvas.create_image(534.0, 30.0, image=self.image_6)

        self.image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.canvas.create_image(534.0, 30.0, image=self.image_7)

        self.image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.canvas.create_image(328.0, 30.0, image=self.image_8)

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

        self.entry_1 = Text(
            self.canvas,
            bd=0,
            bg="#EFF4FB",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=269.0,
            y=176.0,
            width=742.0,
            height=398.0
        )

        self.canvas.create_text(
            275.0,
            605.0,
            anchor="nw",
            text="Note: placeholder for the app log location",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.frame_clicked)

    def frame_clicked(self, event):
        print(f"{self.name} clicked, x: {event.x} y: {event.y}")


