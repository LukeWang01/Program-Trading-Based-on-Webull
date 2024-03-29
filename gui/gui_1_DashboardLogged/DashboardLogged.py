import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Text, PhotoImage

from utils.format_str import format_financial_number


class DashboardLogged(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.name = "DashboardLogged"

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
        self.image_3_msg = self.canvas.create_image(1012.0, 30.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4_notify = self.canvas.create_image(971.0, 30.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(328.0, 30.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(534.0, 30.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(534.0, 30.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(328.0, 30.0, image=self.image_image_8)

        self.dji = self.canvas.create_text(
            536.0,
            705.0,
            anchor="nw",
            text="placeholder for dji",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.spx = self.canvas.create_text(
            273.0,
            705.0,
            anchor="nw",
            text="placeholder for spx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.ixic = self.canvas.create_text(
            404.0,
            705.0,
            anchor="nw",
            text="placeholder for ndx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.text_order_pending = self.canvas.create_text(
            395.0,
            320.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_net_account_value = self.canvas.create_text(
            420.0,
            521.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_cash_balance = self.canvas.create_text(
            420.0,
            559.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_market_value = self.canvas.create_text(
            420.0,
            599.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_dayPL = self.canvas.create_text(
            370.0,
            399.0,
            anchor="nw",
            text="888.88",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_openPL = self.canvas.create_text(
            370.0,
            444.0,
            anchor="nw",
            text="888.88",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_dayPL_pct = self.canvas.create_text(
            465.0,
            399.0,
            anchor="nw",
            text="8.88%",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_openPL_pct = self.canvas.create_text(
            465.0,
            444.0,
            anchor="nw",
            text="8.88%",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_order_filled = self.canvas.create_text(
            395.0,
            281.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_order_placed = self.canvas.create_text(
            392.0,
            242.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_account_id = self.canvas.create_text(
            392.0,
            184.0,
            anchor="nw",
            text="88888",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.text_email = self.canvas.create_text(
            317.0,
            135.0,
            anchor="nw",
            text="emailplaceholder@gmail.com",
            fill="#64748B",
            font=("ArialMT", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(790.0, 400.0, image=self.entry_image_1)
        self.entry_1_my_positions = Text(
            self.canvas,
            bd=0,
            bg="#EFF4FB",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1_my_positions.place(x=545.0, y=190.0, width=490.0, height=420.0)

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
            pass

    def update_data(self):
        self.update_market_status()
        self.parent.trader.update_account_info()
        self.update_text_email(self.parent.trader.username)
        self.update_text_account_id(self.parent.trader.account_id)
        self.update_text_order_placed(self.parent.trader.order_placed)
        self.update_text_order_filled(self.parent.trader.order_filled)
        self.update_text_order_pending(self.parent.trader.order_pending)
        self.update_text_openPL_pct(self.parent.trader.openPL_pct)
        self.update_text_openPL(format_financial_number(self.parent.trader.openPL))
        self.update_text_dayPL_pct(self.parent.trader.dayPL_pct)
        self.update_text_dayPL(self.parent.trader.dayPL)
        self.update_text_market_value(format_financial_number(self.parent.trader.market_value))
        self.update_text_cash_balance(format_financial_number(self.parent.trader.cash_balance))
        self.update_text_net_account_value(format_financial_number(self.parent.trader.net_account_value))
        self.update_entry_my_positions(self.parent.trader.my_positions)

    def msg_clicked(self, event):
        # print(f"{self.name}: Message clicked")
        # Not core functionality, implement later
        pass

    def notify_clicked(self, event):
        # print(f"{self.name}: Notify clicked")
        # Not core functionality, implement later
        pass

    def update_text_email(self, text):
        self.canvas.itemconfig(self.text_email, text=text)

    def update_text_account_id(self, text):
        self.canvas.itemconfig(self.text_account_id, text=text)

    def update_text_order_placed(self, text):
        self.canvas.itemconfig(self.text_order_placed, text=text)

    def update_text_order_filled(self, text):
        self.canvas.itemconfig(self.text_order_filled, text=text)

    def update_text_openPL_pct(self, text):
        self.canvas.itemconfig(self.text_openPL_pct, text=text)

    def update_text_dayPL_pct(self, text):
        self.canvas.itemconfig(self.text_dayPL_pct, text=text)

    def update_text_openPL(self, text):
        self.canvas.itemconfig(self.text_openPL, text=text)

    def update_text_dayPL(self, text):
        self.canvas.itemconfig(self.text_dayPL, text=text)

    def update_text_market_value(self, text):
        self.canvas.itemconfig(self.text_market_value, text=text)

    def update_text_cash_balance(self, text):
        self.canvas.itemconfig(self.text_cash_balance, text=text)

    def update_text_net_account_value(self, text):
        self.canvas.itemconfig(self.text_net_account_value, text=text)

    def update_entry_my_positions(self, text):
        self.entry_1_my_positions.delete("1.0", "end")
        self.entry_1_my_positions.insert("end", text)

    def update_text_order_pending(self, text):
        self.canvas.itemconfig(self.text_order_pending, text=text)

    def update_market_status(self):
        self.canvas.itemconfig(self.spx, text=self.parent.spx_price)
        self.canvas.itemconfig(self.dji, text=self.parent.dji_price)
        self.canvas.itemconfig(self.ixic, text=self.parent.ixic_price)

