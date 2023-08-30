import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Text, PhotoImage

from utils.dataIO import logging_info, logging_error


class TradingList(tk.Frame):
    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)
        self.name = "TradingList"
        self.parent = parent
        self.current = False

        # UI elements：
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./frame4")

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

        # Store references to the PhotoImage objects
        self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))

        self.image_image_1 = self.canvas.create_image(548.0, 364.0, image=self.image_1)
        self.image_image_2 = self.canvas.create_image(648.0, 385.0, image=self.image_2)
        self.image_3_msg = self.canvas.create_image(1012.0, 30.0, image=self.image_3)
        self.image_4_notify = self.canvas.create_image(971.0, 30.0, image=self.image_4)
        self.image_image_5 = self.canvas.create_image(328.0, 30.0, image=self.image_5)
        self.image_image_6 = self.canvas.create_image(534.0, 30.0, image=self.image_6)
        self.image_image_7 = self.canvas.create_image(534.0, 30.0, image=self.image_7)
        self.image_image_8 = self.canvas.create_image(328.0, 30.0, image=self.image_8)

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

        entry_bg_1 = self.canvas.create_image(443.0, 381.0, image=self.entry_image_1)
        self.entry_1_order_list = Text(
            self.canvas,
            bd=0,
            bg="#EFF4FB",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1_order_list.place(
            x=272.0,
            y=181.0,
            width=342.0,
            height=398.0
        )

        entry_bg_2 = self.canvas.create_image(846.0, 381.0, image=self.entry_image_2)
        self.entry_2_transactions = Text(
            self.canvas,
            bd=0,
            bg="#EFF4FB",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2_transactions.place(
            x=675.0,
            y=181.0,
            width=342.0,
            height=398.0
        )

        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.frame_clicked)

        self.canvas.tag_bind(self.image_3_msg, "<Button-1>", self.msg_clicked)
        self.canvas.tag_bind(self.image_4_notify, "<Button-1>", self.notify_clicked)

    def frame_clicked(self, event):
        x = event.x
        y = event.y
        if x <= 200:
            # Sidebar area clicked
            # print("Sidebar clicked, frame0")
            self.parent.sidebar_clicked(x, y)
        elif 200 <= x <= 1096 and y <= 60:
            # Top bar area clicked
            # print("Top_bar clicked, frame0")
            self.parent.top_bar_clicked(x, y)
        else:
            # frame area clicked
            pass

    def update_data(self):
        self.update_market_status()
        self.set_order_list()
        self.set_transactions()

    def msg_clicked(self, event):
        # print(f"{self.name}: Message clicked")
        # not core function, implement later
        pass

    def notify_clicked(self, event):
        # print(f"{self.name}: Notify clicked")
        # not core function, implement later
        pass

    def get_order_list(self):
        try:
            data = self.parent.trader.get_pending_orders_history()
        except Exception as e:
            # print(e)
            logging_error(str(e))
            return "Webull API changed, no order found, please contact developer."
        res_str = ''
        if data:
            for order in data:
                line_str = ''
                try:
                    order_date = f"Create Date: {order['orders'][0]['createTime']}\n"
                    order_list_header = 'Ticker, Action, Qty, Price, Amount\n'
                    Ticker = order['orders'][0]['symbol']
                    Action = order['orders'][0]['action']
                    Qty = order['orders'][0]['totalQuantity']
                    Price = 0
                    if order['orders'][0]['orderType'] == 'LMT':
                        Price = order['orders'][0]['lmtPrice']
                    elif order['orders'][0]['orderType'] == 'STP':
                        Price = order['orders'][0]['auxPrice']
                    Amount = order['orders'][0]['placeAmount']
                    tmp_line = order_list_header + f"{Ticker}, {Action}, {Qty}, {Price}, {Amount}\n"
                    column_widths = [8, 8, 5, 8, 10]
                    formatted = ''
                    # Format and print the data with aligned columns
                    for line in tmp_line.split("\n"):
                        cells = line.split(",")
                        formatted += "".join(cell.strip().ljust(column_width) for cell, column_width in zip(cells, column_widths)) + "\n"
                    line_str += order_date + formatted + '-----------------------------' + '\n'
                except:
                    line_str = 'Order type not supported \n'
                res_str += line_str
            logging_info('Get trader order list successfully')
            return res_str
        else:
            return 'No pending orders'

    def get_transactions(self):
        data = self.parent.trader.get_filled_orders_history()
        res_str = ''
        if data:
            for order in data:
                if order['status'] == 'Filled':
                    line_str = ''
                    order_date = f"Filled Date: {order['orders'][0]['filledTime']}\n"
                    order_list_header = 'Ticker, Action, Qty, Price, Amount\n'
                    Ticker = order['orders'][0]['symbol']
                    Action = order['orders'][0]['action']
                    Qty = order['orders'][0]['filledQuantity']
                    Price = order['orders'][0]['avgFilledPrice']
                    Amount = order['orders'][0]['filledAmount']
                    tmp_line = order_list_header + f"{Ticker}, {Action}, {Qty}, {Price}, {Amount}\n"
                    column_widths = [8, 8, 5, 8, 10]
                    formatted = ''
                    # Format and print the data with aligned columns
                    for line in tmp_line.split("\n"):
                        cells = line.split(",")
                        formatted += "".join(
                            cell.strip().ljust(column_width) for cell, column_width in zip(cells, column_widths)) + "\n"
                    line_str += order_date + formatted + '-----------------------------' + '\n'
                    res_str += line_str
            logging_info('Get trader transaction list successfully')
            return res_str
        else:
            return 'No filled orders'

    def set_order_list(self):
        order_list = self.get_order_list()
        self.entry_1_order_list.delete(1.0, tk.END)
        self.entry_1_order_list.insert(1.0, order_list)
        # self.entry_1_order_list.see(tk.END)

    def set_transactions(self):
        transactions = self.get_transactions()
        self.entry_2_transactions.delete(1.0, tk.END)
        self.entry_2_transactions.insert(1.0, transactions)
        # self.entry_2_transactions.see(tk.END)

    def update_market_status(self):
        self.canvas.itemconfig(self.spx, text=self.parent.spx_price)
        self.canvas.itemconfig(self.dji, text=self.parent.dji_price)
        self.canvas.itemconfig(self.ixic, text=self.parent.ixic_price)

