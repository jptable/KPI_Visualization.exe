import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import random_data as rd
"""客戶資料"""
# 舊客戶資料，暫時隨機生成
# fns 是 five number summary
df = rd.randomIndustry()
cloth_rev_df = rd.randomRevenue()
drink_rev_df = rd.randomRevenue()

# 產生一個新客戶的資料
# fns 是 five number summary
client_df = rd.randomIndustry()
cloth_client_rev_df = rd.randomRevenue()
drink_client_rev_df = rd.randomRevenue()

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.createWidgets()

    def createWidgets(self):
        fig = plt.figure(figsize=(8, 4), dpi=100)
        ax1 = fig.add_subplot()
        ax1.set(title='KPI Visualization')
        fig2 = plt.figure(figsize=(8, 4), dpi=100)
        ax2 = fig2.add_subplot()
        ax2.set(title='Revenue Visualization')
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.draw()

        canvas2 = FigureCanvasTkAgg(fig2, master=window)
        canvas2.get_tk_widget().grid(row=1, column=0)
        canvas2.draw()

        self.plotbutton1 = tk.Button(master=window, text="提交", command=lambda: self.dash1(canvas,ax1))
        self.plotbutton1.grid(row=0, column=2)
        self.plotbutton2 = tk.Button(master=window, text="提交", command=lambda: self.dash2(canvas2,ax2))
        self.plotbutton2.grid(row=1, column=2)

    def callbackFunc_ax1(event):
        return list_box_ax1.get()
    def callbackFunc_ax2(event):
        return list_box_ax2.get()

    def dash1(self, canvas, ax1):
        label_ax1 = ['CPM', 'CPC', 'CTR', 'CPA']
        text = self.callbackFunc_ax1()
        x = [0.8, 1.8, 2.8, 3.8]
        x_new = [1, 2, 3, 4]
        if text == 'mean':
            h = [df['CPM'].mean(),
                 df['CPC'].mean(),
                 df['CTR'].mean(),
                 df['CPA'].mean()]
            h_new = [client_df['CPM'].mean(),
                     client_df['CPC'].mean(),
                     client_df['CTR'].mean(),
                     client_df['CPA'].mean()]
        elif text == 'max':
            h = [df['CPM'].max(),
                 df['CPC'].max(),
                 df['CTR'].max(),
                 df['CPA'].max()]
            h_new = [client_df['CPM'].max(),
                     client_df['CPC'].max(),
                     client_df['CTR'].max(),
                     client_df['CPA'].max()]
        elif text == 'min':
            h = [df['CPM'].min(),
                 df['CPC'].min(),
                 df['CTR'].min(),
                 df['CPA'].min()]
            h_new = [client_df['CPM'].min(),
                     client_df['CPC'].min(),
                     client_df['CTR'].min(),
                     client_df['CPA'].min()]

        elif text == 'median':
            h = [df['CPM'].median(),
                 df['CPC'].median(),
                 df['CTR'].median(),
                 df['CPA'].median()]
            h_new = [client_df['CPM'].median(),
                     client_df['CPC'].median(),
                     client_df['CTR'].median(),
                     client_df['CPA'].median()]

        ax1.clear()  # clear axes from previous plot
        ax1.set(title='KPI Visualization')
        ax1.barh(x_new, h_new, height=0.2, color='c', tick_label=label_ax1, label='new client data')
        ax1.barh(x, h, height=0.2, color='gray', label='client history')
        ax1.legend(loc='best', facecolor='white', framealpha=1, frameon=True)
        canvas.draw()

    def dash2(self, canvas2, ax2):

        text_ax2 = self.callbackFunc_ax2()
        x2 = ['2021/1', '2021/2', '2021/3', '2021/4', '2021/5', '2021/6', '2021/7', '2021/8', '2021/9', '2021/10',
              '2021/11', '2021/12',
              '2022/1', '2022/2', '2022/3', '2022/4', '2022/5', '2022/6', '2022/7', '2022/8', '2022/9', '2022/10',
              '2022/11', '2022/12']
        client_x2 = ['2021/1', '2021/2', '2021/3', '2021/4', '2021/5', '2021/6', '2021/7', '2021/8', '2021/9',
                     '2021/10', '2021/11', '2021/12',
                     '2022/1', '2022/2', '2022/3', '2022/4', '2022/5', '2022/6', '2022/7', '2022/8', '2022/9',
                     '2022/10', '2022/11', '2022/12']

        if text_ax2 == 'cloth':
            y2 = cloth_rev_df['Revenue']
            client_y2 = cloth_client_rev_df['Revenue']
        elif text_ax2 == 'drink':
            y2 = drink_rev_df['Revenue']
            client_y2 = drink_client_rev_df['Revenue']

        ax2.clear()  # clear axes from previous plot

        # 繪製折線圖 ax2
        ax2.plot(x2, y2, color='gray')
        ax2.plot(client_x2, client_y2, color='blue')
        ax2.set(title='Revenue Visualization')
        plt.ylim(0, 200)
        plt.xticks(['2021/1', '2021/6', '2022/1', '2022/6', '2022/12'])
        canvas2.draw()


window = tk.Tk()
window.geometry("1000x900")
app = App(master=window)
window.resizable(False, False)

list_box_ax1 = ttk.Combobox(master=window, values=['mean', 'median', 'min', 'max'])
list_box_ax1.current(0)
list_box_ax1.grid(row=0, column=1)
list_box_ax2 = ttk.Combobox(master=window, values=["cloth", 'drink'])
list_box_ax2.current(0)
list_box_ax2.grid(row=1, column=1)

window.mainloop()



