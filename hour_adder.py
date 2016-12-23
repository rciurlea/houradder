#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

class CalculatorApp(object):
    def __init__(self):
        self.minutes = 0
        self.root = tk.Tk()
        self.total = tk.StringVar()
        self.current = tk.StringVar()
        self.root.title("Adder")
        self.root.resizable(width=False, height=False)
        content = ttk.Frame(self.root, padding=(10, 10, 10, 10))

        total_label = ttk.Label(content, text="00:00", font="bold", textvariable=self.total)
        text_field = ttk.Entry(content, width=9, justify="center", textvariable=self.current)
        add_button = ttk.Button(content, text="Add", command=self.add)
        clr_button = ttk.Button(content, text="Clear", command=self.clr)

        content.grid(column=0, row=0, sticky="nsew")
        
        total_label.grid(column=0, row=0)
        text_field.grid(column=0, row=1, pady=10)
        add_button.grid(column=0, row=2)
        clr_button.grid(column=0, row=3, pady=(10, 0))

        self.total.set("00:00")
        text_field.focus()
        self.root.bind("<Return>", self.add)

    def start(self):
        self.root.mainloop()

    def h_to_m(self, x):
        return (x // 100) * 60 + x % 100

    def m_to_hm(self, x):
        return "%d:%02d" % (x // 60, x % 60)

    def add(self, *args):
        try:
            minutes = int(self.current.get())
            self.minutes += self.h_to_m(minutes)
            self.total.set(self.m_to_hm(self.minutes))
            self.current.set("")
        except:
            pass

    def clr(self, *args):
        self.minutes = 0
        self.total.set("00:00")
        self.current.set("")
        
if __name__ == "__main__":
    c = CalculatorApp()
    c.start()
