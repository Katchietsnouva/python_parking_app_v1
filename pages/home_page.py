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

class HomePage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the home page
        authenticated_user = self.page_controller.get_authenticated_user()
        
        greeting_label = CTkLabel(self, text=f"Welcome to the Home Page {authenticated_user}!", font=("ar", 15, "bold"))
        greeting_label.pack(pady=20)

        logout_button = CTkButton(self, text="Logout", command=self.page_controller.show_login_page)
        logout_button.pack(pady=10)

        Car_register_button = CTkButton(self, text="Register", command=self.page_controller.show_registration_page)
        Car_register_button.pack(pady=10)

        book_parking_button = CTkButton(self, text="Book Parking", command=self.page_controller.show_booking_page)
        book_parking_button.pack(pady=10)

        extend_parking_button = CTkButton(self, text="Extend Parking", command=self.page_controller.show_extend_parking_page)
        extend_parking_button.pack(pady=10)

        profit_loss_button = CTkButton(self, text="Profit/Loss", command=self.page_controller.show_profit_loss_page)
        profit_loss_button.pack(pady=10)
