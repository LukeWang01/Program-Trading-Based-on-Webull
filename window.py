import tkinter as tk
from pathlib import Path
from tkinter import font as tkfont
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./gui/gui_0_DashboardLogin/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set app icon
        icon_photo = tk.PhotoImage(file="gui/icon.png")
        self.iconphoto(False, icon_photo)

        # set app window size
        self.geometry("1096x728")
        self.configure(bg="#FFFFFF")
        self.title("Program Trading Based on Webull")
        self.title_font = tkfont.Font(
            family="Arial Rounded MT Bold", size=18, weight="bold", slant="italic"
        )
        self.resizable(False, False)

        self.frames = {}

        # Create the frames
        # frame1 = Frame1(self)
        frame2 = Frame2(self)

        # Store the frames in a dictionary
        # self.frames[Frame1] = frame1
        # self.frames[Frame2] = frame2

        # frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        # self.show_frame(Frame1)

        # Bind the window's click event to switch frames
        self.bind("<Button-1>", self.switch_frame)

    def switch_frame(self, event):
        print("clicked")
        print(event.x, event.y)
        # self.show_frame(Frame2)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="Frame 1")
        # label.pack()
        self.parent = parent

        # from tkinter import *
        # Explicit imports to satisfy Flake8

        canvas = Canvas(
            parent,
            bg="#F1F5F9",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.create_text(
            40.0,
            43.0,
            anchor="nw",
            text="Administrator",
            fill="#808080",
            font=("Montserrat Bold", 16 * -1),
        )
        canvas.place(x=0, y=0)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(645.0, 432.0, image=image_image_2)
        # print(type(image_1))
        # print(type(image_image_1))
        # print(image_image_1)


class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Create a canvas
        canvas = tk.Canvas(
            self,
            bg="#F1F5F9",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.create_text(
            844.0,
            43.0,
            anchor="nw",
            text="Administrator",
            fill="#808080",
            font=("Montserrat Bold", 16 * -1),
        )
        canvas.place(x=0, y=0)

        # # Create a button
        # button = tk.Button(self, text="Click Me")
        # button_window = canvas.create_window(400, 150, anchor=tk.CENTER, window=button)
        #
        # # Create an entry box
        # entry = tk.Entry(self)
        # entry_window = canvas.create_window(200, 200, anchor=tk.CENTER, window=entry)


# Create the window object
window = Window()
window.mainloop()
