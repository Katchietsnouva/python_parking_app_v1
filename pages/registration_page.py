
# pages/register_page.py
# class RegistrationPage(BasePage):

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
import datetime

# from controllers.page_controller import PageController
# from controllers.user_controller import UserController
from pages.base_page import BasePage
# from pages.login_page import LoginPage
# from pages.registration_page import RegisterPage
# from pages.home_page import HomePage
# from pages.booking_page import BookingPage
# from extend_packing_page import ExtendParkingPage
# from payment_page import PaymentPage
# from profit_loss_page import ProfitLossPage

from models.user_model import UserModel

class RegisterPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Account Creation", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry fields for registration in  formation
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.car_var = tk.StringVar()
        self.email_var = tk.StringVar()

        username_label = CTkLabel(self, text="Username:")
        username_label.pack(pady=5)
        username_entry = CTkEntry(self, textvariable=self.username_var)
        username_entry.pack(pady=5)

        password_label = CTkLabel(self, text="Password:")
        password_label.pack(pady=5)
        password_entry = CTkEntry(self, textvariable=self.password_var, show="*")
        password_entry.pack(pady=5)

        name_label = CTkLabel(self, text="Name:")
        name_label.pack(pady=5)
        name_entry = CTkEntry(self, textvariable=self.name_var)
        name_entry.pack(pady=5)

        phone_label = CTkLabel(self, text="Phone Number:")
        phone_label.pack(pady=5)
        phone_entry = CTkEntry(self, textvariable=self.phone_var)
        phone_entry.pack(pady=5)

        car_label = CTkLabel(self, text="Car Number Plate:")
        car_label.pack(pady=5)
        car_entry = CTkEntry(self, textvariable=self.car_var)
        car_entry.pack(pady=5)

        email_label = CTkLabel(self, text="Email:")
        email_label.pack(pady=5)
        email_entry = CTkEntry(self, textvariable=self.email_var)
        email_entry.pack(pady=5)

        register_button = CTkButton(self, text="Register", command=self.register_user)
        register_button.pack(pady=10)

        home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        home_button.pack(pady=10)

    def register_user(self):
        # Get user registration information
        username = self.username_var.get()
        password = self.password_var.get()
        name = self.name_var.get()
        phone = self.phone_var.get()
        car_plate = self.car_var.get()
        email = self.email_var.get()

        # Validate and save user registration (you can save to a file or database)
        if username and password and name and phone and car_plate and email:
            user_model = UserModel(username, password, name, phone, car_plate, email)
            registration_successful = self.page_controller.user_controller.register_user(user_model)

            if registration_successful:
                messagebox.showinfo("Registration Successful", "User registered successfully!")
                self.page_controller.show_login_page()
            else:
                messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        else:
            messagebox.showerror("Registration Failed", "Please fill in all fields.")
