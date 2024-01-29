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
# from pages.extend_packing_page import ExtendParkingPage
# from pages.payment_page import PaymentPage
# from pages.profit_loss_page import ProfitLossPage

class ProfitLossPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Profit/Loss Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # You might fetch revenue and expenses from a database or other sources
        revenue = 0  # Placeholder for revenue
        expenses = 0  # Placeholder for expenses

        # Display revenue and expenses
        revenue_label = CTkLabel(self, text=f"Total Revenue: ${revenue}")
        revenue_label.pack(pady=5)

        expenses_label = CTkLabel(self, text=f"Total Expenses: ${expenses}")
        expenses_label.pack(pady=5)

        # Calculate profit/loss
        profit_loss = revenue - expenses
        result_text = f"Profit: ${profit_loss}" if profit_loss >= 0 else f"Loss: ${abs(profit_loss)}"

        result_label = CTkLabel(self, text=result_text)
        result_label.pack(pady=20)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)
