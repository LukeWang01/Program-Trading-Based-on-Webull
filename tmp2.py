import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gui.gui_0_DashboardLogin.DashboardLogin import DashboardLogin

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./gui/gui_0_DashboardLogin/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

NUM = 0


def show_frame1():
    frame1.tkraise()


def show_frame2():
    frame2.tkraise()


def switch_frame(event):
    print("clicked")
    print(event.x, event.y)
    global NUM
    NUM += 1
    if NUM % 2 == 0:
        show_frame1()
    else:
        show_frame2()


def get_fram2(window):
    frame2 = tk.Frame(window)
    canvas = Canvas(
        frame2,
        bg="#F1F5F9",
        height=728,
        width=1096,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_text(
        40.0,
        43.0,
        anchor="nw",
        text="Administrator",
        fill="#808080",
        font=("Montserrat Bold", 16 * -1),
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        548.0,
        364.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        645.0,
        432.0,
        image=image_image_2
    )

    return frame2


# Create a Tkinter window
window = tk.Tk()

# Create two frames
frame1 = tk.Frame(window, width=1096, height=728, bg="red")
frame2 = get_fram2(window)

# Initially, show frame1
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")

# # Create buttons to switch frames
# button1 = tk.Button(window, text="Frame 1", command=show_frame1)
# button2 = tk.Button(window, text="Frame 2", command=show_frame2)
#
# # Grid the buttons
# button1.grid(row=1, column=0)
# button2.grid(row=2, column=0)

window.bind("<Button-1>", switch_frame)

show_frame1()

# Start the Tkinter event loop
window.mainloop()
