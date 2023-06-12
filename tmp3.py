import tkinter as tk
from pathlib import Path

from tkinter import Tk, Canvas, Entry, PhotoImage


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui/gui_0_DashboardLogin/frame0")

window = tk.Tk()
window.geometry("1096x728+50+50")



frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, sticky="nsew")

canvas = Canvas(
    frame1,
    bg="#3A59C7",
    height=728,
    width=1096,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Load images
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))

# Create canvas objects
image_1 = canvas.create_image(548.0, 364.0, image=image_image_1)
image_2 = canvas.create_image(645.0, 432.0, image=image_image_2)
image_3 = canvas.create_image(1012.0, 30.0, image=image_image_3)
image_4 = canvas.create_image(971.0, 30.0, image=image_image_4)
entry_bg_1 = canvas.create_image(817.5, 491.5, image=entry_image_1)
entry_bg_2 = canvas.create_image(817.5, 397.5, image=entry_image_2)
entry_bg_3 = canvas.create_image(817.5, 307.0, image=entry_image_3)
image_5 = canvas.create_image(328.0, 30.0, image=image_image_5)
image_6 = canvas.create_image(534.0, 30.0, image=image_image_6)
image_7 = canvas.create_image(534.0, 30.0, image=image_image_7)
image_8 = canvas.create_image(328.0, 30.0, image=image_image_8)

entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
entry_1.place(
    x=688.0,
    y=474.0,
    width=259.0,
    height=33.0
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=688.0,
    y=380.0,
    width=259.0,
    height=33.0
)

entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=688.0,
    y=287.0,
    width=259.0,
    height=38.0
)

# Place the canvas on the frame
canvas.pack(fill="both", expand=True)

window.mainloop()
