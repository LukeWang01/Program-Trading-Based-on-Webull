import os
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Text, PhotoImage, filedialog, messagebox

import schedule

from strategy.Strategy import Strategy
from utils.dataIO import logging_info


class StrategyMonitor(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        self.name = "StrategyMonitor"
        self.parent = parent
        self.current = False

        self.imported_list = []
        self.running_list = []
        self.strategy_obj_list = []
        # self.strategy_job_list = []

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
            707.0,
            anchor="nw",
            text="placeholder for dji",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.spx = self.canvas.create_text(
            273.0,
            707.0,
            anchor="nw",
            text="placeholder for spx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.ixic = self.canvas.create_text(
            404.0,
            707.0,
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
            text=" - ",
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
            if 425 <= x <= 551 and 225 <= y <= 251:
                self.select_strategy()
            elif 285 <= x <= 409 and 588 <= y <= 617:
                self.run_strategy()
            elif 444 <= x <= 568 and 596 <= y <= 626:
                self.cancel_strategy()

    def update_data(self):
        self.update_market_status()

    def select_strategy(self):
        relative_path = "strategy"  # Relative path of the folder under the current folder
        initial_dir = os.path.join(os.getcwd(), relative_path)
        file_path = filedialog.askopenfilename(title="Select a file", initialdir=initial_dir,
                                               filetypes=[("Python files", "*.py"), ("All files", "*.*")])

        if file_path:
            file_name = os.path.basename(file_path)
            # print("Selected file:", file_name)
            if file_name not in self.imported_list:
                self.set_imported_list(file_name)
                self.imported_list.append(file_name)
                self.set_current_strategy(file_name)
                logging_info(f"Imported strategy: {file_name}")

    def run_strategy(self):
        if self.parent.trader.is_trader_logged_in():
            if self.imported_list:
                if set(self.imported_list) == set(self.running_list):
                    messagebox.showinfo("Oops", "All strategies are running!")
                else:
                    for file_name in self.imported_list:
                        if file_name in self.running_list:
                            continue
                        strategy_obj = self.get_strategy_obj(file_name)
                        schedule.every().minute.at(":01").do(strategy_obj.strategy_decision).tag('strategy_jobs')

                        self.running_list.append(file_name)
                        self.strategy_obj_list.append(strategy_obj)
                        print('running strategy: ', file_name)
                        logging_info(f"Add running strategy: {file_name}")
                        self.parent.show_info_message(f"Running strategy: {file_name}")
                        # print(self.imported_list)
                        # print(self.running_list)
                        # print(self.strategy_obj_list)
            else:
                messagebox.showinfo("Oops", "Please select a strategy first!")
        else:
            self.parent.logged_in = False
            messagebox.showinfo("Oops", "To run the strategy, please login first!")

    def get_strategy_obj(self, filename) -> Strategy:
        strategy_name = filename[:-3]
        namespace = {}
        new_strategy_code = f"""
from strategy.{strategy_name} import {strategy_name}
strategy_instance = {strategy_name}()
"""
        # dynamic code should start without indentation
        exec(new_strategy_code, namespace)
        strategy_obj = namespace['strategy_instance']
        strategy_obj.parent = self.parent
        strategy_obj.update_strategy_profile()
        return strategy_obj

    def cancel_strategy(self):
        schedule.clear('strategy_jobs')
        self.imported_list = []
        self.running_list = []
        self.strategy_obj_list = []
        self.empty_imported_list()
        self.parent.show_info_message("All strategies are cancelled!")
        logging_info("Strategies cancelled!")

    def msg_clicked(self, event):
        # print(f"{self.name}: Message clicked")
        # Not core function, implement later
        pass

    def notify_clicked(self, event):
        # print(f"{self.name}: Notify clicked")
        # Not core function, implement later
        pass

    def update_market_status(self):
        self.canvas.itemconfig(self.spx, text=self.parent.spx_price)
        self.canvas.itemconfig(self.dji, text=self.parent.dji_price)
        self.canvas.itemconfig(self.ixic, text=self.parent.ixic_price)

    def set_quoter_stream(self, text):
        # txt = self.get_quoter_stream() + text
        # self.entry_2_quoter_stream.delete(1.0, tk.END)
        self.entry_2_quoter_stream.insert(tk.END, text)
        self.entry_2_quoter_stream.see(tk.END)

    def get_quoter_stream(self):
        return self.entry_2_quoter_stream.get(1.0, tk.END)

    def set_strategy_stream(self, text):
        txt = self.get_strategy_stream() + text
        self.entry_1_strategy_stream.delete(1.0, tk.END)
        self.entry_1_strategy_stream.insert(1.0, txt)
        self.entry_1_strategy_stream.see(tk.END)

    def get_strategy_stream(self):
        return self.entry_1_strategy_stream.get(1.0, tk.END)

    def set_imported_list(self, text):
        txt = self.get_imported_list() + text
        self.entry_3_imported_list.delete(1.0, tk.END)
        self.entry_3_imported_list.insert(1.0, txt)
        self.entry_3_imported_list.see(tk.END)

    def empty_imported_list(self):
        self.entry_3_imported_list.delete(1.0, tk.END)

    def get_imported_list(self):
        return self.entry_3_imported_list.get(1.0, tk.END)

    def set_current_strategy(self, text):
        self.canvas.itemconfig(self.current_strategy, text=text)
