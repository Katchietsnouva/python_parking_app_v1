
# controllers/page_controller.py
# from controllers.user_controller import UserController  # Import UserController
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
import datetime

# from controllers.page_controller import PageController
from controllers.user_controller import UserController
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage
from pages.home_page import HomePage
from pages.booking_page import BookingPage
from pages.extend_packing_page import ExtendParkingPage
from pages.payment_page import PaymentPage
from pages.profit_loss_page import ProfitLossPage

class PageController:
    def __init__(self, root):
        self.root = root
        self.login_page = LoginPage(root, self)
        self.home_page = HomePage(root, self)
        self.registration_page = RegisterPage(root, self)
        self.user_controller = UserController()  
        self.booking_page = BookingPage(root, self)
        self.extend_parking_page = ExtendParkingPage(root, self)
        self.payment_page = PaymentPage(root, self)
        self.profit_loss_page = ProfitLossPage(root, self)

        self.current_page = None
        self.authenticated_user = None

        self.show_login_page()

    def show_login_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.login_page
        self.login_page.show()

    def set_authenticated_user(self, username):
        self.authenticated_user = username

    def get_authenticated_user(self):
        return self.get_authenticated_user

    def show_home_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.home_page
        self.home_page.show()

    def show_registration_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.registration_page
        self.registration_page.show()
    
    def show_booking_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.booking_page
        self.booking_page.show()

    def show_extend_parking_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.extend_parking_page
        self.extend_parking_page.show()

    def show_payment_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.payment_page
        self.payment_page.show()

    def show_profit_loss_page(self):
        if self.current_page:
            self.current_page.hide()
        self.current_page = self.profit_loss_page
        self.profit_loss_page.show()
