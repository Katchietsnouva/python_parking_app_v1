import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
import datetime


class BasePage(ctk.CTkFrame):
    def __init__(self, master, page_controller):
        super().__init__(master)
        self.page_controller = page_controller
        self.create_widgets()

    def create_widgets(self):
        # Common widgets for all pages can go here
        pass

    def show(self):
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        if self.winfo_ismapped():  # Check if the widget is currently visible
            self.pack_forget()