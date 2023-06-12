import tkinter as tk


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.frames = {}

        # Create the frames
        frame1 = Frame1(self)
        frame2 = Frame2(self)

        # Store the frames in a dictionary
        self.frames[Frame1] = frame1
        self.frames[Frame2] = frame2

        frame1.pack()
        frame2.pack()

        # Show the initial frame
        self.show_frame(Frame1)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Frame 1")
        label.pack()

        canvas = tk.Canvas(
            self,
            bg="#F1F5F9",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)


class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Frame 2")
        label.pack()

        canvas = tk.Canvas(
            self,
            bg="#F1F5F9",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

# Create the window object
window = Window()
window.mainloop()
