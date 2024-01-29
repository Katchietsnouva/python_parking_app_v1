# __main__.py
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
import datetime
from controllers.page_controller import PageController
# from controllers.user_controller import UserController
# from pages.login_page import LoginPage
# from pages.home_page import HomePage


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Parking Management System")
    app.geometry("400x600")

    page_controller = PageController(app)

    app.mainloop()